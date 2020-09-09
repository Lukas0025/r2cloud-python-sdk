import os
import r2cloud.api
import r2cloud.tools.common

# create paths
path = os.getcwd()
if not(os.path.exists(path + "/img")):
  os.mkdir(path + "/img")
  os.mkdir(path + "/img/noaa")
  os.mkdir(path + "/img/meteor")

# init api
station = r2cloud.api('https://XXXXXXXXXX')
# login to r2cloud
station.login("XXXXXXXXXXXX", "XXXXXXXXXX")

# get all observatios of images satellites
observations = station.observationList()
observations = r2cloud.tools.common.filterSat(observations, ["NOAA 19", "NOAA 18", "NOAA 15", "METEOR-M 2"])
observations = r2cloud.tools.common.filterHasData(observations)

try:
  reader = open("last.log", "r")
  lastid = reader.read()
  print("last sync id is " + lastid)
  #find id in array
  for i in range(len(observations)):
      if observations[i].id == lastid:
          break

  #strip array to last observatin
  if i > 0:
      observations = observations[0:i]
  else:
      print("All is up to date")
      exit()
except IOError:
  print("No last sync, sync all")


lastid = observations[0].id
# write last observation to file for next sync
file = open("last.log", "w")
file.write(lastid)
file.close()


# download all images
for ob in observations:
    print("Downloading " + str(ob.id) + ".jpg" + " by " + ob.name)
    image = ob.details().a()
    
    if ob.name == "METEOR-M 2":
      dirname = "meteor"
    else:
      dirname = "noaa"

    r2cloud.tools.common.bin2file(image, "img/" + dirname + "/" + str(ob.id) + ".jpg")
