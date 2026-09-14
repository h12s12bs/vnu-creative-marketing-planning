# -*- coding: utf-8 -*-
"""
tools/chapter_content_w01_w04.py
Weeks 1 to 4 chapter slides (4 weeks x 18 slides = 72 unique slides).
"""
import os
import sys

sys.path.append(os.path.dirname(__file__))
from chapter_content_w01_w09 import get_weeks_1_to_9

def get_weeks_1_to_4():
    w = get_weeks_1_to_9()
    return {k: w[k] for k in ["1", "2", "3", "4"] if k in w}
