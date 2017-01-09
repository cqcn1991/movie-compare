from IPython.display import display, HTML, Javascript
import sass
import mpld3


def load_css(raw=False):
    with open('./assets/application.css.scss', 'r') as myfile:
        sass_raw = myfile.read().replace('\n', '')
        css = sass.compile(string=sass_raw)
    if not raw:
        css = "<style media='screen' type='text/css'>" + css + '</style>'
    return css


def movie_list(df):
    movies = df.to_dict(orient='records')
    if len(movies) >= 12:
        movies = movies[:12]
    from jinja2 import Template, Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader('./views'))
    movie_template = env.get_template('movie.jinjia')
    movie_list_template = env.get_template('movie_list.jinjia')
    movie_list_content = movie_list_template.render(movies=movies, movie_template=movie_template)
    css = load_css()
    return HTML(css+ movie_list_content)


def turn_scatter_into_interactive(fig, scatter_plot, df, file_name, figsize=False):
    from jinja2 import Template, Environment, FileSystemLoader
    from mpld3 import plugins
    # file_path = './assets/interactive_plots/'+file_name
    file_path = './'+file_name
    env = Environment(loader=FileSystemLoader('./views'))
    movie_template = env.get_template('movie.jinjia')
    movies = df.to_dict(orient='records')
    movie_cards = [movie_template.render(movie=movie, show_ratings_num=True) for movie in movies]
    if figsize:
        fig.set_size_inches(figsize)
    else:
        fig.set_size_inches(10, 10)
    plugins.connect(fig, plugins.PointHTMLTooltip(scatter_plot, movie_cards, css=load_css(raw=True)))
    mpld3.save_html(fig, file_path)
    button = '''<a class='btn btn-default' style="text-decoration: none;;"
    href="{0}" target='_blank'>
    Interactive Scatter Plot</a>
    '''.format(file_path)
    return HTML(button)


# def movie_index():
#     movie_index_template = env.get_template('movie_index.jinjia')
#     output_from_parsed_template = movie_index_template.render(movie_list_content=movie_list_content, css=css)
#     with open("movie_index.html", "wb") as fh:
#         fh.write(output_from_parsed_template)
