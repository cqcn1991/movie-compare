# 豆瓣电影的评分靠谱吗？ —— 一点数据分析的视角

包括两部分

## 1. 豆瓣和IMDB 电影评分的比较

平时，总能看到一些电影，虽然评分很高，但却并不好看，比如白日梦想家

![](./docs/example_movie_comparison.png)

可以看到，国内豆瓣的评分是8.3，而国外IMDB仅仅为7.3。烂番茄，Metacritic的评分也不高

是不是有一种可能，因为这些电影很文艺、很小资，所以豆瓣的用户很喜欢，所以打了高分呢？ 

分析文章：[知乎](https://zhuanlan.zhihu.com/p/24815577), [豆瓣](https://www.douban.com/note/599456964/)

![](./docs/scatter_demo.gif)

[交互式评分比较散点图](https://cdn.rawgit.com/cqcn1991/movie-compare/master/movie_compare_all.html)

完整的分析notebook, 见[这里](http://nbviewer.jupyter.org/github/cqcn1991/movie-compare/blob/master/application.ipynb)

## 2. 豆瓣电影评分差异的比较

对于西游伏妖篇的分数，我很困惑

![](./docs/xiyou.png)

一方面，周星驰是我很喜欢的导演，怎么会这么差？ 另一方面，网上的评价差别也很大，让我很困惑，西游伏妖篇真的有这么难看吗？

为什么有些电影分数很高/低，但我们却并不理解？为什么有的电影，我们觉得不好看，但是评分却不错？ 

[交互式评分比较散点图](https://cdn.rawgit.com/cqcn1991/movie-compare/master/clusters.html)

完整的分析notebook, 见[这里](http://nbviewer.jupyter.org/github/cqcn1991/movie-compare/blob/master/movie2.ipynb)

## 代码介绍

### Getting Started

0. 本项目基于Python 3，建议使用Anaconda安装

1. 安装若干packages

    pip install -r requirements.txt

2. 数据分析，见`application.ipynb` 和 `movie2.ipynb`

## Contact 

如果有任何问题，可以发issue，或者[在这里](https://www.douban.com/people/wohaobeia/)找我




