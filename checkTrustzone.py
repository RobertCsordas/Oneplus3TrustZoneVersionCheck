#!/usr/bin/python
import zipfile
import sys

if len(sys.argv)<2:
	print("Usage: "+sys.argv[0]+" <Oneplus firmware zip file>")
	sys.exit(-1)

archive = zipfile.ZipFile(sys.argv[1], 'r')
firmware = archive.open('firmware-update/tz.mbn', 'r')
fileText = firmware.read()

MAGIC="QC_IMAGE_VERSION_STRING="
try:
	pos = fileText.index(bytearray(MAGIC,'utf8')) + len(MAGIC)
except:
	print("Trustzone verison not found.")
	sys.exit(-1)

endPos=pos
while fileText[endPos]!=0:
	endPos+=1

print(fileText[pos:endPos].decode("utf-8"))
