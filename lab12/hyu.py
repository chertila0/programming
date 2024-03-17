from appJar import gui

app = gui()

app.addLabelOptionBox('hiy',['fgh','hgf'])


app.go()

if app.getOptionBox('hiy') == 'hgf':
    print('123')
