#!/usr/bin/python3
# Secret = "I will never use nested zip again!"
import re
from shutil import copy, rmtree
from os import remove, rmdir, mkdir, listdir, path
from zipfile import ZipFile, is_zipfile

# Working Folder
extractFolder = 'extracts'
if not path.isdir(extractFolder):
	mkdir(extractFolder)

# Copy the original file to extracts folder
filePath = extractFolder + '/' + 'unZipMe.zip'
copy('unZipMe.zip', filePath)

while is_zipfile(filePath):
	zippedFile = ZipFile(filePath, 'r')
	fileContent = zippedFile.namelist()
	containsZip = False
	for element in fileContent:
		regResult = re.match(r'(.*\.zip)', element)
		if regResult:
			containsZip = True
			zipMember = regResult.groups()[0]
			print(' - {} found in {}'.format(zipMember, filePath))

	if not containsZip: # Check if it is the last zip file
		print("Found last Zip file")
		break

	# Remove old zip file
	remove(filePath)

	filePath = zippedFile.extract(zipMember, extractFolder)

# Extract all files from last zip file
print("Extracting content")
zippedFile.extractall()
print("Extraction Done")

# Remove extracts folder
rmtree(extractFolder)

