from setuptools import find_packages, setup

setup(
    name='metawiki',
    version='0.1.5',
    description='A simple map for urls of definitions in notable sources.',
    url='https://github.com/wefindx/metawiki',
    author='Mindey',
    author_email='mindey@qq.com',
    license='AGPL',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires=['parse'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    zip_safe=False
)
