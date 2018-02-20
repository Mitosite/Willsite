import os

def writetext(content, filename, path):
	os.chdir(path)
	text_file = open(filename, "w")
	text_file.write(content)
	text_file.close()
