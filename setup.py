from setuptools import setup

setup(
    name='ApiLeagueOfLegends',
    packages=['', 'league_of_legends_api', 'league_of_legends_api/Api', 'league_of_legends_api/Database',
              'league_of_legends_api/Tools'],
    package_dir={'': 'src'},
    version='0.04',
    license='MIT',
    description='Wrapper for the League of Legends Api',
    author='Lukas Mahr',
    author_email='LukasMahr@gmx.de',
    url='https://github.com/Lkgsr/League-of-Legends-Api',
    keywords=['API', 'Api', 'api', 'LeagueOfLegends', 'LeagueofLegends', 'league-of-legends', 'lol',
              'League-of-Legends', 'League-Of-Legends'],
    install_requires=[
        'requests',
        'SQLAlchemy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=False,
)
