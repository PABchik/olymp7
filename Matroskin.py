barrel = 88
bucket = 0
can = 0

bucketVol = 12
canVolume = 7

for i in range(1, 100):
    barrel -= bucketVol
    bucket = bucketVol
    if barrel < 11:
        print(i)
        break

    bucket -= canVolume
    can = canVolume
    barrel += bucket
    bucket = 0

    can -= 4
    barrel += can
    can = 0
