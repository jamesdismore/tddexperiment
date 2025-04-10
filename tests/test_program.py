from lib.program import *

def test_make_snippet_exists():
    make_snippet('test')

def test_make_snippet_returns_something():
    assert len(make_snippet('There are five words here')) != 0

def test_return_one_word():
    assert make_snippet('One') == 'One'

def test_return_five_words():
    assert make_snippet('There are five words here') == 'There are five words here'



