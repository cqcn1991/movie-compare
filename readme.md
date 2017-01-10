# 豆瓣和IMDB电影评分比较

## 项目介绍

平时，总能看到一些电影。虽然评分很高，但却并不好看，比如

![](./docs/example_movie.png)

仔细对比其和国外网站，比如IMDB的评分，可以发现评分差别很大

![](./docs/example_movie_comparison.png)

可以看到，国内豆瓣的评分是8.3，而国外IMDB仅仅为7.3。烂番茄，Metacritic的评分也不高

是不是有一种可能，因为这些电影很文艺、很小资，所以豆瓣的用户很喜欢，所以打了高分呢？ .... 这里的数据分析就是一次探索。

### 数据概况

选取了2008-2014 北美上映的电影，比较豆瓣和IMDB评分，看看两者是不是存在很大的差别。

### 结果

![](./docs/scatter_demo.gif)

[交互式评分比较散点图](https://cdn.rawgit.com/cqcn1991/movie-compare/master/movie_compare_all.html)

完整的分析notebook, 见[这里](http://nbviewer.jupyter.org/github/cqcn1991/movie-compare/blob/master/application.ipynb)

## 代码介绍

### Getting Started

0. 本项目基于Python 3，建议使用Anaconda安装

1. 安装若干packages

    pip install -r requirements.txt

2. 数据具体分析，在`application.ipynb`中

3. `movie_compare.pptx` 为介绍时所用的PPT

## Contact 

如果有任何问题，可以发issue，或者[在这里](https://www.douban.com/people/wohaobeia/)找我




