from .shared_imports import *
from plot_print_helper import plt_configure


def plot_movie_scatter_comparison(df, title=''):
    fig, ax = plt.subplots()
    # 1. plot scatter
    scatter_plot = ax.scatter(df.db_rating, df.imdb_rating, alpha=0.3)
    x = [0, 10]
    plt.plot(x, x, '--', color='black', label='1:1')

    # 2. regression
    fit = np.polyfit(df.db_rating, df.imdb_rating, 1)
    fit_fn = np.poly1d(fit)
    x = linspace(0, 10)
    plt.plot(x, fit_fn(x), '-', label='Regression')

    plt.axis([0, 10, 0, 10])
    plt_configure(xlabel='Douban Rating', ylabel='IMDB Rating', title=title, legend={'loc': 'best'})
    plt.gca().set_aspect('equal')
    return fig, fit_fn, scatter_plot
