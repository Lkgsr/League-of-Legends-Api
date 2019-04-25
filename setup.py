from distutils.core import setup

setup(
    name='Api-League-of-Legends',
    packages=['src'],
    version='0.01',
    license='MIT',
    description='Wrapper for the League of Legends Api',
    author='Lukas Mahr',
    author_email='LukasMahr@gmx.de',
    url='https://github.com/Lkgsr/League-of-Legends-Api',
    download_url='https://github.com/Lkgsr/League-of-Legends-Api/archive/0.01.tar.gz',
    keywords=['API', 'Api', 'api', 'LeagueOfLegends', 'LeagueofLegends', 'league-of-legends', 'lol',
              'League-of-Legends', 'League-Of-Legends'],
    install_requires=[
        'requests',
        'SQLAlchemy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
