from escalas import escala
from rich.console import Console
from rich.table import Table
from typer import Argument, run
from typing_extensions import Annotated

console = Console()


def escalas(
    tonica: Annotated[str, Argument(help='tonica da escala')] = 'C',
    tonalidade: Annotated[
        str, Argument(help='Tonalidade da escala')
    ] = 'maior',
):
    table = Table()
    notas, graus = escala(tonica, tonalidade).values()
    for grau in graus:
        table.add_column(grau)
    table.add_row(*notas)
    console.print(table)


run(escalas)
