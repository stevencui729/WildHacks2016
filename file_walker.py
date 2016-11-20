import os
import sys
import csv
import exifread
from os.path import join, getsize

def convert_to_degrees(value):
	d = float(value.values[0].num) / float(value.values[0].den)
	m = float(value.values[1].num) / float(value.values[1].den)
	s = float(value.values[2].num) / float(value.values[2].den)
	return d + (m / 60.0) + (s / 3600.0)

def parseLatLon(latLonDict):
	parsedLatLonDict = {}

	degLat = convert_to_degrees(latLonDict["GPS GPSLatitude"])
	if latLonDict["GPS GPSLatitudeRef"] != "N":
		degLat = 0 - degLat
	degLon = convert_to_degrees(latLonDict["GPS GPSLongitude"])
	if latLonDict["GPS GPSLongitudeRef"] != "E":
		degLon = 0 - degLon

	parsedLatLonDict["lat"] = degLat
	parsedLatLonDict["lon"] = degLon

	return parsedLatLonDict


def main():
	print "hi"
	for root, dirs, files in os.walk('Steven-Photos'):
		path_base = os.path.basename("Steven-Photos")
		filenames = []
		files = files[1:]
		for file in files:
			filenames.append(os.path.join(path_base, file))
		dict_list = []
		fieldnames = ["file", "lat", "lon"]

		for file in filenames:
			with open (file, "r+") as imagefile:
				tags = exifread.process_file(imagefile)
				latlonkeys = ['GPS GPSLatitude', "GPS GPSLatitudeRef", "GPS GPSLongitude", "GPS GPSLongitudeRef"]
				latlondata = {key:value for key,value in tags.items() if key in latlonkeys}
				cur_dict = parseLatLon(latlondata)
				cur_dict["file"] = file
				dict_list.append(cur_dict)

		with open('names_list.csv', 'wb') as myfile:
			wr = csv.DictWriter(myfile, quoting=csv.QUOTE_ALL, fieldnames=fieldnames)
			wr.writeheader()
			for dict in dict_list:
				wr.writerow(dict)
				
				
	    # print root, "consumes",
	    # print sum(getsize(join(root, name)) for name in files),
	    # print "bytes in", len(files), "non-directory files"
	    # if 'CVS' in dirs:
	    #     dirs.remove('CVS')  # don't visit CVS directories


if __name__ == "__main__":
	main()