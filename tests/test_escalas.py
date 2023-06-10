"""
AAA
arange, act - assets
Arrumar - Agir  Garantir
"""
from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minuscolas():

    # arrumar
    tonica = 'c'
    tonalidade = 'maior'
    # act
    result = escala(tonica, tonalidade)
    # Garantir
    assert result


def test_deve_retornar_um_erro_quando_for_inserido_uma_tonica_que_nao_existe_e_retorna_as_notas_disponiveis():
    tonica = 'K'
    tonalidade = 'maior'
    menssagem_de_erro = 'Nota inexistente, tente uma dessas {}'.format(NOTAS)

    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    assert menssagem_de_erro == error.value.args[0]


def test_deve_retornar_um_erro_quando_for_inserido_uma_tonalidade_inexistente_e_retornar_as_tonalidades():
    tonica = 'A'
    tonalidade = 'tonalidade'
    menssagem__de_erro = (
        'Tonalidade Inexistente ou não disponivel, '
        'tente uma destas {}'.format(list(ESCALAS.keys()))
    )

    with raises(KeyError) as error:
        escala(tonica, tonalidade)
    assert menssagem__de_erro == error.value.args[0]


@mark.parametrize(
    'tonica, esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('B', ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),
    ],
)
def test_deve_return_as_notas_correspondente_a_tonica_informada(
    tonica, esperado
):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado
