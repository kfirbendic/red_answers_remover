from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
import img2pdf
from PIL import Image
import os

def pdf2img():
	try:
		images = convert_from_path(str(e1.get()))
		for i in range(len(images)):
			# Save pages as images in the pdf
			if i <= 9:
				images[i].save('page0' + str(i) + '.jpg', 'JPEG')
			else:
				images[i].save('page' + str(i) + '.jpg', 'JPEG')
		for i in range(len(images)):
			# read image
			if i <= 9:
				src = cv2.imread('page0' + str(i) + '.jpg', cv2.IMREAD_UNCHANGED)
			else:
				src = cv2.imread('page' + str(i) + '.jpg', cv2.IMREAD_UNCHANGED)
			#print(src.shape)

			# Make all red pixels white
			src[np.all(src[:, :, 2] > 10, axis=-1)] = (255, 255, 255)

			# save image
			if i <= 9:
				cv2.imwrite('page0' + str(i) + 'noRed.jpg', src)
			else:
				cv2.imwrite('page' + str(i) + 'noRed.jpg', src)

		# opening or creating pdf file
		file = open('exam no answers.pdf', "wb")


		#list of files in dir
		list_of_files = os.listdir()

		#list of images to pdf
		list_to_pdf = [i for i in list_of_files if i.endswith("noRed.jpg")]

		# converting into chunks using img2pdf
		pdf_bytes = img2pdf.convert(list_to_pdf)

		# writing pdf files with chunks
		file.write(pdf_bytes)

		# closing pdf file
		file.close()

		for f in list_of_files:
			if f.endswith('.jpg'):
				os.remove(f)

	except :
		Result = "NO pdf found"
		messagebox.showinfo("Result", Result)

	else:
		Result = "success"
		messagebox.showinfo("Result", Result)



master = Tk()
Label(master, text="File Location").grid(row=0, sticky=W)

e1 = Entry(master)
e1.grid(row=0, column=1)

b = Button(master, text="Convert", command=pdf2img)
b.grid(row=0, column=2,columnspan=2, rowspan=2,padx=5, pady=5)

mainloop()
