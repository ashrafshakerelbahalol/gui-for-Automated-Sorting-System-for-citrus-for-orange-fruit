from tkinter import Toplevel, Canvas
from PIL import Image, ImageTk
from customtkinter import *
app = CTk()
app.config ( bg="#e8edef")
set_appearance_mode("DARK")
app.title("Automated Sorting System for citrus")
app.geometry("1000x700")
app.resizable(False, False)
def button_callback():
    # Create a Toplevel window
    new_window = Toplevel(app)
    # Set the window size
    new_window.geometry("300x300")
    # Set the window title
    new_window.title("New Window")
    new_window.mainloop()

def read_img():
    global Img, path
    path = filedialog.askopenfilename(initialdir='/', title='Select the Image',
                                      filetypes=(('imagefiles', '.png'), ('imagefiles', '.jpg')))
    Img = Image.open(path)
    my_image2 = CTkImage(light_image= Img, size=(250, 200))
    CTkLabel(frame1, image=my_image2,text="").pack()

"""""""""
app.grid_columnconfigure((1,2,3,4,5,6,7) , weight=0 , uniform = 'a')
app.grid_rowconfigure((1,2,3,4,5) , weight=1,uniform = 'a')
"""""""""

##buttons##
button2 = CTkButton(app, text="history", command=button_callback, fg_color="dark orange",text_color="#000000"
                    , bg_color= "#e8edef" ,hover_color="yellow")
button4 = CTkButton(app, text="detect orange", command=button_callback, fg_color="dark orange",text_color="#000000"
                    , bg_color="#e8edef"  ,hover_color="yellow")
button5 = CTkButton(app, text="classify orange", command=button_callback, fg_color="dark orange",text_color="#000000"
                    , bg_color="#e8edef"  ,hover_color="yellow")
button6 =CTkButton(app, text="sort healthy", command=button_callback, fg_color="dark orange",text_color="#000000"
                   , bg_color="#e8edef"   ,hover_color="yellow")
button3 = CTkButton(app, text="automatic", command=button_callback, fg_color="dark orange",text_color="#000000"
                    , bg_color="#e8edef" ,hover_color="yellow")
button1 = CTkButton(app, text="read image", command=read_img, fg_color="dark orange",text_color="#000000"
                    , bg_color="#e8edef" ,hover_color="yellow")

button1.place(x=400, y=150)
button2.place(x=400, y=200)
button3.place(x=400, y=250)
button4.place(x=400, y=300)
button5.place(x=400, y=350)
button6.place(x=400, y=400)

##frames
frame1 = CTkFrame(app,width=250,height=200,bg_color="#e8edef")
frame1.place(x=50, y=200)
frame2 = CTkFrame(app,width=250,height=200,bg_color="#e8edef")
frame2.place(x=600, y=200)

##ctkimage
#logo
my_image1 = CTkImage(light_image= Image.open("Automated Sorting System for citrus for orange fruit.png"), size=(100, 100))
image_label1 = CTkLabel(app, image=my_image1,text="").place(x=10,y=10)

##labels
label1 = CTkLabel(app, text="input image" ,bg_color="#e8edef",text_color=("#000000","#000000"))
label1.place(x=50,y=170)
label2 = CTkLabel(app, text="result image" ,bg_color="#e8edef",text_color=("#000000","#000000"))
label2.place(x=600, y=170)
##the output
# Create a Canvas widget
canvas =Canvas(app, width=1500, height=3 ,bg="green")
canvas.place(x=0,y=600)
# Draw a line on the canvas
line = canvas.create_line(0,380, 1000, 380)
label3 = CTkLabel(app, text="no of oranges" ,font=("Time new roman",18),bg_color="#e8edef",text_color=("#000000","#000000"))
label3.place(x=10,y=500)
label4 = CTkLabel(app, text="no of healthy oranges",font=("Time new roman",18) ,bg_color="#e8edef",text_color=("#000000","#000000"))
label4.place(x=10, y=530)
label4 = CTkLabel(app, text="no of sick oranges" ,font=("Time new roman",18),bg_color="#e8edef",text_color=("#000000","#000000"))
label4.place(x=10, y=560)
label5 = CTkLabel(app, text="0" ,font=("Time new roman",18),bg_color="#e8edef",text_color=("#000000","#000000"))
label5.place(x=180,y=500)
label6 = CTkLabel(app, text="0",font=("Time new roman",18) ,bg_color="#e8edef",text_color=("#000000","#000000"))
label6.place(x=180, y=530)
label7 = CTkLabel(app, text="0" ,font=("Time new roman",18),bg_color="#e8edef",text_color=("#000000","#000000"))
label7.place(x=180, y=560)
app.mainloop()
