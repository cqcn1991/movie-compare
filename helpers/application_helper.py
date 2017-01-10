from .shared_imports import *
from .plot_print_helper import plt_configure


def set_chinese_font():
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['font.serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    sns.set_style({"font.sans-serif": ['simhei', 'Arial']})


def plot_movie_scatter_comparison(df, title='', type='rank', legend=True, regression=True):
    fig, ax = plt.subplots()
    # 1. plot scatter
    if type == 'rating':
        douban, imdb = df.db_rating, df.imdb_rating
        start, scale = 0, 10
    elif type =='rank_norm':
        douban, imdb = df.db_rank_norm, df.imdb_rank_norm
        start, scale = -4, 4
        deviation_range = 1.28
    else:
        douban, imdb = df.db_rank, df.imdb_rank
        start, scale = 0, 100
        deviation_range = 20
    x = [start, scale]
    plt.plot(x, x, '--', color='black', label='1:1')

    # 2. regression
    x = linspace(start, scale)
    if type != 'rating':
        plt.fill_between(x, x - deviation_range, x + deviation_range, alpha=0.15)
    if regression and len(df) >=20:
        fit = np.polyfit(douban, imdb, 1)
        fit_fn = np.poly1d(fit)
        plt.plot(x, fit_fn(x), '-', label='Regression')
    else:
        fit_fn = 'Not available'

    # 3. Plot scatter
    scatter_plot = ax.scatter(douban, imdb, alpha=0.3)

    plt.axis([start, scale, start, scale])
    if type == 'rating':
        plt_configure(xlabel='Douban Rating', ylabel='IMDB Rating', title=title)
    elif type == 'rank_norm':
        plt_configure(xlabel='Douban Rank (Normed)', ylabel='IMDB Rank (Normed)', title=title)
    else:
        plt_configure(xlabel='Douban Rank', ylabel='IMDB Rank', title=title)
    if legend == True:
        plt.gca().legend(loc='best')
    plt.gca().set_aspect('equal')
    return fig, fit_fn, scatter_plot


def plot_category_bars(categories, values):
    ind = np.arange(len(categories))  # the x locations for the groups
    width = 0.5       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, values, width)

    avg = np.average(values)
    ax.axhline(avg, linestyle='--', color='black', label='Average')

    ax.set_xticks(ind + width/2)
    ax.set_xticklabels(categories)
    fig.set_size_inches(8,3)
    plt_configure(legend=True)

    # return fig