import os
import r2cloud.api
import r2cloud.tools.common

# init api
station = r2cloud.api('https://XXXXXXXXXX')
# login to r2cloud
station.login("XXXXXXXXXXXX", "XXXXXXXXXX")


# get all observatios
allObservations = station.observationList()

allObservations = r2cloud.tools.common.filterSat(allObservations, ["NOAA 19", "NOAA 18", "NOAA 15"])
allObservations = r2cloud.tools.common.filterHasData(allObservations)

#download wav
raw = allObservations[0].details().raw()
r2cloud.tools.common.bin2file(raw, "test.wav")

# run wxtoimg
os.system('wxtoimg -e NO test.wav > image.jpg')