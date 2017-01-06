from .shared_imports import *
from .plot_print_helper import plt_configure


def plot_movie_scatter_comparison(df, title='', type='rank'):
    fig, ax = plt.subplots()
    # 1. plot scatter
    if type == 'rating':
        douban, imdb = df.db_rating, df.imdb_rating
        scale = 10
    else:
        douban, imdb = df.db_rank, df.imdb_rank
        scale = 100
    x = [0, scale]
    plt.plot(x, x, '--', color='black', label='1:1')

    # 2. regression
    fit = np.polyfit(douban, imdb, 1)
    fit_fn = np.poly1d(fit)
    x = linspace(0, scale)
    plt.plot(x, fit_fn(x), '-', label='Regression')
    if type != 'rating':
        plt.fill_between(x, x - 20, x + 20, alpha=0.15)

    # 3. Plot scatter
    scatter_plot = ax.scatter(douban, imdb, alpha=0.3)

    plt.axis([0, scale, 0, scale])
    if type == 'rating':
        plt_configure(xlabel='Douban Rating', ylabel='IMDB Rating', title=title, legend={'loc': 'best'})
    else:
        plt_configure(xlabel='Douban Rank', ylabel='IMDB Rank', title=title, legend={'loc': 'best'})
    plt.gca().set_aspect('equal')
    return fig, fit_fn, scatter_plot
