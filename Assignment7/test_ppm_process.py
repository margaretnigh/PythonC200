import pytest
from ppm_process import *

def test_process():
    this = process(['255', '0', '0', '0', '255', '0', '0', '0', '255', '255', '255', '255', '0', '0', '0', '255', '0', '0', '0', '255', '0', '0', '0', '255', '255', '0', '255', '0', '0', '0', '255', '0', '0', '0', '255', '0', '0', '255', '255', '255', '0', '255', '0', '0', '0', '255', '0', '0', '255', '0', '0', '0', '255', '0', '0', '0', '255', '255', '255', '255', '0', '0', '0', '255', '0', '0', '0', '255', '0', '0', '0', '255'],6,4)
    assert this == [[[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]], [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255]], [[255, 0, 255], [0, 0, 0], [255, 0, 0], [0, 255, 0]], [[0, 255, 255], [255, 0, 255], [0, 0, 0], [255, 0, 0]], [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]], [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255]]]

def test_scale():
    this2 = [[[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]], [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255]], [[255, 0, 255], [0, 0, 0], [255, 0, 0], [0, 255, 0]], [[0, 255, 255], [255, 0, 255], [0, 0, 0], [255, 0, 0]], [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]], [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255]]]
    assert this2 == [[[255,0,0], [0,0,225]],[[0,255,255],[0,0,0]]]
