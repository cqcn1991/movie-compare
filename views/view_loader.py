from IPython.display import display, HTML, Javascript

def load_assets():
    lib_files = """
        <link rel="stylesheet" type="text/css" href='./views/application.css' media="screen" />
        """
    return HTML(lib_files)