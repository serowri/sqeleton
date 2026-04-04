import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]


project = 'sqeleton'
copyright = '2026, serowri'
author = 'serowri'
release = '0.1.0'

templates_path = ['_templates']
exclude_patterns = []
html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'



