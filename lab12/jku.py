from appJar import gui

app = gui()

def open_window1():
    app.startSubWindow("Window 1", modal=True)
    app.addLabel("l1", "This is Window 1")
    app.stopSubWindow()

def open_window2():
    app.startSubWindow("Window 2", modal=True)
    app.addLabel("l2", "This is Window 2")
    app.stopSubWindow()

app.addButton("Open Window 1", open_window1)
app.addButton("Open Window 2", open_window2)

app.go()