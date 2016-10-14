# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import os
import os
import sys
from matriz import *
from clear import *

def listaCSV(direccion):
   	#Variable para la ruta al directorio
	path = os.path.join(direccion,'')
	#print direccion

	#Lista vacia para incluir los ficheros
	lstFilesEmissions = []

	#Lista con todos los ficheros del directorio:
	lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
	datos = {}

	#Crea una lista de los ficheros que existen en el directorio y los incluye a la lista.
	for root, dirs, files in lstDir:
	    for fichero in files:
	        (nombreFichero, extension) = os.path.splitext(fichero)
	        if(extension == '.csv'):
	        	lstFilesEmissions.append(nombreFichero+extension)

	return lstFilesEmissions

def final(Archive):
	
	data = {}
	matriz = convertCSVMatrizPoint(Archive)
	head = matriz[0,:]
	index = 0
	
	for value in head:
		if value == 'ROW':
			colROW = index
		if value == 'COL':
			colCOL = index
		if value == 'LAT':
			colLAT = index
		if value == 'LON':
			colLON = index
		if value == 'POLNAME':
			colPollname = index
		if value == 'UNIT':
			colUnit = index
		index += 1


	for i in range(1, matriz.shape[0]):
		keys = matriz[i][colROW] + matriz[i][colCOL] + matriz[i][colPollname]
		
		if data.get(keys) is None:
			data[keys] = {}
			data[keys]['hours'] = {}
			data[keys]['GENERAL'] = {'ROW': [], 'COL': [], 'LAT': [], 'LON': [], 'POLNAME': [], 'UNIT':[]}

		
		for hour in range(0, 25):
			data[keys]['hours'][hour] = []

	
	for i in range(1, matriz.shape[0]):
		keys = matriz[i][colROW] + matriz[i][colCOL] + matriz[i][colPollname]
		if data[keys]['GENERAL']['ROW'] == []:
			data[keys]['GENERAL']['ROW'].append(matriz[i][colROW])
			data[keys]['GENERAL']['COL'].append(matriz[i][colCOL])
			data[keys]['GENERAL']['LAT'].append(matriz[i][colLAT])
			data[keys]['GENERAL']['LON'].append(matriz[i][colLON])
			data[keys]['GENERAL']['POLNAME'].append(matriz[i][colPollname])
			data[keys]['GENERAL']['UNIT'].append(matriz[i][colUnit])

		hour = 0
		for x in range(6, matriz.shape[1]):
			data[keys]['hours'][hour].append(matriz[i][x])
			hour += 1

	matriz = None
	keys = data.keys()
	for key in keys:
		hours = data[key]['hours'].keys()
		for hour in hours:
			if hour == 'GENERAL':
				pass
			else:
				suma = eval('+'.join(data[key]['hours'][hour]))
				data[key]['hours'][hour] = []
				data[key]['hours'][hour].append(suma)

	
	csvsalida = open(Archive, 'w')
	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names:
		if name == names[0]:
			csvsalida.write(name)
		else:
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	names = data.keys()

	for key in names:
		csvsalida.write(data[key]['GENERAL']['ROW'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['COL'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['LAT'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['LON'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['POLNAME'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['UNIT'][0])
		#csvsalida.write(',')
		hours = data[key]['hours'].keys()
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[key]['hours'][hour][0]))
		csvsalida.write('\n')
	csvsalida.close ()

def merge(folder):

	lista = listaCSV(folder)
	for archiv in lista:
		archive = folder + archiv	
		final(archive)

def UNIONS(folder, year):

	listHabil = []
	listNHabil = []

	#folder = os.path.join('..', 'data', 'in', 'unions', '')
	listout = listaCSV(folder)
	
	for out in listout:

		if 'ENH' in out or 'NHABIL' in out or '_NHabil' in out:
			listNHabil.append(out)
		elif 'EH' in out or 'HABIL' in out or '_Habil' in out:
			listHabil.append(out)

	foldersave = os.path.join('..', 'data', 'out', 'UNIONS', '')
	
	csvsalida = open(foldersave + 'pnt_commercial_weekend_'+ year +'.csv', 'w')

	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names:
		if name == 'ROW':
			csvsalida.write(name)
		else:
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')
	
	for lista in listNHabil:
		archive = folder + lista
		matriz = convertCSVMatrizPoint(archive)
		for i in range(1, matriz.shape[0]):
			for x in range(0, matriz.shape[1]):
				if x == 0:
					csvsalida.write(matriz[i][x])
				else:
					csvsalida.write(',')
					csvsalida.write(matriz[i][x])
			csvsalida.write('\n')
		matriz = None
	csvsalida.close()

	csvsalida = open(foldersave + 'pnt_commercial_weekday.'+ year +'.csv', 'w')
	for name in names:
		if name == 'ROW':
			csvsalida.write(name)
		else:
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')
	for lista in listHabil:
		archive = folder + lista
		matriz = convertCSVMatrizPoint(archive)
		for i in range(1, matriz.shape[0]):
			for x in range(0, matriz.shape[1]):
				if x == 0:
					csvsalida.write(matriz[i][x])
				else:
					csvsalida.write(',')
					csvsalida.write(matriz[i][x])
			csvsalida.write('\n')

		matriz = None
	csvsalida.close()