Verify
======

Web-based quiz application.

Questions and answers are stored in quiz.txt in the following format:

    Question:Answer
    Question:Answer

The questions are notoriously True/False and Integer oriented. Why?

Unique Quizzes
==============

The key feature of Verify is that each quiz generated is absolutely unique.
No two students will get the same quiz, or have the same answers. You can
now quiz your students on the computer, and they can't cheat! :)

Setup
=====

    $ virtualenv2 .
    $ source bin/activate
    $ pip install -r requirements.txt
    $ python Verify

Issues
======
Flask only works with Python 2 at the moment.
Our application is [forwards compatible][fw-compat] with Python 3.

[fw-compat]: http://lucumr.pocoo.org/2011/1/22/forwards-compatible-python/
