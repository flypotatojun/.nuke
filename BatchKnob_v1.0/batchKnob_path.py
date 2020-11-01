# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 9/5/2017

import os

inNuke = True


GLOBAL_Folder = ""

if inNuke:
    GLOBAL_Folder = os.path.expanduser('~').replace('\\','/') + '/.nuke/BatchKnob_v1.0'
else:
    GLOBAL_Folder = "F:/Temp/pycharm/BatchKnob pyqtT v1.0"