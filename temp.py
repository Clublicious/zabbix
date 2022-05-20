with open(r"/sys/class/thermal/thermal_zone0/temp") as File:
    CurrentTemp = File.readline()

print(int(float(CurrentTemp) / 1000))

