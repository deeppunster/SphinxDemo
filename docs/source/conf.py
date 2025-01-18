# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
from pathlib import Path
import sys

# identify path to project directory and to source and testing directories
project_path = Path(__file__).parents[2].resolve()
src_path: Path = project_path / "src"
test_path = project_path / "tests"

# add source and testing directories to path in reverse order
sys.path.insert(0, test_path.as_posix())
sys.path.insert(0, src_path.as_posix())

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx Documentation Tool'
copyright = '%Y, Travis Risner'
author = 'Travis Risner'
version = '0.1.0'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


templates_path = ['_templates']
exclude_patterns = []

autodoc_default_options = {
    'members': None,
    'member-order': 'bysource',
    'special-members': '__init__',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'green',
    'flyout_display': 'hidden',
    'version_selector': True,
    'language_selector': True,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
} 

html_static_path = ['_static']
