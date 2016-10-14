#created by @ceapalaciosal
#under code Creative Commons
# -*- encoding: utf-8 -*-

#! /usr/bin/env python
import csv
import os

def WriteYear(data, year):

	folder = os.path.join('..', 'data', 'out','year', '')
	csvsalida = open(folder + 'Year_Emisions_'+ year +'.csv', 'w')

	keys = data.keys()
	identi = 0
	for ID in keys: 
		if identi == 0:
			names = sorted(data[ID]['base'].keys())
			names.insert(0, 'ID')
			for name in names: 
				csvsalida.write(name)
				csvsalida.write(',')

			names = sorted(data[ID]['results'].keys())
			for name in names: 
				if name == names[0]:
					csvsalida.write(name)
				else: 
					csvsalida.write(',')
					csvsalida.write(name)
			csvsalida.write('\n')
			identi = 1

		csvsalida.write(str(ID))
		csvsalida.write(',')
		
		names = sorted(data[ID]['base'].keys())
		for name in names:
			csvsalida.write(str(data[ID]['base'][name][0]))
			csvsalida.write(',')

		names = sorted(data[ID]['results'].keys())
		for name in names:
			if name == names[0]:
				csvsalida.write(str(data[ID]['results'][name][0]))
			else: 
				csvsalida.write(',')
				csvsalida.write(str(data[ID]['results'][name][0]))
		csvsalida.write('\n')
	csvsalida.close()

def WriteDistribution(data, pollutant, year): 
	folder = os.path.join('..', 'data', 'out','distribution', '')
	csvsalida = open(folder + pollutant + '_distribution_'+ year +'.csv', 'w')

	names = ['ID', 'FUELTYPE', 'WORKEDDAYS','ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names: 
		if name == names[0]:
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	keys = data.keys()
	for ID in keys:
		csvsalida.write(str(ID))
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['FUELTYPE'][0])
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['WORKEDDAYS'][0])
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['ROW'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['COL'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LAT'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LON'][0]))
		csvsalida.write(',')
		csvsalida.write(pollutant)
		csvsalida.write(',')
		csvsalida.write('g/h')
		hours = data[ID]['hours'].keys()
		for hours in hours: 
			csvsalida.write(',')
			csvsalida.write(str(data[ID]['hours'][hours]))
		csvsalida.write('\n')

def WriteSplit(data, pollutant, year):
	folder = os.path.join('..', 'data', 'out','split', '')

	Types = data.keys()
	for Type in Types:
		csvsalida = open(folder + pollutant + '_' + Type + '_'+ year +'.csv', 'w')
		names = ['ID', 'FUELTYPE', 'WORKEDDAYS','ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
		for name in names: 
			if name == names[0]:
				csvsalida.write(name)
			else: 
				csvsalida.write(',')
				csvsalida.write(name)
		csvsalida.write('\n')

		keys = data[Type].keys()
		for ID in keys: 
			csvsalida.write(ID)
			csvsalida.write(',')
			csvsalida.write(data[Type][ID]['FUELTYPE'][0])
			csvsalida.write(',')
			csvsalida.write(data[Type][ID]['WORKEDDAYS'][0])
			csvsalida.write(',')
			csvsalida.write(data[Type][ID]['ROW'][0])
			csvsalida.write(',')
			csvsalida.write(data[Type][ID]['COL'][0])
			csvsalida.write(',')
			csvsalida.write(data[Type][ID]['LAT'][0])
			csvsalida.write(',')
			csvsalida.write(data[Type][ID]['LON'][0])
			csvsalida.write(',')
			csvsalida.write(data[Type][ID]['POLNAME'][0])
			csvsalida.write(',')
			csvsalida.write(data[Type][ID]['UNIT'][0])
			hours = names[9:]
			for hour in hours:
				csvsalida.write(',')
				csvsalida.write(data[Type][ID][hour][0])
			csvsalida.write('\n')

def WriteSpeciationVOC(data, POLNAME, Type):
	#print POLNAME
	folder = os.path.join('..', 'data', 'out', 'speciation', '')
	csvsalida = open(folder + POLNAME + Type, 'w')

	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names: 
		if name == names[0]:
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	keys = data.keys()
	for ID in keys:
		csvsalida.write(str(data[ID]['General']['ROW']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['COL']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LAT']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LON']))
		csvsalida.write(',')
		csvsalida.write(POLNAME)
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['UNIT'])
		hours = names[6:]
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[ID]['hours'][hour]))
		csvsalida.write('\n')

def WriteSpeciationPM25(data, POLNAME, Type, FUEL):
	folder = os.path.join('..', 'data', 'out', 'speciation', '')
	csvsalida = open(folder + POLNAME +  '_' + FUEL + Type, 'w')

	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names: 
		if name == names[0]:
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	keys = data.keys()
	for ID in keys:
		csvsalida.write(str(data[ID]['General']['ROW']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['COL']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LAT']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LON']))
		csvsalida.write(',')
		csvsalida.write(POLNAME)
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['UNIT'])
		hours = names[6:]
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[ID]['hours'][hour]))
		csvsalida.write('\n')

def WriteSpeciation(data, POLNAME, Type):
	#print Type
	folder = os.path.join('..', 'data', 'out', 'speciation', '')
	csvsalida = open(folder + POLNAME + Type, 'w')

	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names: 
		if name == names[0]:
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	keys = data.keys()
	for ID in keys:
		csvsalida.write(str(data[ID]['General']['ROW']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['COL']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LAT']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LON']))
		csvsalida.write(',')
		csvsalida.write(POLNAME)
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['UNIT'])
		hours = names[6:]
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[ID]['hours'][hour]))
		csvsalida.write('\n')