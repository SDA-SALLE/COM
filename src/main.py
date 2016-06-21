#! /usr/bin/env python
#-*- encoding: utf-8 -*-

#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
sys.path.append('core')
from clear import *
from emition import *
from distribution import *
from split import *
from speciation import *

folder = os.path.join('..','data', 'out', '')
clear(folder)

database = os.path.join('..', 'data', 'in', 'database.xlsx')
Pollutants = emition(database)

emitions = os.path.join('..', 'data', 'out', 'year', 'Year_Emisions.csv')
distribution(emitions, Pollutants)

distribution = os.path.join('..', 'data','out', 'distribution', '')
SplitDistribution(distribution)

split = os.path.join('..', 'data','out', 'split', '')
speciation(split)
