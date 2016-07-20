from Tkinter import *

root = Tk()
root.geometry("800x700+0+0")

# backGroundCanvas  = Canvas(root, bg = "white", width = 800, height = 600)
# backGroundCanvas.focus_set()
# backGroundCanvas.pack()

scoreLabel = Label(root, text = "foo bar baz quux", bg = "red")
scoreLabel.place(x = 400, y = 600)

root.mainloop()