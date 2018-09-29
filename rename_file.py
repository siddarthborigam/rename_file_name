import os

file = open("photo_sequence_mrg.txt", "r")
content = file.read()
lines = content.split("\n")
count = 0
for x in lines:
	count = count +1
print "Total Number of Photos is :" + str(count)
for x in lines:
	y = x.split("\t")
	scr = y[1] 
	dst = y[0]
	try:
		os.rename(scr + ".JPG", dst)
	except:
		print scr 
		

# #os.rename(src, dst)
# scr = '1.JPG'
# des = '2.JPG'
# try:
	# os.rename(scr,des)
# except:
	# print scr
