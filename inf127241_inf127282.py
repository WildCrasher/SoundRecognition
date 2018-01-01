from __future__ import division
from matplotlib import pylab
from pylab import *
from scipy import *
import numpy as np
import scipy.io.wavfile
import subprocess
import sys

#functions

def load_all_wavfiles():
	ls = subprocess.Popen(("ls","train"), stdout = subprocess.PIPE)
	list_of_files = subprocess.check_output(("tr",' ', '\n'), stdin = ls.stdout)
	ls.wait()
	list_of_files = list_of_files.decode()
	list_of_files = list_of_files.split('\n')
	list_of_files = list_of_files[:-1]

def index_of_max( tab ):
	index = 0
	maks = tab[0]
	
	for i in range(len(tab)):
		if(maks < tab[i]):
			maks = tab[i]
			index = i
	return index
		
	
def find_first_min( rxx, first_pick_lock ):
	i = first_pick_lock + 1
	j = first_pick_lock - 1
	while (rxx[i - 1] > rxx[i]) and (rxx[j + 1] > rxx[j]):
		i += 1
		j -= 1
	return i - 1

#main

#np.set_printoptions(threshold=np.nan)
load_all_wavfiles()
w, signal = scipy.io.wavfile.read(sys.argv[1])
n = len(signal[0])
T = 1/w
sound_time = n/w
print(signal)
rxx = np.correlate(signal/10000, signal/10000, "full")

first_pick_lock = len(signal) - 1

right_min_index = find_first_min(rxx, first_pick_lock) 
left_min_index = first_pick_lock - ( right_min_index - first_pick_lock )

seq = rxx
i = right_min_index
j = left_min_index

seq[j : i] = min(seq)

second_pick_lock = index_of_max(seq)

period_in_samples = abs(second_pick_lock - first_pick_lock)

period = period_in_samples * T
fundamental_frequency = 1/period
print(fundamental_frequency)

#male 85 - 180, female 165 - 255

if(fundamental_frequency <= 165):
	print("M")
elif(fundamental_frequency >= 180):
	print("K")
else:
	print("Not sure")
