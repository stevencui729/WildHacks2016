import os
import csv
import exifread
from os.path import join, getsize

def main():
	print "hi"
	for root, dirs, files in os.walk('Steven-Photos'):
		filenames = []
		dict_list = []
		fieldnames = ["file", "lat", "long"]
		filenames = files
		print filenames
		filenames.remove('.DS_Store')
		print filenames

		for file in filenames:
			with open (file, r+) as imagefile:
				tags = exifread.process_file(imagefile)
			for tag in tags.keys():
				if tag in ('GPS'):
					dict_list.append(tags)
					print "Key: %s, value %s" % (tag, tags[tag])

		with open('names_list.csv', 'wb') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, fieldnames=fieldnames)
			for dict in dict_list:
				wr.writerow(dict)
				
				
	    # print root, "consumes",
	    # print sum(getsize(join(root, name)) for name in files),
	    # print "bytes in", len(files), "non-directory files"
	    # if 'CVS' in dirs:
	    #     dirs.remove('CVS')  # don't visit CVS directories


if __name__ == "__main__":
	main()