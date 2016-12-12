#!/usr/bin/python

#import statement 
import sys
import re
import matplotlib.pyplot as plt

#system argumnets
'''
HM585503_E15_file = sys.argv[0]
HM585504_E22_file = sys.argv[1]
GU734772_H129_file = sys.argv[2]
HM585515_R62_file = sys.argv[3]
HM585506_E25_file = sys.argv[4]
HM585507_E35_file = sys.argv[5]
HM585514_R11_file = sys.argv[6]
DQ889502_HF10_file = sys.argv[7]
GU734771_F_file = sys.argv[8]
HM585505_E23_file = sys.argv[9]
HM585496_E06_file = sys.argv[10]
HM585497_E07_file = sys.argv[11]
JN555585_17_file = sys.argv[12]
HM585508_CR38_file = sys.argv[13]
HM585499_E10_file = sys.argv[14]
HM585511_E19_file = sys.argv[15]
JQ730035_McKrae_file = sys.argv[16]
HM585501_E12_file = sys.argv[17]
HM585502_E13_file = sys.argv[18]
HM585512_S23_file = sys.argv[19]
HM585513_S25_file = sys.argv[20]
HM585500_E11_file = sys.argv[21]
JQ673480_KOS_file = sys.argv[22]
HM585510_E14_file = sys.argv[23]
HM585498_E08_file = sys.argv[24]
'''

#read in the files

#plot the plot 

x = [126, 7910, 9165, 11388, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33638, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 100200, 108658, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 120554, 120593, 122206, 123470, 123574, 123889,
126344, 127112, 136456, 137008, 137085, 7910, 9165, 11388, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 28795, 30083, 33636, 36758, 38227, 40075, 41460, 42976, 45304, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 100200, 111090, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 120554, 120593, 122206, 123470, 123574, 123889, 126344, 127112, 136456, 137008, 137085, 126, 7910, 9165, 11389, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33631, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 97153, 100200, 108658, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 117453, 120544, 120689, 122206, 123470, 123574, 123889, 126215, 126344, 126700, 127112, 136456, 137008, 137085, 137139, 126, 7910, 9165, 11389, 16159, 17506, 17555, 17605, 21868, 25715, 27020, 27176, 30083, 33631, 36758, 38227, 40075, 41460, 42976, 43746, 45304, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63541, 63749, 63936, 64166, 65723, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 100200, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 117453, 120554, 120689, 122206, 123470, 123574, 123889, 126215,126344, 126700, 127112, 129545, 136456, 137008, 137085, 126, 7910, 9165, 11388, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33638, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 100200, 108658, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 120554, 120593, 122206, 123470, 123574, 123889, 126344, 127112, 130123, 136456, 137008, 137085, 126, 7910, 9165, 11388, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33638, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 100200, 108658, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 120554, 120593, 122206, 123470, 123574, 123889, 126215, 126344, 126700, 127112, 129449, 129545, 136456, 137008, 137085, 137203, 126, 7910, 9165, 11389, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33631, 34628, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63541, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 97153, 100200, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 117453, 120544, 120689, 122206, 123470, 123574, 123889, 126215, 126344, 126700, 127112, 129545, 136456, 137008, 137085, 126, 7910, 9165, 11389, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33631, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53104, 55698, 55806, 57398, 59428, 59826, 60699, 62584, 62608, 62632, 62692, 62716, 62740, 62764, 62900, 63002, 63069, 63173, 63261, 63366, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 100200, 113384, 113516, 114180, 114805, 116708, 116991, 117123, 117174, 117453, 120544, 120582, 120689, 122206, 123470, 123889, 124108, 124229, 124298, 124335, 126215, 126344, 126700, 127112, 135858, 136073, 136102, 136456, 137008, 126, 7910, 9165, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33631, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63541, 63749, 63936, 64166, 69155, 69369, 70615, 72190, 82254, 87073, 92266, 93900, 95979, 97153, 100200, 108658, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 117453, 120544, 120689, 122206, 123470, 123574, 123889, 126215, 126344, 126700, 127112, 136456, 137008, 137085, 126, 7910, 9165, 11388, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33638, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 100200, 108658, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 120554, 120593, 122206, 123470, 123574, 123889, 126215, 126344, 126700, 127112, 129449, 129545, 136456, 137008, 137085, 137203, 126, 7910, 9165, 11388, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33638, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 100200, 108658, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 120554, 120593, 122206, 123470, 123574, 123889, 26344, 127112, 136456, 137008, 137085, 126, 7910, 9165, 11389, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33638, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 117453, 120544, 120689, 122206, 123470, 123574, 123889, 126215, 126344, 126700, 127112, 129449, 136456, 137008, 137085, 7910, 9165, 11389, 16159, 17377, 17506, 17555, 17605, 21868, 23698, 25731, 27020, 27176, 30083,
 31567, 33631, 34628, 36758, 38227, 40075, 41460, 42976, 45304, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62692, 62716, 62740, 62764, 62900, 63002, 63069, 63173, 63261, 63366, 63541, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 97153, 100200, 109255, 111248, 113156, 113384, 114180, 114805, 116708, 116901, 116937, 116973, 117123, 117174, 117453, 120544, 120689, 123470, 123574, 123889, 124301, 124346, 126344, 126700, 127112, 129545, 135854, 135884, 135914, 135944, 135974, 136004, 136034, 136064, 136094, 136456,  137008, 137085, 126, 7910, 9165, 11388, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33638, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 100200, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 120554, 120593, 122206, 123470, 123574, 123889, 126344, 127112,136456, 137008, 137085, 126, 7910, 9165, 11389, 16159, 17506, 17555, 17605, 21868, 25740, 27176, 30083, 33631, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62584, 62608, 62692, 62716, 62740, 62764, 62900, 63002, 63069, 63173, 63261, 63366, 63541, 63749, 63936, 64166, 69155, 69369, 70615, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 111248, 113384, 113516, 114180, 114805, 116708, 116973, 117123, 117174, 117453, 120544, 120689, 122206, 123470, 123574, 123889, 126215, 126344, 126700, 127112, 129449, 129545, 136456, 137008, 137085, 126, 7910,  9165, 11389, 16159, 17506, 17555, 17605, 21868, 25731, 27020, 27176, 30083, 33631, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63541, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 96053, 97153, 100200, 111249, 113384, 113516, 114180, 114805, 116708, 116973, 117123, 117174, 117453, 120544, 120582, 120689, 122206, 123470, 123574, 123889, 124336, 124582, 126215, 126344, 126700, 127112, 135854, 135923, 135952, 135982, 136012, 136042, 136072, 136102, 136456, 137008, 137085, 126, 7910, 9165, 11389, 16159, 17506, 17555, 17605, 21868, 25740, 27020, 27176, 30083, 33631, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63260, 63366, 63541, 63749, 63936, 64166, 6915, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 97153, 100200, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 117453, 120554, 120689, 122206, 123470, 123574, 123889, 126344, 126700, 127112, 129449, 136456, 137008, 137085, 137203, 126, 7910, 9165, 11389, 16159, 17506, 17555, 17605, 21868, 25740, 27176, 30083, 33631, 36758, 38227, 40075, 41460, 42976, 45304, 46568, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63541, 63749, 63936, 64166, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 97153, 100200, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 117453, 120554, 120689, 122206, 123470, 123574, 123889, 126344, 126700, 127112, 129449, 136456, 137008, 137085, 137203, 126, 7910, 9165, 11389, 16159, 17506, 17555, 17605, 21868, 25731, 27020, 27176, 30083, 33631, 36758, 38227, 40075, 41460, 42976, 43746, 45304, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62584, 62608, 62632, 62656, 62680, 62704, 62728, 62752, 62776, 62800, 62900, 63002, 63069, 63173, 63261, 63366, 63541, 63749, 63936, 64166, 65723, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 100200, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 117453, 122206, 123470, 123574, 123889, 124278, 124324, 124475, 126215, 126344, 126700, 127112, 129545, 136456, 137008, 137085, 126, 7910, 9165, 11389, 16159, 17506, 17555, 17605, 21868, 25731, 27020, 27176, 30083, 33631, 36758, 38227, 40075, 41460, 42976, 43746, 45304, 47320, 53134, 55698, 55806, 57398, 59428, 59826, 60699, 62900, 63002, 63069, 63173, 63261, 63366, 63541, 63749, 63936, 64166, 65723, 69155, 69369, 72190, 82254, 87073, 92266, 93900, 95979, 100200, 111248, 113384, 113516, 114180, 114805, 116708, 117123, 117174, 117453, 120554, 120689, 122206, 123470, 123574, 123889, 124278, 124324, 126215, 126344, 126700, 127112, 129545, 135854, 136013, 136068, 136094, 136456, 137008, 137085]

y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,  9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16 , 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

plt.scatter(x,y)

plt.show()