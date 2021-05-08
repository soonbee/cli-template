import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

requirements = []
with open('requirements.txt') as file_requirements:
    requirements = file_requirements.read().splitlines()

about = {}
with open(os.path.join(here, 'cli', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    install_requires=requirements,
    packages=find_packages(exclude=['test']),
    python_requires='>=3.5',
    include_package_data=True,
    package_data={},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'mycli = cli.main:entry_point'
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)

