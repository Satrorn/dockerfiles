# qb_dispatch

作为 qbittorrent 的外部程序，将电影 / 剧集文件用硬链接到指定目录，便于 Emby / Jellyfin 使用。

## 介绍

目标是让 Emby /Jellyfin 既能自动刮削又能兼顾保种。
- 因为文件名开头的中文，导致TMDB搜索不到相应电影/剧集，刮削不了
- 改文件名就可以刮削，但是影响保种。

解决方案是通过硬链接来实现改名，用于 Emby /Jellyfin 的媒体库。

把电影和剧集分目录下载，分别分 raw 和 link 两个目录， raw 作为 qb 的下载目录，link 是创建硬链接作为媒体库文件夹的目录。目录结构像这样设置：

```bash
$ tree MediaData
...
├── episodes
│   ├── link
│   └── raw
├── films
│   ├── link
│   └── raw
...
```

- 在 qb 里创建 categories，分别为 films， episodes
- 在添加种子下载的时候选择对应的 categories
- 种子下载完 qb 会自动调用脚本，脚本会分析文件名，提取相关信息，在 link 目录下建立相应的文件夹，然后创建硬链接
- 链接失败或文件名匹配错误的会在 log 里报 warning 和 error，需要手动解决
- 即使链接对的，Emby / Jellyfin 也不一定能正确刮削
 - 原因可能有：文件名里面的年代不一定和 TMDB 用的同一个（就是电影上映时间按电影节算还是按影院上映算）
 - 多种译名，比如法语电影用英语名字搜索可能搜不到，也需要手动检查

## 配置

- 在 qb 中将选项 `Option -> Download -> Run external program on torrent completion` 设置为 `/path_of_script/qb_dispatch.py -f "%F" -c "%L" -n "%N"`
- 根据需求配置 config.ini
- 在 qb 中添加下载的时候，选择相应的类型，例如 "episodes"， "films"

### 配置文件

- **language**：设置语言优先级，如果设置成 `zh`，在没有中文的时候会回退到英文
- **tmdb-refine**：需要先申请 tmdb 的 api-key，启用会根据 tmdb 的搜索信息完善电影 / 剧集名字
- **film-link-binding**：qb 中的 类型（categories） 与需要链接到的文件夹的一一对应关系，支持多个类型名与目录对应
- **docker-path-replacement**：qb 的 docker 里没有 python 时的间接方法中的目录替换