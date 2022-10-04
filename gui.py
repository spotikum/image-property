import tkinter
from tkinter import *
from tkinter import filedialog
import cv2

def openFile():
    global filepath, image, dimensions, height, width, channels, X, color_depth  
    filepath = filedialog.askopenfilename(title="Open File",
                                          filetypes=(("All Files","*.*"),("Text Files","*.txt"),))
    print(filepath)
    image = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    dimensions = image.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]
    X = "x"
    color_depth = channels ** 2 #rumus = banyaknya channel dipangkatkan 2
    
    print("Image Size = ", width,X,height)
    print("Image Width = ", width)
    print("Image Height = ", height)
    print("Image Channel = ", channels)
    print("Image Color Depth = ", color_depth)
    
    window_name = "Image"
    resize = cv2.resize(image, (300,300))
    cv2.imshow(window_name,resize)

    button = tkinter.Button(text="Show Image Property", 
                            command=showProperty, 
                            width = '20', 
                            height = '2', 
                            bd="2", 
                            bg="orange",)
    button.pack(side="bottom")
    
def showProperty():
    img_property = tkinter.Tk()
    img_property.title("Image Property")
    img_property.geometry("300x150")
    img_property.configure(bg="black")
    
    size = "Image Size =  ", width,X,height
    img_width = "Image Width =  ", width
    img_height = "Image Height = ", height
    img_channel = "Image Channel = ", channels
    img_depth = "Image Depth =  ", color_depth
     
    size_msg = Label(img_property, text=size, bg='black', fg='orange', font='28')
    size_msg.pack()
    width_msg = Label(img_property, text=img_width, bg='black', fg='orange', font='28')
    width_msg.pack()
    height_msg = Label(img_property, text=img_height, bg='black', fg='orange', font='28')
    height_msg.pack()
    channel_msg = Label(img_property, text=img_channel, bg='black', fg='orange', font='28')
    channel_msg.pack()
    depth_msg = Label(img_property, text=img_depth, bg='black', fg='orange', font='28')
    depth_msg.pack()
    
    def exit_window():
        img_property.destroy()
        window.destroy()
    
    exit_btn = Button(img_property,text="Exit",
                                   command=exit_window,
                                   width = '8', 
                                   height = '1', 
                                   bd="2", 
                                   bg="orange",
                                   
                )
    exit_btn.pack(side="bottom")
    print(type(size_msg))
        
window = Tk()
window.title("Open File")
window.geometry("300x100")
window.configure(bg='black')
button = Button(text="File Browser", 
                command=openFile, 
                width = '10', 
                height = '2', 
                bd="2", 
                bg="orange",)
button.pack(side="top")

cv2.waitKey(0)   
cv2.destroyAllWindows() 

window.mainloop()