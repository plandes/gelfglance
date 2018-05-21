from setuptools import setup, find_packages

setup(
    name = "zensols.gelfglance",
    packages = ['zensols', 'zensols.gelfglance'],
    version = '0.1',
    description = 'Forward glance statistics as gelf logs.',
    author = 'Paul Landes',
    author_email = 'landes@mailc.net',
    url = 'https://github.com/plandes/gelfglance',
    download_url = 'https://github.com/plandes/gelfglance/releases/download/v0.0.1/zensols.gelfglance-0.1-py3-none-any.whl',
    keywords = ['tooling'],
    classifiers = [],
    entry_points={
        'console_scripts': [
            'gelfglance=zensols.gelfglance.cli:main'
        ]
    }
)
