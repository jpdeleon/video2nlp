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
Fetch the cc from this [youtube video](https://www.youtube.com/watch?v=LnC5kiqiKlw) then estimate sentiment/polarity and create a wordcloud.
```bash
./video2nlp.py -e -v

Raw word count: 8488
stopwords removed: 5107
Sentiment:  Sentiment(polarity=0.21995583825509454, subjectivity=0.5443397329642683)
```
![img](./wordcloud.png)

## usage
How about [this speech](https://www.youtube.com/watch?v=sBYdIPZDYsU) by Trump?
```
./video2nlp.py -id sBYdIPZDYsU -v

Raw word count: 8488
stopwords removed: 5107
Sentiment:  Sentiment(polarity=0.21995583825509454, subjectivity=0.5443397329642683)

```

## Run at Google colab
<a href="https://colab.research.google.com/github/jpdeleon/video2nlp/blob/master/example.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
