import takehomemidterm
import pytest
import random as rn
from pytest import approx

# Feel free to add more test cases as you see fit
x1_str = "The cat is outside, but the cat should be in the house."
e1_unique = ["the", "cat", "is", "outside", "but", "should", "be", "in", "house"]
e1_transmat = [[0,2,0,0,0,0, 0, 0, 1,],[0, 0, 1, 0, 0, 1, 0, 0, 0],[0, 0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0,0, 0],[1, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 1, 0],[1, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]

xlist2 = [11, 82, 91, 55, 32, 91, 12, 5]
per2 = 3
e2_runavg = [61.33, 76.0, 59.33, 59.33, 45.0, 36.0]

def test_Problem1():

    assert e1_unique == takehomemidterm.unique_words(x1_str)
    assert e1_transmat == takehomemidterm.get_transition_matrix(x1_str)

def test_Problem2():

    assert e2_runavg ==  takehomemidterm.running_average(xlist2,per2)
