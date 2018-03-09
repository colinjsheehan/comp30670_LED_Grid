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
