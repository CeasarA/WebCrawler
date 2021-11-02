import io
from urllib.request import urlopen
import base64
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk


from logo_crawler import download_image, get_url, convert_to_csv

root = Tk()
root.title('Email Verifier')

#initial window size
window_width = 600
window_height = 500

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# root.geometry('600x400+400+150')

#window logo
root.iconbitmap('./assets/amalitech_logo.ico')

a = Label(root, text='Logo Crawler')
a.pack()


#Get URL TExt Box
url = tkinter.StringVar()
url_label = ttk.Label(root, text="Enter Your Url")
url_label.pack(ipadx=1, ipady=2, fill='y', expand=True)

url_entry = ttk.Entry(root, textvariable=url)
url_entry.pack(ipadx=3, ipady=4, expand=True)
url_entry.focus()

# Get the text in the text field
def get_text():
    input_value = url_entry.get()
    imageeeeeeee = get_url(input_value)
    # print(imageeeeeeee)
    # return imageeeeeeee

    image_url = imageeeeeeee
    image_byt = urlopen(image_url).read()
    image_b64 = base64.encodestring(image_byt)

    # Display Image
    canvas = Canvas(root, width = 300, height = 300)
    canvas.pack( expand=True)
    img = tkinter.PhotoImage(data=image_b64)
    canvas.create_image(150, 150, anchor='center', image=img)


# Button 
get_url_button = ttk.Button(root, text="Submit Url", command=lambda: get_text())
# remove the disabled flag
get_url_button.state(['!disabled'])
get_url_button.pack(ipadx=3, ipady=4, expand=True)

# Display Image
# canvas = Canvas(root, width = 300, height = 300)
# canvas.pack()
# img = tkinter.PhotoImage(data=image_b64)
# # img = ImageTk.PhotoImage(Image.open('./images/Kofi nsano web.jpg'))
# canvas.create_image(150, 150, anchor='center', image=img)



# Download Icon
download_button = ttk.Button(root, text="Download Image", command=download_image)
download_button.pack(ipadx=5, ipady=5, expand=True)

# Convert to Csv
csv_button = ttk.Button(root, text="Convert To CSV", command=convert_to_csv)
csv_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()