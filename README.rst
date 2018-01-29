=========================================
glarg: a pseudo-word passphrase generator
=========================================


History
=======

The ``glarg`` module let's you generate random, pronounceable pseudo-words. It
started life as `StackOverflow answer`_ about password generators. It was then
forked from `greghaskins/gibberish`_, after being abandoned for over 4 years.

.. _`StackOverflow answer`: http://stackoverflow.com/a/5502875/356942
.. _`greghaskins/gibberish`: https://github.com/greghaskins/gibberish


Objectives
==========

1. Security: A reasonably high amount of entropy so that guessing is difficult
   *even when the geneation formula is known*
2. Convenience:

   A. Easy to remember: subjectively easier for English speakers
   B. Easy to input: letters and non-letters are grouped to minimize keyboard
      switching on mobile devices


Usage
=====

``glarg`` creates pseudo-words which consist of one consonant-vowel-consonant
syllable that sounds like it could be English. Sometimes it spits out real
words. Most of the time, it does not::

  >>> import glarg
  >>> glarg.generate_word()
  'zept'
  >>> glarg.generate_word()
  'prast'
  >>> glarg.generate_words(3)
  ['yink', 'glunt', 'skim', 'jask']

It also works as a console script::

  ~$ glarg 6
  Noonk.7038.swab.noold.swousp.kusk.suk
  ~$ glarg
  Dek.1832.led.swuip


Testing Quick Start
===================

1. Change directory into repository (into same directory as where this README
   resides).
2. Install virtual environment (assuming Python 2 is default)::

    mkvirtualenv -a . -r tests/requirements.txt glarg_test2

   a. If installing requirements errors, update `pip`::

        pip install --upgrade pip

   b. Install requirements::

        pip install -r tests/requirements.txt

3. Run pytest::

    py.test

To test against alternate Python versions, it may be useful to create virtual
environments with an interpreter other than the one with which ``virtualenv``
was installed, e.g. for non-default python3::

    PYTHONPATH='' mkvirtualenv -a . -p '/usr/bin/env python3'
        -r tests/requirements.txt glarg_test3


License
=======

- `LICENSE.txt`_ (Expat License/`MIT License`_)

.. _`LICENSE.txt`:
   https://github.com/TimZehta/glarg/blob/master/LICENSE.txt
.. _`MIT License`: http://www.opensource.org/licenses/MIT
