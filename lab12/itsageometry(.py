from appJar import gui
from rectangle import rectangle as rect
from trapezoid import trapezoid as trap
from triangle import triangle as tri

app = gui()
app.addLabel("Привет! Какая фигура тебе больше всего нравится?")

def press(Button):
    if Button == "Никакая не нравится":
        print("Ну ты и писька")
    elif Button == "Эчпочмак":
        print("Ура эчпочмак!")
    elif Button == "Квадратиш":
        print("Ура квадратиш!")
    elif Button == "Совок":
        print("Ура совок!")
app.addButtons(["Никакая не нравится", "Эчпочмак", "Квадратиш", "Совок"], press)
app.addAppJarMenu()
app.go()