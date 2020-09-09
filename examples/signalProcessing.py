import r2cloud.api
import r2cloud.tools.common
import matplotlib.pyplot as plot
from scipy.io import wavfile


# init api
station = r2cloud.api('https://XXXXXXXXXX')
# login to r2cloud
station.login("XXXXXXXXXXXX", "XXXXXXXXXX")

# get all observatios of NOAA 19
observations = station.observationList()

# keep only with data
observations = r2cloud.tools.common.filterHasData(observations)
observations = r2cloud.tools.common.filterSat(observations, "NOAA 19")

# get last observation
last = observations[0].details()

#download wav
r2cloud.tools.common.bin2file(last.raw(), "test.wav")

#load wav
samplingFrequency, signalData = wavfile.read('test.wav')

# Plot the signal read from wav file
plot.subplot(211)
plot.title('Spectrogram of a wav ' + last.tle.line1)
plot.plot(signalData)
plot.xlabel('Sample')
plot.ylabel('Amplitude')

plot.subplot(212)
plot.specgram(signalData,Fs=samplingFrequency)
plot.xlabel('Time')
plot.ylabel('Frequency')


plot.show()