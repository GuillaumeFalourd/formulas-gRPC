#!/usr/bin/python3
import os

from formula import formula

text = os.environ.get("RIT_TEXT")
name = os.environ.get("RIT_NAME")
surname = os.environ.get("RIT_SURNAME")

formula.run(text, name, surname)
