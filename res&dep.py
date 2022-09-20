import cv2


img = cv2.imread('kucing.jpeg', cv2.IMREAD_UNCHANGED)


dimensions = img.shape


height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

var4 = channels ** 2 # rumus nya 2/4 = 16

var = str(width)
var2 = str (height)
var3 = str("ukuran")

print('Image Dimension    : ',var3,var,"X",var2)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)
print('color depth        : ',var4)
