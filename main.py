from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from urllib.request import urlopen, Request
import json

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


##### You will use the following functions to complete the exercises #######

"""
The get_sentiment() function returns a number between -1 and 1 for a given string (sentence).  
The higher the number, the more positive the sentiment is.  
"""


def get_sentiment(sentence):     
    return sid.polarity_scores(sentence)['compound']


"""
The get_news_excerpt function return a list of current world news titles from time.com
"""

def get_news_excerpt(site = 'time.com'):
    url = f'https://{site}/wp-json/wp/v2/posts/?per_page=10&context=embed'
    my_socket = urlopen(Request(url, headers={'User-Agent':'abcde'}))
    dta = my_socket.read()
    site_data = json.loads(dta)    
    titles = [x['excerpt']['rendered'] for x in site_data]
    return titles


####### Start of the exercises #########

"""
Exercise 1:

Given a list of sentences as input, return a list of corresponding sentiments

Here is how I would use the function:
> get_sentiments(['good day!','terrible day'])
[0.4926, -0.4767]


"""
def get_sentiments(list_of_sentences):
    sentiment_list = []

    # use the accumulator patern here as per Chatper 10.22    
    
    return sentiment_list


"""
Exercise 2:

Given a list of sentences as input, return the maximum (most positive) score

Here is how I would use the function:

> get_max_score(['good day!','terrible day'])
0.4926

"""

def get_max_score(list_of_sentences):
    # first we get a list of scores from previous exercise
    scores = get_sentiments(list_of_sentences)

    # now we find the max score
    max_score = 0

    # use the acculmulator as per 10.18.1
    
    return max_score

"""
Exercise 3:

Given a list of sentences as input, return the minimum (most negative) score

Here is how I would use the function:

>get_min_score(['good day!','terrible day'])
-0.4767

"""
def get_min_score(list_of_sentences):
    scores = get_sentiments(list_of_sentences)
    min_score = 1

    # same as previous exercise, but find min instead of max

    return min_score

"""
Exercise 4:

Given is list of sentences, return a list of only positive items.

i.e.
> positive_only(['good day!','terrible day','I love today'])
['good day!', 'I love today']

"""
def positive_only(list_of_sentences):
    positive_items = []
    
    # use the acculmulator pattern.  
    # for every sentence, we first find out the numerical
    # sentiment value.  If positive, we add it to 
    # the return list
    
    return positive_items

"""
Exercise 5:

Given is list of sentences, return a list of only negative items.

i.e.
> negative_only(['good day!','terrible day','I love today','I feel sad'])
['terrible day', 'I feel sad']

"""
def negative_only(list_of_sentences):
    negative_items = []

    # same as previous but only accumulate negative items
    
    return negative_items


"""
Exercise 6:

Return the MOST POSITIVE news right now (using the get_news_excerpt() function)

> get_most_positive_news()
'Armenia’s Central Bank improves GDP growth forecast from 1.6 to 13% due to mass influx of ‘talented and well-educated’ Russians into the country'

"""
def get_most_positive_news():
    news_items = get_news_excerpt()    
    max_score = get_max_score(news_items)

    # search each news items, and
    # return the item that matches the max_score

    return ''

"""
Exercise 7:

Return the MOST NEGATIVE news right now (using the get_news_excerpt() function)

> get_most_negative_news()
'Ukraine Sends Stark Warning to Belarus Against Joining War'

"""
def get_most_negative_news():
    news_items = get_news_excerpt()
    min_score = get_min_score(news_items)

    # same as previous but return the item with most
    # negative score

    return ''


### DO NOT MODIFY THE CODE BELOW THIS LINE ###

if __name__ == "__main__":

    import gradio as gr
    
    # --- Gradio UI Section ---
    def ui_get_sentiments(sentences):
        # Split input by newlines, strip whitespace, ignore empty lines
        lines = [line.strip() for line in sentences.split('\n') if line.strip()]
        return get_sentiments(lines)

    def ui_positive_only(sentences):
        lines = [line.strip() for line in sentences.split('\n') if line.strip()]
        return '\n'.join(positive_only(lines))

    def ui_negative_only(sentences):
        lines = [line.strip() for line in sentences.split('\n') if line.strip()]
        return '\n'.join(negative_only(lines))

    def ui_get_max_score(sentences):
        lines = [line.strip() for line in sentences.split('\n') if line.strip()]
        return get_max_score(lines)

    def ui_get_min_score(sentences):
        lines = [line.strip() for line in sentences.split('\n') if line.strip()]
        return get_min_score(lines)

    def ui_get_most_positive_news():
        return get_most_positive_news()

    def ui_get_most_negative_news():
        return get_most_negative_news()

    with gr.Blocks() as demo:
        gr.Markdown("# News Sentiment Analyzer")

        with gr.Tab("Sentiment Scores"):
            inp = gr.Textbox(label="Enter sentences (one per line) - use SHIFT+ENTER for new line")
            out = gr.JSON(label="Sentiment Scores")
            inp.submit(ui_get_sentiments, inp, out)
            gr.Button("Analyze").click(ui_get_sentiments, inp, out)

        with gr.Tab("Positive Only"):
            inp2 = gr.Textbox(label="Enter sentences (one per line) - use SHIFT+ENTER for new line")
            out2 = gr.Textbox(label="Positive Sentences")
            inp2.submit(ui_positive_only, inp2, out2)
            gr.Button("Show Positive").click(ui_positive_only, inp2, out2)

        with gr.Tab("Negative Only"):
            inp3 = gr.Textbox(label="Enter sentences (one per line) - use SHIFT+ENTER for new line")
            out3 = gr.Textbox(label="Negative Sentences")
            inp3.submit(ui_negative_only, inp3, out3)
            gr.Button("Show Negative").click(ui_negative_only, inp3, out3)

        with gr.Tab("Max/Min Score"):
            inp4 = gr.Textbox(label="Enter sentences (one per line) - use SHIFT+ENTER for new line")
            out4 = gr.Number(label="Max Score")
            out5 = gr.Number(label="Min Score")
            inp4.submit(ui_get_max_score, inp4, out4)
            inp4.submit(ui_get_min_score, inp4, out5)
            gr.Button("Get Max Score").click(ui_get_max_score, inp4, out4)
            gr.Button("Get Min Score").click(ui_get_min_score, inp4, out5)

        with gr.Tab("Live News"):
            out6 = gr.Textbox(label="Most Positive News")
            out7 = gr.Textbox(label="Most Negative News")
            gr.Button("Get Most Positive News").click(ui_get_most_positive_news, None, out6)
            gr.Button("Get Most Negative News").click(ui_get_most_negative_news, None, out7)

    demo.launch()

