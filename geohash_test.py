import Geohash
#works fine

#print(Geohash.encode(45.0602750,7.6548340))
arr = Geohash.decode_exactly("u0j2q4yp4s1f")
print(arr[1]," ",arr[2])