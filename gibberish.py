#!/usr/bin/env python
"""Python pseudo-word generator."""
import argparse
import math
import random
import string

__all__ = ('generate_word', 'generate_words')

initial_consonants = list(set(string.ascii_lowercase) - set('aeiou') -
                          # remove those easily confused with others
                          set('qxc') |
                          # add some crunchy clusters
                          set(['bl', 'br', 'cl', 'cr', 'dr', 'fl',
                               'fr', 'gl', 'gr', 'pl', 'pr', 'sk',
                               'sl', 'sm', 'sn', 'sp', 'st', 'str',
                               'sw', 'tr', 'ch', 'sh'])
                          )

final_consonants = list(set(string.ascii_lowercase) - set('aeiou') -
                        # remove the confusables
                        set('qxcsj') |
                        # add some crunchy clusters
                        set(['ct', 'ft', 'mp', 'nd', 'ng', 'nk', 'nt',
                             'pt', 'sk', 'sp', 'ss', 'st', 'ch', 'sh'])
                        )

vowels = 'aeiou'


def generate_word():
    """Returns a random consonant-vowel-consonant pseudo-word."""
    return ''.join(random.choice(s) for s in (initial_consonants,
                                              vowels,
                                              final_consonants))


def generate_words(wordcount):
    """Returns a list of ``wordcount`` pseudo-words."""
    return [generate_word() for _ in xrange(wordcount)]


def entropy_per_word(wordcount):
    """Caclulates entropy per pseudo-word."""
    entropy_initial = math.log(len(initial_consonants), 2)
    entropy_vowels = math.log(len(vowels), 2)
    entropy_final = math.log(len(final_consonants), 2)
    entropy_per_word = entropy_initial + entropy_vowels + entropy_final
    entropy_total = entropy_per_word * wordcount
    return('Pseduo words contain a total of %.2f bits of entropy (%.2f bits'
           ' each):' % (entropy_total, entropy_per_word))


def parser_setup():
    """Instantiate and return an ArgumentParser instance."""
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('-v', '--verbose', action='store_true',
                    help='Display entropy for requested word count')
    ap.add_argument('wordcount', nargs='?', default=3, type=int,
                    help='Number of words to generate (default: %(default)s).')
    args = ap.parse_args()

    return args


def console_main():
    args = parser_setup()
    if args.verbose:
        print(entropy_per_word(args.wordcount))
        print
    print(' '.join(generate_words(args.wordcount)))


if __name__ == '__main__':
    console_main()
