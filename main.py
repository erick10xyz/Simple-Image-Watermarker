from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from tkinter import messagebox

GREEN = "#9bdeac"

# File source and path, location of text in image
def text_watermark():
    file_path = watermark_input.get()
    im = Image.open(f"{file_path}")
    width, height = im.size
    drawing = ImageDraw.Draw(im)
    font = ImageFont.truetype("CookieCrisp-L36ly.ttf", 75)
    fill_color = (203, 201, 201)
    watermark_text = watermark_text_entry.get()
    x = width - 400
    y = height - 200
    position = (x, y)
    drawing.text(xy=position, text=watermark_text, font=font, fill=fill_color)
    im.show()
    im.save('watermark_image.jpg')
    im.close()
    messagebox.showinfo(title="Done!", message="You've been watermarked baby!")


# File source and path, location of logo in image
def image_watermark():
    file_path = watermark_input.get()
    im = Image.open(f"{file_path}")
    watermark_img = watermark_image_entry.get()
    watermark = Image.open(f'{watermark_img}')

    # Coordinates to place the watermark
    position = (10, 10)
    im.paste(watermark, position)
    im.save('output_image.jpg')
    im.close()
    watermark.close()
    messagebox.showinfo(title="Done!", message="You've been watermarked baby!")

# Simple application window for user interface
window = Tk()
window.title("Text/Image Watermarker")
window.config(padx=50, pady=50, bg=GREEN)

watermark_input = Entry(width=40)
watermark_input.insert(END, string="Enter Image Path file.")
watermark_input.grid(column=0, row=1, columnspan=3)

watermark_label = Label(text='File Location: ')
watermark_label.grid(column=1, row=0, padx=10, pady=20)

watermark_text_button = Button(text="Text Watermark", highlightthickness=0, command=text_watermark)
watermark_text_button.grid(column=0, row=2, padx=10, pady=40)

watermark_text_entry = Entry(width=20)
watermark_text_entry.insert(END, string="Enter Text Watermark!")
watermark_text_entry.grid(column=0, row=3)

watermark_image_button = Button(text="Image Watermark", highlightthickness=0, command=image_watermark)
watermark_image_button.grid(column=2, row=2, padx=10, pady=40)

watermark_image_entry = Entry(width=30)
watermark_image_entry.insert(END, string="Enter Watermark Image Path!")
watermark_image_entry.grid(column=2, row=3)


window.mainloop()


