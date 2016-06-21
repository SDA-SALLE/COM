# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import os
import sys


def listCSV(direccion):
	path = os.path.join(direccion,'')

	#Lista vacia para incluir los ficheros
	lstFilesEmissions = []

	#Lista con todos los ficheros del directorio:
	lstDir = os.walk(path) 

	#Crea una lista de los ficheros que existen en el directorio y los incluye a la lista.
	for root, dirs, files in lstDir:
	    for fichero in files:
	        (nombreFichero, extension) = os.path.splitext(fichero)
	        if(extension == '.csv'):
	        	lstFilesEmissions.append(nombreFichero+extension)

	return lstFilesEmissions