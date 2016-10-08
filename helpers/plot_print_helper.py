from .shared_imports import *


def plt_configure(ax=None, xlabel=None, ylabel=None, title='', legend=False, tight=False, figsize=False, no_axis=False):
    if ax == None :
        ax=plt.gca()
        plt.suptitle(title)
    else:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if legend:
        if isinstance(legend, dict):
            ax.legend(**legend)
        else:
            ax.legend()
    if tight:
        if tight == 'xtight' or tight == 'x':
            ax.autoscale(enable=True, axis='x', tight=True)
        elif tight == 'ytight':
            ax.autoscale(enable=True, axis='y', tight=True)
        else:
            ax.axis('tight')
    if figsize:
        plt.gcf().set_size_inches(figsize)
    if no_axis:
        plt.gca().axis('off')
        legend = ax.legend()
        if legend:
            legend.remove()


