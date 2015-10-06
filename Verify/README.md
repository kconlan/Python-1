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

    $ virtualenv3
    $ source bin/activate
    $ pip install -r requirements.txt
    $ python Verify
