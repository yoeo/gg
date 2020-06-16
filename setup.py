#!/usr/bin/env python3

from pathlib import Path

from setuptools import setup, find_packages


def list_resources(basedir, resource_dirs):
    return [
        (str(path.parent), [str(path)])
        for dirname in resource_dirs
        for path in Path(basedir, dirname).glob('**/*') if path.is_file()
    ]


setup(
    name="gg",
    author="yoeo",
    version="0.2",
    url="https://github.com/yoeo/gg",
    license="MIT",
    description="Programming language Gessing Game",
    install_requires=Path('requirements.txt').read_text().splitlines(),
    packages=find_packages(),
    data_files=list_resources('gg', ('static', 'templates')),
    zip_safe=False,
    scripts=['bin/gg-gunicorn'],
    entry_points={
        'console_scripts': ['gg = gg.__main__:main']
    },
)
