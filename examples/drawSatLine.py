import os
import r2cloud.api
import r2cloud.tools.common
import gpxpy
import gpxpy.gpx
from datetime import timedelta

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
gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Create points:
time_delta = last.details().end - last.details().start
for seconds in range(int(time_delta.total_seconds())):
    (lon, lat, alt) = last.details().tle.pyOrbital.get_lonlatalt(
        last.details().start + timedelta(seconds=seconds)
    )

    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat, lon, elevation=alt))

f = open("sat.gpx", "w+")
f.write(gpx.to_xml())
f.close()

print("line is saved to sat.gpx. You can vizualized it with https://www.gpsvisualizer.com/")