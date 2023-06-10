NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a parti de uma tonica e uma tonalidade.

    Parameters:
        tonica: Nota que será a tónica da escala.
        tonalidade: Tonalidade da escala.

    Raises:
        ValueError: Tonica ou nota inxestente
        KeyError: tonalidade inexistente ou nao disponivel.

    Returns:
        Um dicionario com as notas, escals e graus precessados com base nos parametros passados.

    Examples:

        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        intevalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS.index(tonica)
    except ValueError:
        raise ValueError('Nota inexistente, tente uma dessas {}'.format(NOTAS))
    except KeyError:
        raise KeyError(
            'Tonalidade Inexistente ou não disponivel, '
            'tente uma destas {}'.format(list(ESCALAS.keys()))
        )

    temp = []
    for intervalo in intevalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
