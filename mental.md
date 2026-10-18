** pyproject.toml **

Serve como um arquivo de configuração e é dividido em 3 seções principais:

[build-system]

- Tabela fortemente recomendada que permite declarar qual 'build backend'* utilizar e quais outras dependências são necessárias para buildar o projeto

*Biblioteca que usa a 'source tree' (código bruto antes de ser enpacotado) e constroi a 'source distribution' (distribuição com os metadados e os arquivos fontes essenciais)

[project]

- Usada para especificar metadados basicos do projeto, dependências, nome...

[tool]

- tabela utilizada para especificar sub-tabelas. EX: [tool.hatch], [tool.black], [tool.mypy] onde cada uma tem sua particularidade.

https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

** uv.lock **

Ao contrário do pyproject.toml, especifica versões exatas que estão instaladas no projeto, servindo como lockfile universal que captura os pacotes que seriam instalados em todos os marcadores python. Deve ir ao git para fornecer um ambiente reproduzível.

** ruff **

A regra F é o Pyflakes (imports não utilizados), erros de lógica, já o E é estilo