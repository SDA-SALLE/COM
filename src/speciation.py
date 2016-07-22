#! /usr/bin/env python
#-*- encoding: utf-8 -*-

#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
import json
sys.path.append('core')
from listCSV import * 
from excelmatriz import *
from wcsv import *


def speciation(folder):

	VOC = os.path.join('..', 'data', 'in', 'Speciation', 'COM_SCP_PROF_VOC.xlsx')
	MVOC = convertXLSCSVPoint(VOC)
	VOC = {}

	head = MVOC[0,:]
	index = 0
	for value in head: 
		if value == 'SPCID':
			colSPCID = index
		if value == 'MASSFRAC':
			colMASSFRAC = index
		if value == 'SPC_MOL_W':
			colSPC = index
		if value == 'FUEL_TYPE':
			colFUELTYPE = index
		index += 1 

	for i in range(1, MVOC.shape[0]):
		name = MVOC[i][colFUELTYPE]
		SPCID = MVOC[i][colSPCID]
		
		if VOC.get(name) is None: 
			VOC[name] = {}

		entrySPCID = VOC[name]
		if entrySPCID.get(SPCID) is None:
			entrySPCID[SPCID] = {'MASSFRAC': float(MVOC[i][colMASSFRAC]), 'SPC_MOL_W': float(MVOC[i][colSPC])}

	#PM25
	PM25 = os.path.join('..', 'data', 'in', 'Speciation', 'COM_SCP_PROF_PM25.xlsx')
	MPM25 = convertXLSCSVPoint(PM25)
	PM25 = {}

	head = MPM25[0,:]
	index = 0
	for value in head: 
		if value == 'SPCID':
			colSPCID = index
		if value == 'MASSFRAC':
			colMASSFRAC = index
		if value == 'FUEL_TYPE':
			colFUELTYPE = index
		index += 1 

	for i in range(1, MPM25.shape[0]):
		name = MPM25[i][colFUELTYPE]
		SPCID = MPM25[i][colSPCID]
		
		if PM25.get(name) is None: 
			PM25[name] = {}

		entrySPCID = PM25[name]
		if entrySPCID.get(SPCID) is None:
			entrySPCID[SPCID] = {'MASSFRAC': float(MPM25[i][colMASSFRAC])}


	CSV = listCSV(folder)


	for archive in CSV: 
		index = 0
		data = {}
		for n in archive:
			if n == '_':
				pos = index
			index += 1 
		
		#VOC
		if archive[:pos] == 'VOC': 

			Types = VOC.keys()
			VOCS = VOC[Types[0]].keys()

			for SPC in VOCS:

				archive2 = folder + archive
				matriz = convertCSVMatrizPoint(archive2)
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
				 	if value == 'UNIT': 
				 		colUNIT = index
				 	if value == 'POLNAME': 
				 		colPOLNAME = index
				 	if value == 'FUELTYPE':
				 		colFUELTYPE = index
					index += 1

				data = {}	
				for i in range(1, matriz.shape[0]):
					ID = matriz[i][colID]
					
					if data.get(ID) is None:
						data[ID] = {'General': {'ROW': int(float(matriz[i][colROW])), 'COL': int(float(matriz[i][colCOL])), 'LAT': float(matriz[i][colLAT]), 'LON': float(matriz[i][colLON]), 'UNIT': matriz[i][colUNIT], 'POLNAME': matriz[i][colPOLNAME], 'FUELTYPE': matriz[i][colFUELTYPE]}, 'hours': {}}

					for x in range(colUNIT + 1, matriz.shape[1]):
						hour = matriz[0][x]
						if data[ID]['hours'].get(hour) is None:
							#print matriz[i][x]
							data[ID]['hours'][hour] = float(matriz[i][x])

				keys = data.keys()
			 	#print SPCID
			  	for ID in keys: 
			  		hours = data[ID]['hours'].keys()
			  		#print data[ID]['hours']
			  		for hour in hours: 
			 			if data[ID]['General']['FUELTYPE'] not in VOC.keys():
			  				data[ID]['General']['FUELTYPE'] = 'CHARBROILING'
			  			data[ID]['hours'][hour] = (data[ID]['hours'][hour] * VOC[data[ID]['General']['FUELTYPE']][SPC]['MASSFRAC']) / (VOC[data[ID]['General']['FUELTYPE']][SPC]['SPC_MOL_W'] * 3600)
			  		data[ID]['General']['UNIT'] = 'mol/s'

				WriteSpeciationVOC(data, SPC, archive[pos:])
		
		#PM25
		elif archive[:pos] == 'PM25': 
			archive2 = folder + archive
			matriz = convertCSVMatrizPoint(archive2)
			head = matriz[0,:]
			data = {}
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
			 	if value == 'UNIT': 
			 		colUNIT = index
			 	if value == 'POLNAME': 
			 		colPOLNAME = index
			 	if value == 'FUELTYPE':
			 		colFUELTYPE = index
				index += 1

			for i in range(1, matriz.shape[0]):
				ID = matriz[i][colID]
				
				if data.get(ID) is None:
					data[ID] = {'General': {'ROW': int(float(matriz[i][colROW])), 'COL': int(float(matriz[i][colCOL])), 'LAT': float(matriz[i][colLAT]), 'LON': float(matriz[i][colLON]), 'UNIT': matriz[i][colUNIT], 'POLNAME': matriz[i][colPOLNAME], 'FUELTYPE': matriz[i][colFUELTYPE]}, 'hours': {}}

				for x in range(colUNIT + 1, matriz.shape[1]):
					hour = matriz[0][x]
					if data[ID]['hours'].get(hour) is None:
						data[ID]['hours'][hour] = float(matriz[i][x])

			FUELTYPE = PM25.keys()
			keys = data.keys()
			for Type in FUELTYPE: 
				SPCID = PM25[Type].keys()
				for SP in SPCID:
					for ID in keys: 
						hours = data[ID]['hours'].keys()
						for hour in hours: 
							if data[ID]['General']['FUELTYPE'] not in  VOC.keys():
								data[ID]['General']['FUELTYPE'] = 'CHARBROILING'
							data[ID]['hours'][hour] = (data[ID]['hours'][hour] * PM25[Type][SP]['MASSFRAC']) / 3600
							data[ID]['General']['UNIT'] = 'g/s'
				
					WriteSpeciationPM25(data, SP, archive[pos:], Type)

		#NOX
		elif archive[:pos] == 'NOX':

			for POLNAME in ['NO2', 'NO']:
				
				archive2 = folder + archive
				matriz = convertCSVMatrizPoint(archive2)
				head = matriz[0,:]
				data = {}

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
				 	if value == 'UNIT': 
				 		colUNIT = index
				 	if value == 'POLNAME': 
				 		colPOLNAME = index
				 	if value == 'FUELTYPE':
				 		colFUELTYPE = index
					index += 1
				
				for i in range(1, matriz.shape[0]):
					ID = matriz[i][colID]

					if data.get(ID) is None:
						data[ID] = {'General': {'ROW': int(float(matriz[i][colROW])), 'COL': int(float(matriz[i][colCOL])), 'LAT': float(matriz[i][colLAT]), 'LON': float(matriz[i][colLON]), 'UNIT': matriz[i][colUNIT], 'POLNAME': matriz[i][colPOLNAME], 'FUELTYPE': matriz[i][colFUELTYPE]}, 'hours': {}}

					for x in range(colUNIT + 1, matriz.shape[1]):
						hour = matriz[0][x]
						if data[ID]['hours'].get(hour) is None:
							if POLNAME == 'NO2': 
								data[ID]['hours'][hour] = float(matriz[i][x]) * 0.1 / (3600 * 46)
							elif POLNAME == 'NO': 
								data[ID]['hours'][hour] = float(matriz[i][x]) * 0.9 / (3600 * 30)

					data[ID]['General']['UNIT'] = 'g/s'

				#print data
				WriteSpeciation(data, POLNAME, archive[pos:])

		#OTHERS
		#print archive[:pos]
		if archive[:pos] not in ['VOC', 'PM25', 'NOX', 'PM10']:
			#print archive[:pos]
			archive2 = folder + archive
			matriz = convertCSVMatrizPoint(archive2)
			head = matriz[0,:]
			data = {}

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
			 	if value == 'UNIT': 
			 		colUNIT = index
			 	if value == 'POLNAME': 
			 		colPOLNAME = index
			 	if value == 'FUELTYPE':
			 		colFUELTYPE = index
				index += 1
			
			for i in range(1, matriz.shape[0]):
				ID = matriz[i][colID]

				if data.get(ID) is None:
					data[ID] = {'General': {'ROW': int(float(matriz[i][colROW])), 'COL': int(float(matriz[i][colCOL])), 'LAT': float(matriz[i][colLAT]), 'LON': float(matriz[i][colLON]), 'UNIT': matriz[i][colUNIT], 'POLNAME': matriz[i][colPOLNAME], 'FUELTYPE': matriz[i][colFUELTYPE]}, 'hours': {}}

				for x in range(colUNIT + 1, matriz.shape[1]):
					hour = matriz[0][x]
					if data[ID]['hours'].get(hour) is None:
						if archive[:pos] == 'CO': 
							data[ID]['hours'][hour] = float(matriz[i][x])/(3600*28)
						if archive[:pos] == 'CO2': 
							data[ID]['hours'][hour] = float(matriz[i][x])/(3600*44)
						if archive[:pos] == 'SO': 
							data[ID]['hours'][hour] = float(matriz[i][x])/(3600*64)
						else: 
							data[ID]['hours'][hour] = float(matriz[i][x])/3600


				data[ID]['General']['UNIT'] = 'g/s'

			WriteSpeciation(data, archive[:pos], archive[pos:])
