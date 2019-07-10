from setuptools import setup
setup(
    name = 'griddy',
    version = '0.1.0',
    packages = ['griddy'],
    entry_points = {
        'console_scripts': [
            'griddy = griddy.__main__:main'
        ]
    })