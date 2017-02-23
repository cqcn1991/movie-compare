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


class PointClickableHTMLTooltip2(mpld3.plugins.PluginBase):
        JAVASCRIPT = """
        mpld3.register_plugin("clickablehtmltooltip", PointClickableHTMLTooltip);
        PointClickableHTMLTooltip.prototype = Object.create(mpld3.Plugin.prototype);
        PointClickableHTMLTooltip.prototype.constructor = PointClickableHTMLTooltip;
        PointClickableHTMLTooltip.prototype.requiredProps = ["id"];
        PointClickableHTMLTooltip.prototype.defaultProps = {labels:null,
                                                     targets:null,
                                                     hoffset:0,
                                                     voffset:10};
        function PointClickableHTMLTooltip(fig, props){
            mpld3.Plugin.call(this, fig, props);
        };
        PointClickableHTMLTooltip.prototype.draw = function(){
           var obj = mpld3.get_element(this.props.id);
           var labels = this.props.labels;
           var targets = this.props.targets;
           var tooltip = d3.select("body").append("div")
                        .attr("class", "mpld3-tooltip")
                        .style("position", "absolute")
                        .style("z-index", "10")
                        .style("visibility", "hidden");
           obj.elements()
               .on("mouseover", function(d, i){
                                  tooltip.html(labels[i])
                                         .style("visibility", "visible");})
                .on("mousedown", function(d, i){
                      window.open(targets[i], '_blank');
                                   })
                .on("mousemove", function(d, i){
                      tooltip
                        .style("top", d3.event.pageY + this.props.voffset + "px")
                        .style("left",d3.event.pageX + this.props.hoffset + "px");
                     }.bind(this))
                .on("mousemove", function(d, i){
                      tooltip
                        .style("top", d3.event.pageY + this.props.voffset + "px")
                        .style("left",d3.event.pageX + this.props.hoffset + "px");
                     }.bind(this))
                .on("mouseout",  function(d, i){
                               tooltip.style("visibility", "hidden");});
        };
        """

        def __init__(self, points, labels=None, targets=None,
                     hoffset=2, voffset=-6, css=None):
            self.points = points
            self.labels = labels
            self.targets = targets
            self.voffset = voffset
            self.hoffset = hoffset
            self.css_ = css or ""

            if isinstance(points, mpl.lines.Line2D):
                suffix = "pts"
            else:
                suffix = None
            self.dict_ = {"type": "clickablehtmltooltip",
                          "id": mpld3.utils.get_id(points, suffix),
                          "labels": labels,
                          "targets": targets,
                          "hoffset": hoffset,
                          "voffset": voffset}