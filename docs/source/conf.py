# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'advent-calendar-2025'
copyright = '2025, Dialid Santiago'
author = 'Dialid Santiago'
release = '0.1'

html_logo = 'logo.jpg'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
              'myst_parser',
              'sphinx.ext.mathjax',
            #   'sphinx_gallery.gen_gallery',
              ]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']


sphinx_gallery_conf = {
    'within_subsection_order': "FileNameSortKey",
    'examples_dirs': ["../../examples", "../../bonus"] ,  # path to your example scripts
    'gallery_dirs': ['auto_examples', 'auto_bonus'],  # path to where to save gallery generated output
}


myst_enable_extensions = [
    "amsmath",  # for environments like \begin{align}
    "dollarmath"  # for $ and $$ math syntax
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/quantgirluk/advent-calendar-2025",
    "use_repository_button": True,
    "use_source_button": True,
}

html_title = "Advent Calendar 2025"

html_static_path = ['_static']

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"