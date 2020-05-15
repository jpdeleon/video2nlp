# video2nlp
[![Build Status](https://travis-ci.com/jpdeleon/tql.svg?branch=master)](https://travis-ci.com/jpdeleon/tql)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

NLP analysis of closed caption (cc) from youtube videos

## installation
```bash
git clone https://github.com/jpdeleon/video2nlp.git
pip install -e .
python -m spacy download en
```
## example
```bash
python video2nlp.py
```
![img](./wordcloud.png)

## Run at Google colab
<a href="https://colab.research.google.com/github/jpdeleon/tql/blob/master/notebooks/examples-QL.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
