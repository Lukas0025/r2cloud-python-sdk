import r2cloud.api
import r2cloud.groundStation
import r2cloud.tools.common

from datetime       import datetime
import time

def wait_until(end_datetime):
    while True:
        diff = (end_datetime - datetime.now()).total_seconds()
        if diff < 0: return       # In case end_datetime was in past to begin with
        time.sleep(diff/2)
        if diff <= 0.1: return

# init api
station = r2cloud.api('https://XXXXXXXXXX')
# login to r2cloud
station.login("XXXXXXXXXXXX", "XXXXXXXXXX")

# create new ground station
mySation = r2cloud.groundStation({
    "lat":          10.219722,
    "lon":          16.568468,
    "alt":          20,
    "elevationMin": 10
})

#get sats tle from server
tles = station.tle()

# get all satelites schedules and select meteor
mysh = station.scheduleList()
mysh = r2cloud.tools.common.filterSat(mysh, "NOAA 18")[0]

# disbale autoplaning
mysh.disable()

mysat = r2cloud.tools.common.tleFilterSat(tles, mysh.name).tle[0]

# get future passes (for 24h)
passes = mySation.futurePass(mysat, length = 24)

# select nearist
mypass = passes[0]

print("wait for start " + mypass[0].strftime("%m/%d/%Y, %H:%M:%S"))

wait_until(mypass[0])

# fresh auth token
station.freshAuth()
# start observing
mysh.immediatelyStart()

print("wait for end " + mypass[2].strftime("%m/%d/%Y, %H:%M:%S"))

wait_until(mypass[2])

# fresh auth token
station.freshAuth()
# end observing
mysh.immediatelyComplete()
