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
from unions import *

folder = os.path.join('..','data', 'out', '')
clear(folder)

year = raw_input('Insert year running: ')

database = os.path.join('..', 'data', 'in', 'database_'+ year +'.xlsx')
Pollutants = emition(database, year)

emitions = os.path.join('..', 'data', 'out', 'year', 'Year_Emisions_'+ year +'.csv')
distribution(emitions, Pollutants, year)

distribution = os.path.join('..', 'data','out', 'distribution', '')
SplitDistribution(distribution, year)

split = os.path.join('..', 'data','out', 'split', '')
speciation(split, year)

'''INIT UNIONS'''
folder = os.path.join('..', 'data', 'out', 'speciation', '')
UNIONS(folder, year)

folder = os.path.join('..', 'data', 'out', 'UNIONS', '')
merge(folder)

'''END UNIONS'''