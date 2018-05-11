import os

x = 0
while x < 606:
	print(str(x)+' doing')
	os.system("mv "+str(x)+".png "+str(x-1)+".png")
	x += 1

print('alhamduliLlah')