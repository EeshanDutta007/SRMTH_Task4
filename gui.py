from tkinter import *
from PIL import Image, ImageTk
app=Tk()
app.title("Filtering")
app.geometry('795x447+200+100')
l1=Label(app,text="Availabe Filters:",height =2)
l2=Label(app,text="Preview")
b1=Button(app,text='Sobel Horizontal',width=19)
b2=Button(app,text='Sobel Vertical',width=19)
b3=Button(app,text='Laplacian Operation',width=19)
b4=Button(app,text='Gaussian Blur',width=19)
b5=Button(app,text="Browse",width=19)
b6=Button(app,text='Take from Camera',width=19)
b7=Button(app,text="Crop",width=19)
tmp_img=Image.open('no-preview.jpg')
def_img=tmp_img.resize((300,300), Image.ANTIALIAS)
pic=ImageTk.PhotoImage(def_img)
photolabel=Label(app,image=pic,bg='white')
l1.grid(row = 0, column = 1 , columnspan = 2, rowspan=2)
b1.grid(row = 2,column=0,padx=9)
b2.grid(row = 2,column=1,padx=9)
b3.grid(row = 2,column=2,padx=9)
b4.grid(row = 2,column=3,padx=9)
b5.grid(row=11,column=3,padx=9)
b6.grid(row=12,column=3,padx=9,pady=6)
b7.grid(row=4,column=3,padx=9,pady=6)

photolabel.grid(row=3,column=0,columnspan=3,rowspan=10,padx=9,pady=(20,4))
l2.grid(row=13,column=0,columnspan=3)

app.mainloop()
