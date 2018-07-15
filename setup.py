from setuptools import find_packages, setup

setup(
    name='metawiki',
    version='0.0.4',
    description='A simple map for urls of definitions in notable sources.',
    url='https://github.com/mindey/metawiki',
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
