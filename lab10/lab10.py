import typer
from papka import lab8, lab77, lab9

app = typer.Typer()

@app.command()
def laba8(operation: str, a: int, b: int):
    calc = lab8.make_calc(operation, a)
    print(calc(b))


@app.command()
def laba7(lst: str):
    print(lab77.rec_count(eval(lst)))
    


@app.command()
def laba9(minn: int, maxx: int): 
    print(lab9.rand_num(minn, maxx))


if __name__ == "__main__":
    app()


