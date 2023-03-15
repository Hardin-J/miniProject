f = open("temp_id.txt", "r")
temp_id = f.read()
print(temp_id)
f = open("temp_id.txt", "w")
l = 10000
f.write(str(l))
d = open("temp_id.txt", "r")
temp_id = d.read()
print(d.read())
