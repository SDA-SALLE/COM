# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import os
import sys
import json
sys.path.append('core')
from excelmatriz import * 
from wcsv import *

def distribution(archive, pollutants, year):
	matriz = convertCSVMatrizPoint(archive)
	Position = {}
	Days = {}

	head = matriz[0,:]
	index = 0
	for value in head:
	 	if value == 'ID': 
	 		colID = index
	 	if value == 'ROW': 
	 		colROW = index
	 	if value == 'COL':
	 		colCOL = index
	 	if value == 'LAT': 
	 		colLAT = index
	 	if value == 'LON':
	 		colLON = index
	 	if value == 'FUELTYPE':
	 		colFUELTYPE = index
	 	if value == 'SOURCETYPE': 
	 		colSOURCETYPE = index
	 	if value == 'WORKEDDAYS':
	 		colWORKEDDAYS = index
	 	for pollutant in pollutants: 
	 		if value == pollutant:
	 			Position[value] = index
	 	index += 1

	data = {}
	for i in range(1, matriz.shape[0]):
		ID = matriz[i][colID]
		if data.get(ID) is None: 
			data[ID] = {}
			data[ID]['General'] = {'FUELTYPE': [], 'COL': [], 'LON': [], 'LAT': [], 'ROW': [], 'SOURCETYPE': [], 'WORKEDDAYS': []}
			data[ID]['hours'] = {}
			data[ID]['Pollutants'] = {}

		if data[ID]['General']['COL'] == []:
			data[ID]['General']['COL'].append(int(float(matriz[i][colCOL])))
			data[ID]['General']['ROW'].append(int(float(matriz[i][colROW])))
			data[ID]['General']['LAT'].append(float(matriz[i][colLAT]))
			data[ID]['General']['LON'].append(float(matriz[i][colLON]))
			data[ID]['General']['FUELTYPE'].append(matriz[i][colFUELTYPE])
			data[ID]['General']['SOURCETYPE'].append(matriz[i][colSOURCETYPE])
			data[ID]['General']['WORKEDDAYS'].append(matriz[i][colWORKEDDAYS])

		for pollutant in pollutants: 
			data[ID]['Pollutants'][pollutant] = []
			data[ID]['Pollutants'][pollutant].append(matriz[i][Position[pollutant]])

		for hour in range(0, 25):
			data[ID]['hours'][hour] = []

	matriz = None

	distribution = os.path.join('..', 'data', 'in', 'Constants', 'distribution_' + year + '.xlsx')
	matriz = convertXLSCSVPoint(distribution)

	distribution = {}

	for i in range(1, matriz.shape[0]):
		category = matriz[i][0]
		if distribution.get(category) is None:
			distribution[category] = {}

			for x in range(1, 25):
				hour = int(float(matriz[0][x]))
				if distribution[category].get(hour) is None:
					distribution[category][hour] = matriz[i][x]

	days = os.path.join('..', 'data', 'in', 'Constants', 'DAYS_'+ year +'.xlsx')
	MDays = convertXLSCSVPoint(days)

	for i in range(1, MDays.shape[0]):
		Type = MDays[i][0]
		if Days.get(Type) is None:
			Days[Type] = int(float(MDays[i][2]))

	keys = data.keys()
	for pollutant in pollutants:
		for ID in keys: 
			hours = distribution[data[ID]['General']['SOURCETYPE'][0]].keys()
			for hour in hours: 
				#print Days[data[ID]['General']['WORKEDDAYS'][0]]
				data[ID]['hours'][hour] = float(float(data[ID]['Pollutants'][pollutant][0]) / Days[data[ID]['General']['WORKEDDAYS'][0]]) * float(distribution[data[ID]['General']['SOURCETYPE'][0]][hour])
			data[ID]['hours'][24] = float(data[ID]['Pollutants'][pollutant][0]) * float(distribution[data[ID]['General']['SOURCETYPE'][0]][0])

		WriteDistribution(data, pollutant, year)




