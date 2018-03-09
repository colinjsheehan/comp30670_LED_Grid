#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_grid` package."""
# tests/test_led_tester.py
import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
from led_grid import main


def test_read_file():
    ifile = "./data/input_assign3.txt"
    buffer = main.read_file(ifile)
    assert buffer == "10\nturn off 2,4 through 6,9"
    arraySize=int(buffer.split("\n")[0])
    for line in buffer.split("\n")[1:]:
        cmd, x1, y1, x2, y2 = main.get_cmd(line,arraySize)
    
    assert arraySize == 10
    assert cmd == 'turn off'
    assert x1 == 2
    assert y1 == 4
    assert x2 == 6
    assert y2 == 9
