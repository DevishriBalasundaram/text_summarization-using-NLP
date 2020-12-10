## Importing Libraries
import streamlit as st

import pandas as pd
import numpy as np
import nltk
import re
import heapq

from nltk.corpus import stopwords
stops = set(stopwords.words('english'))
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


st.sidebar.title("Text summarization")
st.sidebar.subheader("Check the below box!")
agree = st.sidebar.checkbox("Want to summarise your text?")
if agree:
    st.title("Let's do text extractive summarization!")

## Finding most oftentimes word recurrence
def word_recurrence(words):
    often_words = {}
    cleaned_words=word_tokenize(words)
    cleaned_words=[word for word in cleaned_words if word not in stops]
    for word in cleaned_words:
        if word not in often_words.keys():
            often_words[word] = 1
        else:
            often_words[word] += 1
        maximum_frequncy = max(often_words.values())
        for word in often_words.keys():
            often_words[word] = (often_words[word]/maximum_frequncy)
    return often_words

def clean_preprocessing(text):
    text = text.lower()  # LOWER THE CASE
    text = re.sub("[^a-z0-9.\- ]"," ",text) # keeping only aplha numerical  @#$
    text = re.sub(' +', ' ', text) # remove all extra long spaces
    text = re.sub(r'[[0-9]*]', ' ', text) # remove sqr brackets
    final_text = re.sub('[^a-zA-Z]', ' ', text ) # remove special char
    cleaned_words = word_recurrence(final_text)
    return cleaned_words

## Finding scores for all sentences
def sentence_score(input_text,sentences_list):
    scores = {}
    for sentence in sentences_list:
        often_words = clean_preprocessing(sentence)
        for word in often_words.keys():
            if word in often_words.keys():
                if sentence not in scores.keys():
                    scores[sentence] = often_words[word]
                else:
                    scores[sentence] += often_words[word]
    return scores

## Generating summary using heapq based on large scores
def summary_generator(input_text,summary_lines,sentences_list):
    summary = heapq.nlargest(summary_lines, sentence_score(input_text,sentences_list), key=sentence_score(input_text,sentences_list).get)
    summary = ' '.join(summary)
    summary = re.sub(' +', ' ', summary) # remove all extra long spaces
    summary = re.sub(r'[\n\r\t]', " ", summary) # remove line spacing
    return summary



# ----------------------------- Summariser Function ------------------------------- #
def text_summarization():
    text = """Machine learning (ML) is the study of computer algorithms that improve automatically through experience.[1] 
        It is seen as a subset of artificial intelligence. Machine learning algorithms build a model based on sample data, 
        known as "training data", in order to make predictions or decisions without being explicitly programmed to do so. 
        Machine learning algorithms are used in a wide variety of applications, such as email filtering and computer vision, 
        where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks.
        A subset of machine learning is closely related to computational statistics, 
        which focuses on making predictions using computers; but not all machine learning is statistical learning. 
        The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. 
        Data mining is a related field of study, focusing on exploratory data analysis through unsupervised learning.[4][5] 
        In its application across business problems, machine learning is also referred to as predictive analytics."""

    input_text = st.text_area("Enter large text or paragraph to summarize:", value=text)
    summary_lines = st.number_input("Enter the number of sentences to view in summary:", value=5)
    ## Spliting paragraphs into sentences
    sentences_list = sent_tokenize(input_text)
    
    if st.button("Generate Summary of the above text"):
        summary = summary_generator(input_text,summary_lines,sentences_list)
        st.subheader("Your {} lines of summary:".format(summary_lines))
        st.write(summary)

if __name__ == "__main__":
    # streamlit sidebar function
    if agree:
        text_summarization()
