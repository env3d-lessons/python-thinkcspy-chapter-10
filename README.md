# News Sentiment Analyzer

## Challenge 10: Lists

### Learning Objectives

- Practice using lists and list indexing
- Practice using loops
- Practice writing functions

## Background

In recent years, AI advances have allowed computers to perform functions that used to be the exclusive domain of human beings. One of these fields is for computers to understand natural languages.

"Understanding" may be a bit of an overstatement. As you will see, the AI system is simply providing us a function where the input is a sentence, and it returns the sentence's sentiment as a number.

Your job is to use this AI to analyze live newsfeeds.

## Provided Functions

You are provided with the following two functions:

- **get_sentiment(sentence)**  
  Given a sentence (string), it returns a number indicating the sentiment (or emotion) of the sentence.  
  Example:
  ```
  > get_sentiment('this is going to be a great day!')
  0.6588
  > get_sentiment('i hate rainy mornings!')
  -0.6476
  ```
  The number returned is a float in the range of [-1.0, 1.0]. The higher the number, the more positive the sentence, and vice versa.

- **get_news_excerpt()**  
  Retrieves a list of current news excerpts.

## Your Tasks

You will use these functions to complete the exercises. Most exercises require you to loop over a list of items using a `for` loop and process each item in the list.


## How to Use

1. **Run the Application**  
   To launch the UI, run:
   ```
   python main.py
   ```
   And visit the app using the "PORTS" tab in the Codespaces interface.

3. **Interact with the UI**  
   - **Sentiment Scores:** Enter sentences (one per line) to see their sentiment scores.
   - **Positive Only:** See only the positive sentences from your input.
   - **Negative Only:** See only the negative sentences from your input.
   - **Max/Min Score:** Find the most positive and most negative sentiment scores from your input.
   - **Live News:** See the most positive and most negative current news headlines.


## Notes

- The sentiment analysis uses NLTK's VADER SentimentIntensityAnalyzer.
- News headlines are fetched live from [time.com](https://time.com).
- All exercises are implemented in `main.py`.
- You can run the included tests with:
  ```
  pytest
  ```

## Submit

Once you have completed the exercises, submit your code as follows:

```
git add -A
git commit -m 'submit'
git push
```

