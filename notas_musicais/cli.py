from escalas import escala
from rich.console import Console
from rich.table import Table
from typer import Argument, run

console = Console()
table = Table()


def escalas():
    notas, graus = escala('C', 'maior').values()
    for grau in graus:
        table.add_column(grau)
    table.add_row(*notas)
    console.print(table)


run(escalas)
