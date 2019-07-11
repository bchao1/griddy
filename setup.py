from setuptools import setup
setup(
    name = 'griddy',
    author = "Mckinsey666",
    description = "Generate CSS grid-layouts FAST.",
    version = '0.3.0',
    packages = ['griddy'],
    url = "https://github.com/Mckinsey666/griddy",
    keywords = "html css javascript grid-layouts flexbox",
    entry_points = {
        'console_scripts': [
            'griddy = griddy.__main__:main'
        ]
    })