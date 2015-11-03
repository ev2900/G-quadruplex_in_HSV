#!/usr/bin/python

#import statement 
import sys
import re

#system argumnets
fasta_file = sys.argv[1]
gff_file = sys.argv[2]
gff_file_gene_only = sys.argv[3]
gff_file_exon_only = sys.argv[4]

#read in the fasta file
fasta_file_open = open(fasta_file,'r')
sequence = ''
for line_fasta in fasta_file_open.readlines():
	#if not the header
	if ">" not in line_fasta:
		line_fasta = line_fasta.rstrip()
		sequence = sequence + line_fasta
	#if the header or something else
	else:
		header = line_fasta
fasta_file_open.close()

#after the above we have 
#
#	sequence = the genome
#	header = the name of the genome
#

#read in gff file - all
gff_file_gene_open = open(gff_file, 'r')
gff_line_array = []
for line_gff in gff_file_gene_open.readlines():
	#remove new line char
	line_gff = re.sub(r'\n','',line_gff)
	#if not the header
	if "#" not in line_gff:
		line_gff = line_gff.rstrip()
		gff_line_array.append(line_gff)
	#if the header
	else:
		headerLines = []
		headerLines.append(headerLines)
gff_file_gene_open.close()

#read in gff file - genes only 
gff_file_open_gene_only = open(gff_file_gene_only, 'r')
gff_line_array_gene_only = []
for line_gff_gene_only in gff_file_open_gene_only.readlines():
	#remove new line char
	line_gff_gene_only = re.sub(r'\n','',line_gff_gene_only)
	#if not the header
	if "#" not in line_gff_gene_only:
		line_gff_gene_only = line_gff_gene_only.rstrip()
		gff_line_array_gene_only.append(line_gff_gene_only)
	#if the header
	else:
		headerLines = []
		headerLines.append(headerLines)
gff_file_open_gene_only.close()

#read in gff file - exons only
gff_file_open_exon_only = open(gff_file_exon_only, 'r')
gff_line_array_exon_only = []
for line_gff_exon_only in gff_file_open_exon_only.readlines():
	#remove new line char
	line_gff_exon_only = re.sub(r'\n','',line_gff_exon_only)
	#if not the header
	if "#" not in line_gff_exon_only:
		line_gff_exon_only = line_gff_exon_only.rstrip()
		gff_line_array.append(line_gff_exon_only)
	#if the header
	else:
		headerLines = []
		headerLines.append(headerLines)
gff_file_open_exon_only.close()

#after the above we have
#
#	gff_line_array = an array of each line of the gff file
# 	gff_line_array_gene_only = 		
#  	gff_line_array_exon_only = 
#

print ""
print "All motifs"
print ""

# --
# 
# Quadreplex Idenitifciation part of the this program 
#
# --

#regex engine powering the motif finding, vroom vroom.lol
quadreplex_output_array = []

for m in re.finditer(r'G{3,}.{1,7}G{3,}.{1,7}G{3,}.{1,7}G{3,}', sequence, re.I):
	
	string_to_print = str(m.group()) + "\t" + str(m.start()) + "\t" + str(m.end())
	quadreplex_output_array.append(string_to_print)
	print string_to_print

#after the above we have
#
#	 quadreplex_output_array = array of 	motif 	start poisition 	end position
#	
#	

print " "
print "Motfis which matched as in side of a gene"
print " "

# --
#
# Inside of gene or out side of gene identifer, part of this program 
#
# --

for quadreplex in quadreplex_output_array:
	#slit each line of the array 
	motif, startMotif, stopMotif = quadreplex.split("\t")

	for gff_gene_only in gff_line_array_gene_only:
		seqname, source, feature, startFeature, endFeature, score, strand, frame, attribute = gff_gene_only.split("\t")
		
		#check strand orientation
		if strand == '+':
			startFeature = startFeature 
			endFeature = endFeature
		elif strand == '-':
			 startFeature = endFeature
			 endFeature = startFeature

		#matching logic
		if( int(startMotif) > int(startFeature) and int(stopMotif) < int(endFeature) ):
			
			string_to_print_new = motif + "\t" + startMotif + "\t" + stopMotif + str(attribute)
			print string_to_print_new

#after the above we have
#
#	 string_to_print_new = array of 	motif 	start poisition 	end position 	gene the motif is in
#	
#	

print " "
print "Motfis which matched as in side of a exons"
print " "

# --
#
# Inside of exon or out side of exon identifer, part of this program 
#
# --

for quadreplex in quadreplex_output_array:
	#slit each line of the array 
	motif, startMotif, stopMotif = quadreplex.split("\t")

	for gff_exon_only in gff_line_array_exon_only:
		seqname, source, feature, startFeature, endFeature, score, strand, frame, attribute = gff_exon_only.split("\t")
		
		#check strand orientation
		if strand == '+':
			startFeature = startFeature 
			endFeature = endFeature
		elif strand == '-':
			 startFeature = endFeature
			 endFeature = startFeature

		#matching logic
		if( int(startMotif) > int(startFeature) and int(stopMotif) < int(endFeature) ):
			
			string_to_print_new = motif + "\t" + startMotif + "\t" + stopMotif + str(attribute)
			print string_to_print_new
