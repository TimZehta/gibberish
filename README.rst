==============================
glarg: a pseudo-word generator
==============================


History
=======

The ``glarg`` module let's you generate random, pronounceable pseudo-words. It
started life as `StackOverflow answer`_ about password generators. It was then
forked from `greghaskins/gibberish`_, after being abandoned for over 4 years.

.. _`StackOverflow answer`: http://stackoverflow.com/a/5502875/356942
.. _`greghaskins/gibberish`: https://github.com/greghaskins/gibberish


Usage
=====

``glarg`` creates pseudo-words which consist of one consonant-vowel-consonant
syllable that sounds like it could be English. Sometimes it spits out real
words; most of the time not::

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


License
=======

- `LICENSE.txt`_ (`MIT License`_)

.. _`LICENSE.txt`:
   https://github.com/ClockworkNet/gacli/blob/master/LICENSE.txt
.. _`MIT License`: http://www.opensource.org/licenses/MIT
