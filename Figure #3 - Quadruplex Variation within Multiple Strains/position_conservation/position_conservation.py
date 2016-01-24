#!/usr/bin/python

#import statement 
import sys
import re

#system argumnets
reference_quadrplex = sys.argv[1]
compare_quadrplex = sys.argv[2]

#read in reference_quadrplex
reference_quadrplex_open = open(reference_quadrplex, 'r')
reference_quadrplex_line_array = []

for line_reference_quadrplex in reference_quadrplex_open.readlines():
	#remove new line char
	line_reference_quadrplex = re.sub(r'\n','',line_reference_quadrplex)
	line_reference_quadrplex = re.sub(r'\t','',line_reference_quadrplex)
	reference_quadrplex_line_array.append(line_reference_quadrplex)

reference_quadrplex_open.close()

#read in compare_quadrplex
compare_quadrplex_open = open(compare_quadrplex, 'r')
compare_quadrplex_line_array = []

for line_compare_quadrplex in compare_quadrplex_open.readlines():
	#remove new line char
	line_compare_quadrplex = re.sub(r'\n','',line_compare_quadrplex)
	line_compare_quadrplex = re.sub(r'\t','',line_compare_quadrplex)
	compare_quadrplex_line_array.append(line_compare_quadrplex)

compare_quadrplex_open.close()

#after the above we have 
#
#	reference_quadrplex_line_array
#	compare_quadrplex_line_array
#

for line in reference_quadrplex_line_array:

	temp_line_split = []
	temp_line_split = line.split(' ')
	
	motif_17 = temp_line_split[0]
	start_17 = temp_line_split[1]
	end_17 = temp_line_split[2]


	for line_comp in compare_quadrplex_line_array:

			temp_line_split_comp = []
			temp_line_split_comp = line_comp.split(' ')
			
			comp_motif = temp_line_split_comp[0]
			comp_start = temp_line_split_comp[1]
			comp_end = temp_line_split_comp[2]

			if start_17 == comp_start:

				print motif_17 + ' ' + start_17 
				print comp_motif + ' ' + comp_start