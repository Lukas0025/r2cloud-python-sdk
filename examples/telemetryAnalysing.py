import matplotlib
import matplotlib.pyplot as plt
import r2cloud.api
import r2cloud.tools.common

# init api
station = r2cloud.api('https://XXXXXXXXXX')
# login to r2cloud
station.login("XXXXXXXXXXXX", "XXXXXXXXXX")


# get all observatios of NAYIF-1 (EO-88)
observations = station.observationList()
observations = r2cloud.tools.common.filterSat(observations, "NAYIF-1 (EO-88)")

# keep only with data
observations = r2cloud.tools.common.filterHasData(observations)

if len(observations) == 0:
       print("no observations :(")
       exit()

# find observation with highest number of packets
best = observations[0].details()
for observation in observations:
  if best.numberOfDecodedPackets < observation.details().numberOfDecodedPackets:
      best = observation.details()

# get data from observation
time     = []
volatage = []
for data in best.dataEntity:
       time.append(data['name']) #uptime
       volatage.append(data['body']['realtimeTelemetry']['batteryVolts'])



fig, ax = plt.subplots()
ax.plot(time, volatage)

ax.set(xlabel='uptime (ms)', ylabel='voltage (mV)',
       title='NAYIF-1 (EO-88) Battery volatage')
ax.grid()
plt.show()