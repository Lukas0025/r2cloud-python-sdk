import os
import r2cloud.api
import r2cloud.tools.common

# init api
station = r2cloud.api('https://XXXXXXXXXX')
# login to r2cloud
station.login("XXXXXXXXXXXX", "XXXXXXXXXX")

# get all observatios of images satellites
observations = station.observationList()
observations = r2cloud.tools.common.filterSat(observations, ["NOAA 19", "NOAA 18", "NOAA 15", "METEOR-M 2"])
observations = r2cloud.tools.common.filterHasData(observations)

last = observations[0]

# get lat, lon, alt of satellite when start
(lon, lat, alt) = last.details().tle.pyOrbital.get_lonlatalt(
    last.details().start
)

print("lon:" + str(lon) + " lat:" + str(lat) + " alt:" + str(alt))

# get lat, lon, alt of satellite when end
(lon, lat, alt) = last.details().tle.pyOrbital.get_lonlatalt(
    last.details().end
)

print("lon:" + str(lon) + " lat:" + str(lat) + " alt:" + str(alt))
