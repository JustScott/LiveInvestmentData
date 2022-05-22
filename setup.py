from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

VERSION = '0.0.1'
DESCRIPTION = 'Simple to use stock, commodity, forex, and cryptocurrency market webscraper, utilizing the beautiful soup and requests libraries.'

# Setting up
setup(
    name="liveinvestmentdata",
    version=VERSION,
    license="MIT",
    author="JustScott",
    author_email="<justscottmail@protonmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url = "https://github.com/JustScott/liveinvestmentdata",
    project_urls={
        "Bug Reports":"https://github.com/JustScott/liveinvestmentdata/issues",
    },
    package_dir={"":"src"},
    packages=["liveinvestmentdata"],
    install_requires=['beautifulsoup4==4.11.1','requests==2.27.1'],
    keywords=['python','finance'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Topic :: Office/Business :: Financial :: Investment',
    ]
)
