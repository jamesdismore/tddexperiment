from lib.program import *

def test_make_snippet_exists():
    make_snippet('test')

def test_make_snippet_returns_something():
    assert len(make_snippet('test')) != 0