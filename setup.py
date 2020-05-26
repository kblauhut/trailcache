from setuptools import setup

setup(
    name='trailcache',
    version='1.0',
    description='Downloads geocaches along a GPX trail.',
    author='Kolja Blauhut',
    packages=['trailcache'],  # same as name
    entry_points={
        'console_scripts': ['run=trailcache.commandline:main'],
    },
    # external packages as dependencies
    install_requires=['gpxpy', 'colorama'],
)
