from __future__ import division
from matplotlib import pylab
from pylab import *
from numpy import *
from scipy import *
import scipy.io.wavfile

w, signal = scipy.io.wavfile.read('003_K.wav')
print("czestotliwosc probkowania: {}".format(w))
n = len(signal)
print( "dlugosc sygnalu: {}".format(n) )


subplot(211)
t = linspace(0, n, n, endpoint=False)
plot(t, signal, '*')

signal1 = fft(signal)
signal1 = abs(signal1)

subplot(212)
freqs = linspace(0, w, n, endpoint=False)
print("przed")
stem(freqs, signal1, '-*')
print("po")
xlabel("w [Hz]")
ylabel('fft(signal)')
print("show")
plot.show()
