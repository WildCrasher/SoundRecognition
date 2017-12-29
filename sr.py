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

sound_time = n/w
t = linspace(0, sound_time, n, endpoint=False)
#t = arange(0, sound_time, 1/w)

subplot(311)
plot(t, signal, '*')
xlabel("Probki")
ylabel("Signal[t]")

signal1 = fft(signal)*2/n
signal1 = abs(signal1)
freqs = linspace(0, w, n, endpoint=False)

subplot(312)
plot(freqs, signal1, '-*')
#stem(freqs, signal1, '-*')
xlabel("w [Hz]")
ylabel('fft(signal)')

rxx_lags = xcorr(signal, signal)
rxx = rxx_lags[0]
lags = rxx_lags[1]

subplot(313)
plot(lags, rxx, '.')

show()
