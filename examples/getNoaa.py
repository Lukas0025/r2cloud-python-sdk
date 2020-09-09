import r2cloud.api
import r2cloud.tools.common

# init api
station = r2cloud.api('https://XXXXXXXXXX')
# login to r2cloud
station.login("XXXXXXXXXXXX", "XXXXXXXXXX")


obs = station.observationList()

obs = r2cloud.tools.common.filterSat(obs, ["NOAA 19", "NOAA 18", "NOAA 15"])
obs = r2cloud.tools.common.filterHasData(obs)

for ob in obs:
    print("Downloading " + str(ob.id) + ".jpg" + " by " + ob.name)
    image = ob.details().a()
    r2cloud.tools.common.bin2file(image, str(ob.id) + ".jpg")
