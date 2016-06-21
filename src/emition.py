# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
import json
import math
sys.path.append('core')
from excelmatriz import * 
from wcsv import *

def emition(archive): 
	matriz = convertXLSCSV(archive)

	head = matriz[0,:]
	index = 0
	for value in head: 
		if value == 'LAT':
			colLAT = index
		if value == 'LON':
			colLON = index
		if value == 'ROW':
			colROW = index
		if value == 'COL':
			colCOL = index
		if value == 'BUSINESS ID':
			colID = index
		if value == 'SOURCE TYPE':
			colSOURCETYPE = index
		if value == 'YEAR' or value == ' YEAR':
			colYEAR = index
		if value == 'WDW':
			colWDW = index		
		if value == 'FUEL TYPE':
			colFUELTYPE = index
		if value == 'FUEL CONSUMPTION':
			colFUELCONSUMPTION = index
		if value == 'GROW RATE':
			colGROWRATE = index
		if value == 'CoBChP':
			colCoBChP = index
		if value == 'CoBP':
			colCoBP = index
		if value == 'CoCh':
			colCoCh = index
		if value == 'FUEL ID': 
			colFUELID = index
		index += 1

	data = {}
	for i in range(1, matriz.shape[0]):
		ID = matriz[i][colID]
		if data.get(ID) is None:
			data[ID] = {} 
			data[ID]['base'] = {'LAT': [], 'LON': [], 'ROW': [], 'COL': [], 'SOURCETYPE': [], 'YEAR': [], 'FUELTYPE': [], 'FUELCONSUMPTION': [], 'CoBChP': [], 'CoBP': [], 'CoCh': [], 'FUELID': [], 'WDW': [], 'GROWRATE': []}
			data[ID]['results'] = {'TOTALCONSUMPTION': [], 'WORKEDDAYS': []}

		if data[ID]['base']['LAT'] == []:
			data[ID]['base']['LAT'].append(float(matriz[i][colLAT]))
			data[ID]['base']['LON'].append(float(matriz[i][colLON]))
			data[ID]['base']['ROW'].append(int(float(matriz[i][colROW])))
			data[ID]['base']['COL'].append(int(float(matriz[i][colCOL])))
			data[ID]['base']['SOURCETYPE'].append(matriz[i][colSOURCETYPE])
			data[ID]['base']['YEAR'].append(int(float(matriz[i][colYEAR])))
			data[ID]['base']['FUELTYPE'].append(matriz[i][colFUELTYPE])
			data[ID]['base']['FUELCONSUMPTION'].append(float(matriz[i][colFUELCONSUMPTION]))
			data[ID]['base']['CoBChP'].append(float(matriz[i][colCoBChP]))
			data[ID]['base']['CoBP'].append(float(matriz[i][colCoBP]))
			data[ID]['base']['CoCh'].append(float(matriz[i][colCoCh]))
			data[ID]['base']['FUELID'].append(matriz[i][colFUELID])
			data[ID]['base']['WDW'].append(int(float(matriz[i][colWDW])))
			data[ID]['base']['GROWRATE'].append(float(matriz[i][colGROWRATE]))


		data[ID]['results']['TOTALCONSUMPTION'].append(data[ID]['base']['FUELCONSUMPTION'][0] + data[ID]['base']['CoBChP'][0] + data[ID]['base']['CoBP'][0] + data[ID]['base']['CoCh'][0])
		if data[ID]['base']['WDW'][0] >= 6:
			data[ID]['results']['WORKEDDAYS'].append('ALW')
		elif data[ID]['base']['WDW'][0] >= 3 and data[ID]['base']['WDW'][0] <= 5:
			data[ID]['results']['WORKEDDAYS'].append('WKD')
		elif data[ID]['base']['WDW'][0] <= 2:
			data[ID]['results']['WORKEDDAYS'].append('WKN')


	matriz = None		
	
	archive = os.path.join('..', 'data', 'in', 'EmissionsFactors', 'EmissionFactors.xlsx')
	matriz = convertXLSCSV(archive)

	head = matriz[0,:]
	
	EmissionFactors = {}
	for i in range(1, matriz.shape[0]):
		
		name = matriz[i][0]
		if EmissionFactors.get(name) is None: 
			EmissionFactors[name] = {}
		
			for x in range(2, matriz.shape[1]):
				pollutant = matriz[0][x]
				if EmissionFactors[name].get(pollutant) is None: 
					EmissionFactors[name][pollutant] = float(matriz[i][x])

	YEAR = int(raw_input('Insert Year: '))



	keys = data.keys()
	for ID in keys: 
		Pollutants = EmissionFactors[data[ID]['base']['FUELID'][0]].keys()
		n = YEAR - data[ID]['base']['YEAR'][0]
		if n < 0: 
			print 'Review YEAR, number negative. ID = ',ID
		for pollutant in Pollutants: 
			data[ID]['results'][pollutant] = []
			data[ID]['results'][pollutant].append((float(data[ID]['results']['TOTALCONSUMPTION'][0]) * float(EmissionFactors[data[ID]['base']['FUELID'][0]][pollutant]) * (math.exp(data[ID]['base']['GROWRATE'][0] * n))) * 12)
			if pollutant == 'PM10':
				data[ID]['results']['PM25'] = []
				data[ID]['results']['PMC'] = []
				data[ID]['results']['PM25'].append(data[ID]['results'][pollutant][0] * 0.52)
				data[ID]['results']['PMC'].append(data[ID]['results'][pollutant][0] * 0.48)

	Pollutants.insert(0, 'PM25')
	Pollutants.insert(0, 'PMC')
	WriteYear(data)
	return Pollutants

