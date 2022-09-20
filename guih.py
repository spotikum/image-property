
import PySimpleGUI as sg
import cv2

sg.theme('dark grey 9')


window = sg.Window('Window Title')


filename = sg.popup_get_file('Enter the file you wish to process')

print(filename)


img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

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


mytex = "Image Dimension",var3,var, "X", var2
varheit = "Image Height",height
varwidit = "Image Width",width
varcanel = "Number of Channels",channels
var444 = "color depth",var4




#mylist = ['Image Dimension    : ',mytex,
#'Image Height       : ',height,
#'Image Width        : ',width,
#'Number of Channels : ',channels,
#'color depth        : ',var4

#]

layout = [
            [sg.Text(mytex)],
            [sg.Text(varheit)],
            [sg.Text(varwidit)],
            [sg.Text(varcanel)],
            [sg.Text(var444)],
            [sg.Button('Save'), sg.Button('Exit')]
         ]

window = sg.Window('To Do List Example', layout)


  
# path 
path = filename
  
# Reading an image in default mode
image = cv2.imread(path)
  
# Window name in which image is displayed
window_name = 'image'
  
# Using cv2.imshow() method 
# Displaying the image 
resize = cv2.resize(image, (246, 240))
cv2.imshow(window_name, resize)
  
#waits for user to press any key 
#(this is necessary to avoid Python kernel form crashing)
event, values = window.read()
cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows() 







    

#sg.Window('You entered', var3,var, "X", var2)





