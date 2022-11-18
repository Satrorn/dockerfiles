#!/usr/bin/python3
# this script work as qbittorrent's external program and will
# rename and create hard link for emby/jellyfin to scrape easily
# film and episodes naming rule follows https://jellyfin.org/docs/general/server/media/movies.html
# 2021-01-26 by spartazhc

# Usage: download this python script, setup in qbittorrent
# Option -> Download -> Run external program on torrent completion
# set as /path_of_script/qb_dispatch.py -f "%F" -c "%L" -n "%N"
# Set categories "episodes" and "films", choose them when add torrent
# Note: for non-standard film name, script will fail or mismatch

# 2021-02-02 add country_codes and cut_types, code clean
# 2021-02-23 fix regex for punctuations in film name; better error logging; add episode-chi
# 2021-02-25 use git repository to manage other than gist

import re
import os
import sys
import subprocess
import argparse
import logging
import configparser
import tmdbsimple as tmdb
import tinydb

# bluray source
country_codes = ["BFI", "CEE", "CAN", "CHN", "ESP", "EUR", "FRA", "GBR", "GER", "HKG", "IND", "ITA", "JPN", "KOR", "NOR", "NLD", "POL", "RUS", "TWN", "USA"]
cut_types = { 'cc': 'CC', 'criterion': 'CC', 'director': 'Directors Cut', 'extended': 'Extended Cut', 'uncut': 'UNCUT', 'remastered': 'Remastered', 'repack': 'Repack', 'uncensored': 'Uncensored', 'unrated': 'Unrated'}

def is_video_or_subtitle(fname):
    video_suffix = ['mp4', 'mkv', 'avi', 'wmv', 'm2ts', 'rmvb', 'ts',
                    'webm', 'ogg', 'srt', 'ass', 'sup', 'vtt', 'aac', 'ac3',
                    'mp3', 'opus']
    fname = fname.lower()
    for suffix in video_suffix:
        if fname.endswith(suffix):
            return True
    return False

def getname_episodes(ori_name, conf):
    tmdb_refine = conf.get('tmdb_refine')
    filter_list = conf.get('filter_list')
    zh_in = conf.get('zh_in')
    year_in = conf.get('year_in')
    file_mode = False
    if is_video_or_subtitle(ori_name):
        # file mode, do not filter S\d+|E\d+ (some TV shows have name for every episode)
        file_mode = True
        to_filter = ori_name
    else:
        to_filter = re.sub('S\d{2}-?|E\d{2}|合集|全\d+集|Part\d+-\d+|Complete|AMZN|中英.*CMCT.*', '', ori_name)
    fullname = re.sub(filter_list, '', to_filter)
    match = re.match(u"([\u4E00-\u9FA5]?.*[\u4E00-\u9FA5]+).*", fullname)
    # 1. get chinese name
    if match:
        vf_zh = match[1].replace('.', ' ')
    else:
        vf_zh = ""
    if zh_in:
        vf_zh = zh_in
    # 2. get english name
    fs = fullname.split('.')
    name_t = []
    start_flag = 0
    for item in fs:
        if not item:
            continue
        if not start_flag and (item[0].isupper() or item[0].isdigit()):
            start_flag = 1
        elif item[0].isdigit() or (file_mode == True and (item[0]=='S' or item[0]=='E')) \
            or item[0] == '-' or ("web" in item.lower()) or ("blu" in item.lower()):
            break
        if start_flag:
            name_t.append(item)
    vf_en = ' '.join(name_t)
    # 3. get year
    match = re.search('19\d{2}|20\d{2}', fullname)
    if match:
        year = match[0]
    else:
        year = ""
    if year_in:
        year = year_in
    logging.debug(f"getname_episodes: zh:{vf_zh}, en:{vf_en}, year:{year}")
    if tmdb_refine:
        # if it is not S01, than du not use year to refine
        match = re.search("S\d{2}", ori_name)
        if match and match[0] != 'S01':
            year = ""
        vf_zh, vf_en, year = refine_episode(vf_zh, vf_en, year)
        logging.debug(f"tmdb_refine: zh:{vf_zh}, en:{vf_en}, year:{year}")
    else:
        logging.debug(f"tmdb_refine: disabled")
    return vf_zh, vf_en, year

def refine_translations(id, isTv):
    vf_zh = ''
    vf_en = ''
    if isTv:
        tv = tmdb.TV(id=id)
        trans_ret = tv.translations()
    else:
        movie = tmdb.Movies(id=id)
        # TODO: this info is better to use
        info_ret = movie.info()
        if check:
            print(info_ret)
        if movie.original_language == 'en' and movie.original_title:
            vf_en = movie.original_title
        if movie.original_language in ['zh', 'cn'] and movie.original_title:
            vf_zh = movie.original_title
        trans_ret = movie.translations()
    if trans_ret:
        for item in trans_ret['translations']:
            if item['iso_3166_1'] == 'CN' and item['iso_639_1'] == 'zh' and not vf_zh:
                vf_zh = item['data']['name'] if isTv else item['data']['title']
            elif item['iso_3166_1'] == 'US' and item['iso_639_1'] == 'en' and not vf_en:
                vf_en = item['data']['name'] if isTv else item['data']['title']
                print(f"find vf_en {vf_en}")
            else:
                continue
    else:
        logging.warning(f"fail in refine translation: {id} (TV={isTv})")

    if not vf_en and not isTv:
        vf_en = movie.title

    return vf_zh, vf_en

def refine_episode(in_zh, in_en, in_year):
    vf_zh , vf_en, year = in_zh, in_en, in_year
    if in_zh:
        search_zh = tmdb.Search()
        search_zh.tv(query=in_zh, first_air_date_year=in_year, language='zh')
        if search_zh.results:
            item = search_zh.results[0]
            if item['original_language'] == 'en':
                vf_en = item['original_name']
            else:
                _, vf_en = refine_translations(item['id'], isTv=True)
            return item['name'], vf_en, item['first_air_date'][:4]
    # no in_zh input or search_zh no results
    search_en = tmdb.Search()
    search_en.tv(query=in_en, first_air_date_year=in_year, language='en')
    if search_en.results:
        # print(search_en.results)
        idx = 0
        for i, item in enumerate(search_en.results):
            # with backdrop and perfect name match
            if item['backdrop_path'] is not None and item['name'] == in_en:
                idx = i
                break
        if idx == 0:
            for i, item in enumerate(search_en.results):
                # first item with backdrop
                if (item['backdrop_path'] is not None):
                    idx = i
                    break
        item = search_en.results[idx]
        year = item['first_air_date'][:4]
        vf_en = item['name']
        if item['original_language'] == "zh":
            vf_zh = item['original_name']
        else:
            vf_zh, _ = refine_translations(item['id'], isTv=True)
    else:
        print('refine_episode: fail to search on tmdb')

    return vf_zh, vf_en, year

def refine_films(in_zh, in_en, in_year, zh_first):
    vf_zh, vf_en, year, item = in_zh, in_en, in_year, None
    print(f"> refine_films {vf_zh} / {vf_en} ({year})")
    logging.info(f"> refine_films {vf_zh} / {vf_en} ({year})")
    search_en = tmdb.Search()
    if not zh_first:
        search_en.movie(query=in_en, year=in_year, language='en', include_adult=True)
    else:
        search_en.movie(query=in_zh, year=in_year, language='zh', include_adult=True)
    if not search_en.results:
        # try france name
        search_en.movie(query=in_en, year=in_year, language='fre', include_adult=True)
    if not search_en.results and in_zh:
        # when we have name in zh
        search_en.movie(query=in_zh, year=in_year, language='zh', include_adult=True)
    if not search_en.results:
        # in case year error
        search_en.movie(query=in_en, language='en', include_adult=True)
    if not search_en.results and in_zh:
        # when we have name in zh
        search_en.movie(query=in_zh, language='zh', include_adult=True)
    if search_en.results:
        # print(search_en.results)
        idx = 0
        for i, item in enumerate(search_en.results):
            # with backdrop and perfect name match
            if item['backdrop_path'] is not None and item['title'] == in_en:
                idx = i
                break
        if idx == 0:
            for i, item in enumerate(search_en.results):
                # first item with backdrop
                if (item['backdrop_path'] is not None):
                    idx = i
                    break
        item = search_en.results[idx]
        year = item['release_date'][:4]
        vf_en = item['title']
        # if item['original_language'] == "zh":
        #     vf_zh = item['original_title']
        # else:
        vf_zh, vf_en = refine_translations(item['id'], isTv=False)
    else:
        print(f"fail in search tmdb: {in_en} ({in_year})")
        logging.warning(f"fail in search tmdb: {in_en} ({in_year})")
    return vf_zh, vf_en, year, item

def link_episodes(spath, target, linkdir):
    fullname = os.path.basename(spath)
    logging.info(f"'{fullname}' => '{target}'")
    if check:
        print(f"'{fullname}' => '{target}'")
    if not target:
        logging.error(f"episodes: no short name on '{fullname}', check!")
        return
    if not os.path.exists(os.path.join(linkdir, target)) and not check:
        os.makedirs(os.path.join(linkdir, target))
    # print(spath)
    if os.path.isdir(spath):
        for root, dirs, files in os.walk(spath):
            vfiles = [f for f in files if is_video_or_subtitle(f)]
            # print(vfiles)
            if not vfiles:
                continue
            series_base = os.path.basename(root)
            m = re.match(r".*(S\d+).*", series_base)
            if not m:
                if 'SP' in series_base:
                    season = 'SP'
                else:
                    logging.warning(f"episodes: no season number found, regard as only one season.")
                    season = "S01"
            else:
                season = m[1]
            season_dir = os.path.join(linkdir, target, season)
            if not os.path.exists(season_dir) and not check:
                os.makedirs(season_dir)
            vfiles.sort()
            for vf in vfiles:
                se_str = season
                sp = re.findall(r"(SP[E]?\d*)", vf)
                if not sp:
                    ep_list = re.findall(r"E[Pp]?(\d+)", vf)
                    if not ep_list:
                        logging.warning(f"episodes: check special: {vf}")
                        continue
                    else:
                        for ep in ep_list:
                            se_str += "E" + ep
                else:
                    se_str += sp[0]
                link_cmd = f"ln \"{os.path.join(root, vf)}\" \"{os.path.join(season_dir, se_str)}.{vf.split('.')[-1]}\""
                if check:
                    print(link_cmd)
                    continue
                logging.info(f"episodes: link: {link_cmd}")
                try:
                    subprocess.check_output(link_cmd, stderr=subprocess.STDOUT, shell=True)
                except subprocess.CalledProcessError as e:
                    logging.error(f"episodes: link: {e.output}")
    else:
        if not is_video_or_subtitle(spath):
            logging.warning(f"input file is not media file")
            return
        vf = os.path.basename(spath)
        m = re.match(r".*(S\d+).*", vf)
        if not m:
            if 'SP' in vf:
                season = 'SP'
            else:
                logging.warning(f"episodes: no season number found, regard as only one season.")
                season = "S01"
        else:
            season = m[1]
        season_dir = os.path.join(linkdir, target, season)
        if not os.path.exists(season_dir) and not check:
            os.makedirs(season_dir)
        se_str = season
        sp = re.findall(r"(SP[E]?\d*)", vf)
        if not sp:
            ep_list = re.findall(r"E[Pp]?(\d+)", vf)
            if not ep_list:
                logging.warning(f"episodes: check special: {vf}")
            else:
                for ep in ep_list:
                    se_str += "E" + ep
        else:
            se_str += sp[0]
        link_cmd = f"ln \"{spath}\" \"{os.path.join(season_dir, se_str)}.{vf.split('.')[-1]}\""
        if check:
            print(link_cmd)
            return
        logging.info(f"episodes: linkf: {link_cmd}")
        try:
            subprocess.check_output(link_cmd, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"episodes: linkf: {e.output}")

def dispatch_episodes(path, conf):
    fname = os.path.basename(path)
    vf_zh, vf_en, year = getname_episodes(fname, conf)
    # print(vf_zh, vf_en)
    if conf.get('lang') == 'zh' and vf_zh != "":
        vf = f"{vf_zh}" if not year else f"{vf_zh} ({year})"
    else:
        vf = f"{vf_en}" if not year else f"{vf_en} ({year})"
    link_episodes(path, vf, conf.get('linkdir'))

def link_film(vf, root, conf):
    linkdir = conf.get('linkdir')
    filter_list = conf.get('filter_list')
    version_list = conf.get('version_list')
    tmdb_refine = conf.get('tmdb_refine')
    lang = conf.get('lang')
    dir_lang = conf.get('dir_lang')
    db = conf.get('db')
    zh = conf.get('zh')

    vf_ori = os.path.basename(vf)
    if filter_list:
        vf_ori = re.sub(filter_list, "", vf_ori)
    if version_list:
        ver = re.search(version_list, vf_ori)
        vf_ori = re.sub(version_list, "", vf_ori)
    vf_ori = re.sub("\[.*\]|IMAX", "", vf_ori)
    m_zh = re.search(u"([\u4E00-\u9FA5]+.*[\u4E00-\u9FA5]+\d?)", vf_ori)
    # 1. get chinese name
    if m_zh:
        vf_zh = m_zh[1].replace('.', ' ')
    else:
        vf_zh = ""
        m_zh = re.search(u"([\u4E00-\u9FA5]+.*[\u4E00-\u9FA5]+\d?)", os.path.basename(root))
        if m_zh:
            vf_zh = m_zh[1].replace('.', ' ')
    if zh:
        vf_zh = zh
    # Remove Chinese
    vf_en = re.sub("[\u4E00-\u9FA5]+.*[\u4E00-\u9FA5]+.*?\.", "", vf_ori)
    logging.debug(f'vf_en after filter: "{vf_en}"')
    print(vf_en)
    m = re.search(r"\.?([\w,.'!?&:() -]+)\.(19\d{2}|20\d{2})+.*(720[pP]|1080[pP]|2160[pP])+.*(mkv|mp4|m2ts|srt|ass)+", vf_en)
    # TODO: deal with extra videos
    if "EXTRA" in vf_en or "FEATURETTE" in vf_en or "Sample" in vf_en or "sample" in vf_en or 'feature' in vf_en:
        return
    cut = ""
    country = ""
    # check FIFA country code
    for code in  country_codes:
        if code in vf_en:
            country = code
            break
    vf_en_lower = vf_en.lower()
    for key, val in cut_types.items():
        if key in vf_en_lower:
            cut = val
            # search again without cut
            vf_en = re.sub(key, '', vf_en, flags=re.IGNORECASE)
            m = re.search(r"\.?([\w,.'!?&:() -]+)\.(19\d{2}|20\d{2})+.*(720[pP]|1080[pP]|2160[pP])+.*(mkv|mp4|m2ts|srt|ass)+", vf_en)
            break
    # Normally, there should be either country or cut
    cut = country + cut
    if version_list and ver:
        if cut:
            cut += ' '
        cut += ver[0]
    if m is None:
        # sometimes there is no resolution in filename, maybe the uploader missed it
        m = re.search(r"([\w,.'!?&:() -]+).(19\d{2}|20\d{2})+.*(mkv|mp4|m2ts|srt|ass)+", vf_en)
        if m is None:
            print(f"vf_en: {vf_en}, fail in regex match")
            logging.error(f"vf_en: {vf_en}, fail in regex match")
            return
        name_en, year, reso, suffix = m[1], m[2], "1080p", m[3]
        if "AKA" in m[1]:
            try:
                name_en = re.match(r"([\w,.'!?&-]+)\.AKA.*", m[1])[1]
            except TypeError:
                print(f"vf_en: {vf_en}, fail in AKA regex match")
                logging.error(f"vf_en: {vf_en}, fail in AKA regex match")
        name_en = name_en.replace('.', ' ').strip()
        fname = f"{name_en} ({year}) - [{cut if cut else reso}].{suffix}"
        logging.warning(f"no resolution found, set as 1080p.")
    else:
        name_en, year, reso, suffix = m[1], m[2], m[3].lower(), m[4]
        if "AKA" in m[1]:
            try:
                name_en = re.match(r"([\w,.'!?&-]+)\.AKA.*", m[1])[1]
            except TypeError:
                print(f"vf_en: {vf_en}, fail in AKA2 regex match")
                logging.error(f"vf_en: {vf_en}, fail in AKA2 regex match")
        name_en = name_en.replace('.', ' ').strip()
        fname = f"{name_en} ({year}) - [{cut if cut else reso}].{suffix}"

    vf_dir = ''
    if tmdb_refine:
        ref_zh, ref_en, year, item = refine_films(vf_zh, name_en, year, bool(zh))
        if ref_en:
            name_en = ref_en
            if lang == 'en':
                fname = f"{ref_en} ({year}) - [{cut if cut else reso}].{suffix}"
        # print(f"after refine: {ref_zh}, {ref_en}, {year}")
        if ref_zh:
            if lang == 'zh':
                fname = f"{ref_zh} ({year}) - [{cut if cut else reso}].{suffix}"
            if dir_lang == 'zh':
                vf_dir = os.path.join(linkdir, f"{ref_zh} ({year})")
    if not vf_dir:
        vf_dir = os.path.join(linkdir, f"{name_en} ({year})")
    if not os.path.exists(vf_dir) and not check:
        os.makedirs(vf_dir)
    link_cmd = f"ln \"{os.path.join(root, vf)}\" \"{vf_dir}/{fname}\""
    if check:
        print(link_cmd)
        return vf_dir

    if tmdb_refine and db is not None and item:
        info = {
            'vf_en': name_en,
            'vf_zh': ref_zh,
            'link_cmd': link_cmd,
            **item
            }
        table = db.table('movies')
        Movie = tinydb.Query()
        if not table.search(Movie.vf_en == name_en):
            table.insert(info)
    if os.path.exists(f"{vf_dir}/{fname}"):
        logging.error(f"films: check: file already exists \"{vf_dir}/{fname}\", source: {root}/{vf}")
        return vf_dir
    logging.info(f"films: cmd: {link_cmd}")
    print(link_cmd)
    try:
        subprocess.check_output(link_cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"films: link: {e.output}")

    return vf_dir

def link_extras(path, film_dir):
    # https://jellyfin.org/docs/general/server/media/movies.html
    if not film_dir:
        logging.warning('link_extras: no input film_dir')
        return
    extras_dir = os.path.join(film_dir, 'extras')
    if not os.path.exists(extras_dir) and not check:
        os.makedirs(extras_dir)
    for root, dirs, files in os.walk(path):
        vfiles = [f for f in files if is_video_or_subtitle(f)]
        if not vfiles:
            continue
        for vf in vfiles:
            link_cmd = f"ln \"{os.path.join(root, vf)}\" \"{extras_dir}/{vf}\""
            if check:
                print(link_cmd)
                continue
            if os.path.exists(f"{film_dir}/{vf}"):
                logging.error(f"extras: check: file already exists \"{film_dir}/{vf}\"")
                continue
            logging.info(f"extras: cmd: {link_cmd}")
            try:
                subprocess.check_output(link_cmd, stderr=subprocess.STDOUT, shell=True)
            except subprocess.CalledProcessError as e:
                logging.error(f"extras: link: {e.output}")

def dispatch_films(path, conf):
    if not os.path.isdir(path) and is_video_or_subtitle(path):
        link_film(path, "", conf)
    for root, dirs, files in os.walk(path):
        # print(f"{root} | {dirs} | {files}")
        vfiles = [f for f in files if is_video_or_subtitle(f)]
        if not vfiles:
            continue
        for vf in vfiles:
            if vf.startswith('SP'):
                # may fail with empty film_dir
                link_extras(os.path.join(root, dir), film_dir)
                continue
            film_dir = link_film(vf, root, conf)
        for dir in dirs:
            if dir.lower() in ['extras', 'bonus']:
                link_extras(os.path.join(root, dir), film_dir)
                dirs.remove(dir)

check = False
if __name__ == '__main__':
    pwd = os.path.dirname(os.path.realpath(__file__))
    parser = argparse.ArgumentParser(
        description='qbittorrent download file dispatcher for nas')
    parser.add_argument('-f', "--file", required=True,
                        help="content path (root path for multifile torrent")
    parser.add_argument('-c', "--category", required=True,
                        help="torrent category")
    parser.add_argument("--config", default=os.path.join(pwd, "config.ini"),
                        help="config file")
    parser.add_argument('-z', "--zh", default='',
                        help="force zh name")
    parser.add_argument('-y', "--year", default=0,
                        help="force year")
    parser.add_argument('--check', action='store_true',
                        help="just check output, not do")
    args = parser.parse_args()
    if args.check:
        check=True
    # read config
    config = configparser.ConfigParser()
    config.read(args.config)
    if config['default']['tmdb-refine'] == 'yes':
        tmdb.API_KEY = config['default']['tmdb-apikey']
        tmdb_refine = True
    else:
        tmdb_refine = False
    logging.basicConfig(filename=os.path.join(pwd, config['default']['logpath']),
                        format='%(asctime)-15s %(levelname)s %(message)s',
                        level=logging.getLevelName(config['default']['loglevel']))
    ifile = args.file
    db = None
    if config['default']['db-path']:
        db = tinydb.TinyDB(config['default']['db-path'])

    # path replacement
    for substr in config['docker-path-replacement']:
        if substr in args.file:
            ifile = args.file.replace(substr, config['docker-path-replacement'][substr])
            break

    for cate in config['film-link-binding']:
        if args.category == cate:
            conf = {
                'linkdir': config['film-link-binding'][cate],
                'lang': config['default']['language'],
                'dir_lang': config['default']['film-dir-lang'],
                'tmdb_refine': tmdb_refine,
                'filter_list': config['filter-list']['films'],
                'version_list': config['version-list']['films'],
                'zh': args.zh,
                'db': db
                }
            dispatch_films(ifile, conf)
            sys.exit()

    for cate in config['episode-link-binding']:
        if args.category == cate:
            conf = {
                'linkdir': config['episode-link-binding'][cate],
                'lang': config['default']['language'],
                'tmdb_refine': tmdb_refine,
                'filter_list': config['filter-list']['episodes'],
                'version_list': config['version-list']['episodes'],
                'zh_in': args.zh,
                'year_in': args.year,
                }
            dispatch_episodes(ifile, conf)
            sys.exit()
