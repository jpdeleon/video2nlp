#!/usr/bin/env python
import sys
from matplotlib.figure import Figure

sys.path.append("..")
from video2nlp import Base

bc = Base(youtube_video_id="sBYdIPZDYsU", verbose=True)


def test_init():
    # measure sentiment
    senti = bc.get_sentiment()
    assert isinstance(senti.polarity, float)
    assert isinstance(senti.subjectivity, float)


def test_plot():
    # visualize wordcloud
    fig = bc.plot_wordcloud()
    assert isinstance(fig, Figure)
