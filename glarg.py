#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""Python pseudo-word generator.
"""

# Standard library
from __future__ import absolute_import, division, print_function
import argparse
import math
import random
import string


__all__ = ("entropy_per_word", "generate_word", "generate_words")
VOWELS = set("aeiou")
FILL_VOWELS = list(VOWELS | set("ee oo ou ui".split()))
PRE_CONSONANTS = list(set(string.ascii_lowercase) -
                      # remove vowels
                      VOWELS -
                      # remove those easily confused with others
                      set("cqx") |
                      # add some crunchy clusters
                      set("bl br ch dr fl fr gl gr kl kr pl pr sh sk sl sm sn"
                          " sp st str sw tr".split()))
POST_CONSONANTS = list(set(string.ascii_lowercase) -
                       # remove vowels
                       VOWELS -
                       # remove the confusables
                       set("cjqsxy") |
                       # add some crunchy clusters
                       set("ch ct ft ld lf lk ll lm lp lt mp nd ng nk nt pt rm"
                           " sh sk sp ss st".split()))


def generate_phrase(wordcount):
    """Returns a list of "wordcount" pseudo-words.
    """
    number = "{0:04d}".format(random.randint(0, 9999))
    words = generate_words(wordcount)
    words.insert(1, number)
    phrase = ".".join(words)
    phrase = phrase.capitalize()
    return phrase


def generate_words(wordcount):
    """Returns a list of "wordcount" pseudo-words.
    """
    return [generate_word() for _ in list(range(wordcount))]


def generate_word():
    """Returns a random consonant-vowel-consonant pseudo-word.
    """
    return "".join(random.choice(s) for s in (PRE_CONSONANTS,
                                              FILL_VOWELS,
                                              POST_CONSONANTS))


def entropy_per_word(wordcount, count):
    """Caclulates entropy per pseudo-word.
    """
    entropy_initial = math.log(len(PRE_CONSONANTS), 2)
    entropy_vowels = math.log(len(FILL_VOWELS), 2)
    entropy_final = math.log(len(POST_CONSONANTS), 2)
    entropy_per_word = entropy_initial + entropy_vowels + entropy_final
    entropy_number = math.log(10, 2) * 4
    entropy_total = entropy_per_word * wordcount + entropy_number
    if count > 1:
        plural = "s"
    else:
        plural = ""
    return("The phrase{0} below contains a total of {1:.2f} bits of entropy"
           "\n({2:.2f} bits per word and {3:.2f} bits for the number):\n"
           .format(plural, entropy_total, entropy_per_word, entropy_number))


def parser_setup():
    """Instantiate and return an ArgumentParser instance.
    """
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-c", "--count", default=1, type=int,
                    help="Number of phrases (default: %(default)s).")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="Display entropy for requested word count")
    ap.add_argument("wordcount", nargs="?", default=3, type=int,
                    help="Number of words in the phrase (default:"
                    " %(default)s).")
    args = ap.parse_args()

    return args


def main():
    args = parser_setup()
    if args.verbose:
        print(entropy_per_word(args.wordcount, args.count))
    for _ in list(range(0, args.count)):
        phrase = generate_phrase(args.wordcount)
        print(phrase)


if __name__ == "__main__":
    main()
