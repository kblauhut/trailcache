from setuptools import setup

setup(
    name='trailcache',
    version='1.0',
    description='Downloads geocaches along a GPX route or track.',
    author='Kolja Blauhut',
    packages=['trailcache'],
    entry_points={
        'console_scripts': ['run=trailcache.core:main'],
    },
    install_requires=['gpxpy', 'colorama', 'requests', 'tqdm']
)
