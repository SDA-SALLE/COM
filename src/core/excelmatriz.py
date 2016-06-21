# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

#List Library Import
import csv
import os
import xlrd
import unicodedata
import numpy as np



def convertXLSCSV(direccion):
	#print direccion

	direccionexcel = direccion
	workbook = xlrd.open_workbook(direccionexcel)
	all_worksheets = workbook.sheet_names()

	data = workbook.sheet_by_index(0) #Numero de Sheet donde se encuentran los datos
	direccioncsv = direccionexcel + '.csv'

	data_emissions = open(''.join([direccioncsv]), 'wb') #crea el csv datos Base
	emissions = csv.writer(data_emissions, delimiter='|') #quoting=csv.QUOTE_ALL) #Abre el CSV para escritura de emsiones

 	for rownum in xrange(data.nrows):
 		emissions.writerow([unicode(entry).encode("utf-8") for entry in data.row_values(rownum)]) #unicode(entry).encode("utf-8")

 	data_emissions.close()

 	matriz = convertCSVMatriz(direccioncsv)
 	return matriz


def convertCSVMatriz(direccioncsv):
	matriz = np.genfromtxt(direccioncsv, delimiter='|', dtype=None)
	return  matriz


def convertXLSCSVPoint(direccion):
	direccionexcel = direccion
	workbook = xlrd.open_workbook(direccionexcel)
	all_worksheets = workbook.sheet_names()

	data = workbook.sheet_by_index(0) #Numero de Sheet donde se encuentran los datos
	direccioncsv = direccionexcel + '.csv'

	data_emissions = open(''.join([direccioncsv]), 'wb') #crea el csv datos Base
	emissions = csv.writer(data_emissions, delimiter=',') #quoting=csv.QUOTE_ALL) #Abre el CSV para escritura de emsiones

 	for rownum in xrange(data.nrows):
 		emissions.writerow([unicode(entry).encode("utf-8") for entry in data.row_values(rownum)]) #unicode(entry).encode("utf-8")

 	data_emissions.close()

 	matriz = convertCSVMatrizPoint(direccioncsv)
 	return matriz

def convertCSVMatrizPoint(direccioncsv):
	matriz = np.genfromtxt(direccioncsv, delimiter=',', dtype=None)
	return  matriz

