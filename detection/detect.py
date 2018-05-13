from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

def threshold(imageArray):
	balanceArray = []
	newArray = imageArray
	
	for eachRow in imageArray:
		for eachPix in eachRow:
			avgNum = reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3])
			balanceArray.append(avgNum)

	balance = reduce(lambda x, y: x + y, balanceArray)/len(balanceArray)

	for eachRow in newArray:
		for eachPix in eachRow:
			if reduce (lambda x, y: x + y, eachPix[:3])/len(eachPix[:3]) > balance:
				eachPix[0] = 255
				eachPix[1] = 255
				eachPix[2] = 255
				eachPix[3] = 255
			else:
				eachPix[0] = 0
				eachPix[1] = 0
				eachPix[2] = 0
				eachPix[3] = 255
			

i = Image.open('images/mri.jpg')
iar = np.array(i)

i2 = Image.open('images/mri2.jpg')
iar2 = np.array(i2)

threshold(iar)
threshold(iar2)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)

plt.show()

