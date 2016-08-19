# vim: set fileencoding=utf-8 :

"""Unit Tests
"""

# Standard Library
from __future__ import absolute_import, division, print_function
import re

# Local/library specific
import glarg


RE_ALL_LOWERCASE = re.compile(r"^[a-z]+$")
RE_CONTAINS_LOWERCASE = re.compile(r"[a-z]")
RE_CONTAINS_NUMBERS = re.compile(r"[0-9]")
RE_CONTAINS_DIVS = re.compile(r"[.]")
RE_CONTAINS_UPPERCASE = re.compile(r"[A-Z]")


def test_generate_word():
    # GIVEN
    # WHEN a word is generated
    word = glarg.generate_word()
    # THEN word should be a string and
    #      word should be at least 3 characters in length and
    #      word should contain only lowercase characters
    assert isinstance(word, str)
    assert len(word) >= 3
    assert RE_ALL_LOWERCASE.search(word)


def test_generate_words():
    # GIVEN a word count of 4
    wordcount = 4
    # WHEN a list of words is generated
    words = glarg.generate_words(wordcount)
    # THEN list should be a list and
    #      list should contain 4 members
    assert isinstance(words, list)
    assert len(words) == 4


def test_generate_phrase():
    # GIVEN a word count of 4
    wordcount = 2
    # WHEN a password phrase is generated
    phrase = glarg.generate_phrase(wordcount)
    # THEN phrase should be a string and
    #      phrase should be at least 12 characters in length and
    #      phrase should contain dividers and
    #      phrase should contain lowercase alphas and
    #      phrase should contain numbers and
    #      phrase should contain uppercase alphas
    assert isinstance(phrase, str)
    assert len(phrase) >= 12
    assert RE_CONTAINS_DIVS.search(phrase)
    assert RE_CONTAINS_LOWERCASE.search(phrase)
    assert RE_CONTAINS_NUMBERS.search(phrase)
    assert RE_CONTAINS_UPPERCASE.search(phrase)
