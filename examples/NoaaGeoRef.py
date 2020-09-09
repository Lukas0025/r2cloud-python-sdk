import julia
from julia import APTDecoder
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

# download all images and georef
for ob in allObservations:
  print("Downloading " + str(ob.id) + " by " + ob.name)

  wavname = "gqrx_" + ob.start.strftime('%Y%m%d_%H%M%S') + "_" + str(ob.details().frequency) + ".wav"
  
  raw = ob.details().raw()
  r2cloud.tools.common.bin2file(raw, wavname)

  print("Decoding and GeoReferencing")
  APTDecoder.makeplots(wavname, ob.name)