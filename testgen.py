import random
import numpy as np
import csv
import os, os.path
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


questions  = [os.listdir('chapters/11'), os.listdir('chapters/12'), os.listdir('chapters/13'), os.listdir('chapters/14'), os.listdir('chapters/15')]
valid = False


while not valid: 
    option = input("Generate new test or open existing one?: ")
    if (option == "open" or option == "new"): 
        valid = True

if option == "new":
#GENERATING NEW TEST
    mytest = []
    size =  int(input("How many questions?: ")) + 1
    name = input("Name of test: ")

    completed = open('completed.csv', 'a+')
    new_test = open(name + ".csv", 'a+')
    reader = csv.reader(completed)
    data = list(reader)

    completedquestions_array = np.array(data).tolist();

    numbers = [0,2,3,4]
    weights = [2,4,10,10]

    for i in range(size):
        while 1 :

            curr_chapter = random.choices(numbers, weights=weights, k=1)[0]
    
            curr_question_number = random.randrange(len(questions[curr_chapter]))
            curr_question = 'chapters/' + str(11 + curr_chapter) + '/' + questions[curr_chapter][curr_question_number]


            if not (curr_question in completedquestions_array):
                completedquestions_array.append(curr_question)
                mytest.append(curr_question)
                completed.write(curr_question + ',')
                new_test.write(curr_question + ',')

                break

    completed.close()
    new_test.close()

elif option == "open":
    name = input("Which test would you like to open?: ")
    
    test = open(name + ".csv", "r")
    reader = csv.reader(test)
    data = list(reader)

    mytest = np.array(data).tolist()[0];
    print(mytest)

#chat code


# Create the main application window
root = tk.Tk()
root.title("Image Frame")
root.attributes('-fullscreen', True)


# Create a scrollable frame
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(main_frame)
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Load and display images in the scrollable frame
for file in mytest:
    try:
        # Open the image and resize it to fit within the frame
        img = Image.open(file)
        img.thumbnail((1400, 1400))  # Resize the image to a max size of 400x400
        img_tk = ImageTk.PhotoImage(img)

        # Create a label to hold the image
        label = ttk.Label(scrollable_frame, image=img_tk)
        label.image = img_tk  # Keep a reference to avoid garbage collection
        label.pack(anchor='center', pady=50)  # Add padding between images
    except Exception as e:
        print(f"Error loading image {file}: {e}")

# Start the Tkinter main loop
root.mainloop()













