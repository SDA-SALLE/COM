# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import os
import sys
sys.path.append('core')
from excelmatriz import * 
from wcsv import *
from listCSV import *


def SplitDistribution(folder):
	lstDistribution = listCSV(folder)
	
	for archive in lstDistribution:
		index = 0
		for l in archive: 
			if l == '_': 
				pos = index
			index += 1


		pollutant = archive[:pos]
		data = {}
		data['HABIL'] = {}
		data['NHABIL'] = {}
		archive = folder + archive

		matriz = convertCSVMatrizPoint(archive)
		head = matriz[0,:]
		index = 0 
		
		for value in head: 
			if value == 'WORKEDDAYS':
				colWORKEDDAYS = index
			index += 1
		
		for i in range(1, matriz.shape[0]):
			ID = matriz[i][0]
			WORKEDDAYS = matriz[i][colWORKEDDAYS]

			


			if WORKEDDAYS == 'ALW' or WORKEDDAYS == 'WKD':
				if data['HABIL'].get(ID) is None: 
					data['HABIL'][ID] = {}
				entryHabil = data['HABIL'][ID]
				
				for name in sorted(head): 
					if name != 'ID':
						if entryHabil.get(name) is None: 
							entryHabil[name] = []

				names = entryHabil.keys()
				for name in names: 
					for x in range(1, matriz.shape[1]):
						if matriz[0][x] == name:
							data['HABIL'][ID][name].append(matriz[i][x])

			if WORKEDDAYS == 'ALW' or WORKEDDAYS == 'WKN': 
				if data['NHABIL'].get(ID) is None:
					data['NHABIL'][ID] = {}
				entryNHabil = data['NHABIL'][ID]

				for name in sorted(head): 
					if name != 'ID':
						if entryNHabil.get(name) is None: 
							entryNHabil[name] = []

				names = entryNHabil.keys()
				for name in names: 
					for x in range(1, matriz.shape[1]):
						if matriz[0][x] == name:
							data['NHABIL'][ID][name].append(matriz[i][x])

		WriteSplit(data, pollutant)

