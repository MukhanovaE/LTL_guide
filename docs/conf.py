# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LTLguide'
copyright = '2025, Ekaterina Mukhanova'
author = 'Ekaterina Mukhanova'
release = '01.08.2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.mathjax",          # для формул LaTeX
    "sphinx.ext.autosectionlabel", # для ссылок по заголовкам
    "myst_parser",                 # для Markdown (опционально)
]

math_number_all = True
autosectionlabel_prefix_document = True

html_theme = "sphinx_rtd_theme"
language = "ru"

templates_path = ["_templates"]
html_static_path = ["_static"]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


