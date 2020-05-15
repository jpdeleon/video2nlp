#!/usr/bin/env python
from matplotlib import rcParams

rcParams["figure.dpi"] = 150
rcParams["savefig.dpi"] = 150

import matplotlib.pyplot as pl
import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
import spacy
from textblob import TextBlob
from wordcloud import WordCloud

nlp_spacy = spacy.load("en")
STOPWORDS = nlp_spacy.Defaults.stop_words


class Base:
    def __init__(self, youtube_video_id, languages=["en"], verbose=True):
        self.video_id = youtube_video_id
        self.languages = languages
        self.verbose = True
        self.caption_json = None
        self.caption_df = None
        self.caption_raw = self.get_caption()
        self.caption_clean = self.get_clean_caption(stopwords=None)
        self.wordcloud = None

    def get_caption(self):
        """"""
        caption_json = YouTubeTranscriptApi.get_transcript(
            self.video_id, languages=self.languages
        )
        self.caption_json = self.caption_json
        self.caption_df = pd.DataFrame(caption_json)
        raw_text = " ".join([phrase for phrase in self.caption_df["text"]])
        if self.verbose:
            words_list = raw_text.split(" ")
            print(f"Raw word count: {len(words_list)}")
        return raw_text

    def get_clean_caption(self, stopwords=None):
        """ """
        if stopwords is not None:
            if isinstance(stopwords, list):
                for word in stopwords:
                    STOPWORDS.add(word)
            else:
                STOPWORDS.add(word)

        raw_text_nlp = nlp_spacy(self.caption_raw)
        words_list_without_stop_words = [
            words.text for words in raw_text_nlp if not words.is_stop
        ]

        if self.verbose:
            words_list = self.caption_raw.split(" ")
            print(
                f"stopwords removed: {len(words_list) - len(words_list_without_stop_words)}"
            )

        text_cleaned = " ".join(words_list_without_stop_words)
        return text_cleaned

    def get_sentiment(self, text=None):
        if text is None:
            textblob = TextBlob(self.caption_clean)
        else:
            textblob = TextBlob(text)
        return textblob.sentiment

    def get_sencences(self, min_word_count=1):
        nlp_spacy.add_pipe(nlp_spacy.create_pipe("sentencizer"))
        doc = nlp_spacy(self.caption_raw)
        sentences = [sent.string.strip() for sent in doc.sents]

        if min_word_count > 1:
            sentences = [
                sentence
                for sentence in sentences
                if len(sentence.split()) > min_word_count
            ]
        return sentences

    def plot_wordcloud(self, stopwords=None, ax=None):
        if ax is None:
            fig, ax = pl.subplots(
                1, 1, figsize=(8, 4), constrained_layout=True
            )

        wc = WordCloud(
            background_color="white",
            max_words=200,
            width=600,
            height=300,
            stopwords=stopwords,
            repeat=False,
        )
        wc.generate(self.caption_clean)
        self.wordcloud = wc

        ax.imshow(wc, interpolation="bilinear")
        pl.axis("off")
        return fig

    def __repr__(self):
        return f"Base(youtube_video_id={self.video_id})"


if __name__ == "__main__":
    # video_id = "JznCB4yplJw"
    video_id = "LnC5kiqiKlw"

    # base class
    bc = Base(youtube_video_id=video_id)
    #
    senti = bc.get_sentiment()
    print("Sentiment: ", senti)

    # visualization
    more_stopwords = ["oh", "like", "thing", "come", "yeah", "ba", "ko"]
    fig = bc.plot_wordcloud(stopwords=more_stopwords)
    pl.show()
