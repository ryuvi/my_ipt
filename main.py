bbat = open("bbat.m3u", "r").read()

name = ""
details = []
final = 

for line in bbat:
    if line.startswith("#EXTINF"):
        item = line.split(",")
        name = 

#EXTINF:-1 tvg-logo="http://bit.ly/2igU9Hj" group-title="1° TEMPORADA", BBAT T1|EP1
#http://origin.ntcdn.us/content/sobdemanda/netcine-bucket/tbbt/01dub/01-ALTO.mp4
