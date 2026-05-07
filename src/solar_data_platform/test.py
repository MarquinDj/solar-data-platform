"""Apenas um teste XD"""


def testar(nome: str) -> str:
    """Função para comunicar o nome do 'testador'"""
    if not nome:
        raise ValueError("Um fantasma está testando :O UI UI UI QUE MEDO")
    return rf"Opa, o teste de {nome} funcionou. \o/"
