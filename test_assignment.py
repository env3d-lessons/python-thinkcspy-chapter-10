import pytest
from main import *
from unittest.mock import patch

def test_sentiment_return_list():
    l = get_sentiments(['very good!','excellent!','perfect!'])
    assert isinstance(l, list)

def test_sentiment_values():
    l = get_sentiments(['very good!','excellent!','perfect!'])
    for i in l:
        assert 0.5 < i < 0.65

def test_max_score():
    score = get_max_score(['very good!','excellent!','perfect!'])
    assert 0.6 < score < 0.62

def test_min_score():
    score = get_min_score(['very good!','excellent!','perfect!'])
    assert 0.53 < score < 0.55

def test_positive_only():
    l = positive_only(['very good!','excellent!','perfect!'])
    assert len(l) == 3
    l = positive_only(['very bad!','worst!','terrible!'])
    assert len(l) == 0

def test_negative_only():
    l = negative_only(['very good!','excellent!','perfect!'])
    assert len(l) == 0
    l = negative_only(['very bad!','worst!','terrible!'])
    assert len(l) > 0

def test_most_positive():
    with patch('main.get_news_excerpt', return_value=['very good!','excellent!','very bad!','worst!','terrible!']) as mock_reddit:
        n = get_most_positive_news()
        assert mock_reddit.called
        assert n == 'excellent!'

def test_most_negative():
    with patch('main.get_news_excerpt', return_value=['very good!','excellent!','very bad!','worst!','terrible!']) as mock_reddit:
        n = get_most_negative_news()
        assert mock_reddit.called
        assert n == 'worst!'
