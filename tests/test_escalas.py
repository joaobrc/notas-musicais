"""
AAA
arange, act - assets
Arrumar - Agir  Garantir
"""
from notas_musicais.escalas import escala


def test_escala_deve_funcionar_com_notas_minuscolas():

    # arrumar
    tonica = 'c'
    tonalidade = 'maior'
    # act
    result = escala(tonica, tonalidade)
    # Garantir
    assert result
