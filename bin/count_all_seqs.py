#!/usr/bin/env python


import os.path
import sys
import seq_utils


def count_All(input_file_path):
	cnt =0
	files_path = input_file_path
	filename_list = sorted(os.listdir(files_path))
#listing the results
	line_counts = []
	file_grouped = []
#Looping through the list and paths etc
	for filename in filename_list:	
		try:
			if filename.endswith('.fasta'):
				path = os.path.join(files_path, filename)
				input_file = open(path)
		except IOError as e:
			print >>sys.stderr, "Failed to open {}: {}".format(path, e.strerror)
			
		else:
				seq_count = seq_utils.count_seqs(input_file)
				#line_counts.append(seq_count)
				print seq_count, "in", filename
				input_file.close()
		

def arguFile():
	if len(sys.argv)!=2:
		print >>sys.stderr,"Usage; count_all_seqs.py<filename>"
		sys.exit(1)
	if __name__ == '__main__':
		count_All(sys.argv[1])
	
arguFile()




 
#print count_All("/home/sanbi/Dropbox/python/coding/Python/data")
