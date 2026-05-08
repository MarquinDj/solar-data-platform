"""Teste que testa o teste"""

import socket

import pytest

from solar_data_platform.test import testar


@pytest.mark.unit
def test_o_teste_retorna_o_testador() -> None:
    assert testar("Maguinho") == r"Opa, o teste de Maguinho funcionou. \o/"


@pytest.mark.unit
def test_o_teste_com_fantasma() -> None:
    with pytest.raises(ValueError, match="Um fantasma está testando :O UI UI UI QUE MEDO"):
        testar("")


@pytest.mark.requires_internet
def test_internet() -> None:
    socket.setdefaulttimeout(3)
    socket.create_connection(("8.8.8.8", 53))
