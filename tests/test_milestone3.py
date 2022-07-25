from app.milestone3 import *
import pytest


test = Patent("I have an idea", "Joe Bonotz", "active", "2032/07/24")


assert type(test.anticipatedExpiration) == str
assert type(test.inventor) == str
assert type(test.status) == str