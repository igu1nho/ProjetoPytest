<h1 align="center"> Pytest💻 </h1>

- [Projeto](#o-projeto-)
- [Equipe](#equipe)
- [Guia de Instalação](#instalação-)
   - [Pré-requisitos](#pré-requisitos)
   - [Versão e atualização do PIP](#versão-e-atualização)
   - [Instalação do Pytest](#instalando-o-pytest)
   - [Clone](#clonar-o-projeto)
- [Testes](#testes-%EF%B8%8F%EF%B8%8F)

# O Projeto 📈
Projeto da matéria de Engenharia de Software (C214), ministrada pelo professor **Chris Lima**. Tem como um seminário relacionado a uma framework em específico no nosso caso o Pytest.<br>
Apresentaremos alguns testes de unidade feitos com a ferramenta de testes, ***Pytest***. Para isso desenvolvemos cada um um problema em ***python***, que será testado.
Igor(Horário de monitoria),
Lucas(Quantidade de títulos de um time de futebol) e
Rodrigo(General de um game).

## Equipe
| ![Igor Luiz Rodrigues](https://avatars.githubusercontent.com/u/89806466?s=400&u=e8107d3d169b3775f289e49470b097b45d778d68&v=4) | ![Lucas Henrique](https://avatars.githubusercontent.com/u/89883718?v=4) | ![Rodrigo Braga](https://avatars.githubusercontent.com/u/77506652?v=4)|
| --- | --- | --- |
| [Igor Luiz Rodrigues](https://github.com/igu1nho) | [Lucas Henrique](https://github.com/LucasHGraciano) | [Rodrigo Braga](https://github.com/Zenks1) |


## Instalação ⚙💻
Se você gostaria de saber um pouco mais das informações sobre essa ferramenta de teste, você pode acessar a documentação oficial do <a href="https://docs.pytest.org/en/stable/index.html">Pytest</a>.<br> O processo de instalação é simples, basta seguir o passo a passo abaixo:

### Pré-requisitos
Para instalar o Pytest é necessário ter em sua máquina o Python instalado <a href="https://www.python.org/">python.org</a>

### ⚠️ Alguns IDE's como o <a href="https://www.jetbrains.com/pt-br/pycharm/">PyCharm</a> e o <a href="https://www.code.visualstudio.com/ ">VScode</a> já possuem o PIP integrado, ⚠️<br>

Abra um console com permissão de administrador no seu computador.
Após aberto, siga os seguintes passos:

### Versão e atualização
- Para verificar se instalou corretamente e saber sua versão, rode o seguinte comando:
```bash
pip --version
```

- Para atualizar sua versão do PIP, rode o seguinte comando:
```bash
python -m pip install --upgrade pip
```

### Instalando o Pytest
- 1º Com um simples comando você já instala o Pytest:
```bash
pip install pytest
```

- 2º Para saber a versão do Pytest, também é simples:
```bash
pytest --version
```

### Clonando o projeto
Agora é hora de baixar o projeto e poder testar um pouco dessa ferramenta de testes.
- Com o terminal ainda aberto, navegue até a pasta onde deseja salvar o projeto e cole o seguinte comando:
```bash
git clone https://github.com/igu1nho/test_projeto/
```

**Pronto, tudo configurado! Agora é só escolher o seu IDE preferido e _Let's code with us_!**

## Testes ☑️✖️
### Para realização dos testes, 3 comandos podem ser feitos:
- 1º (Rodar todos os arquivos de teste):
```bash
pytest
```

- 2º (Rodar um arquivo de teste específico):
```bash
pytest nome_do_arquivo.py
```

- 3º (Rodar os testes, até encontrar um erro):
```bash
pytest -x ou pytest nome_do_arquivo.py -x
```

## Arquivos :open_file_folder:
<!--ts-->
  * :file_folder: atendimento
    * :file_folder: test
        * :page_facing_up: __init__.py
        * :page_facing_up: [test_monitoria.py](#teste-atendimento)
     * :page_facing_up: __init__.py
     * :page_facing_up: [monitoria.py](#atendimento)
<!--te-->

<!--ts-->
  * :file_folder: general
    * :file_folder: test
        * :page_facing_up: __init__.py
        * :page_facing_up: [test_generalgame.py](#teste-generalgame)
     * :page_facing_up: __init__.py
     * :page_facing_up: [generalgame.py](#generalgame)
<!--te-->

<!--ts-->
  * :file_folder: time
    * :file_folder: test
        * :page_facing_up: __init__.py
        * :page_facing_up: [test_timefutebol.py](#teste-timefutebol)
     * :page_facing_up: __init__.py
     * :page_facing_up: [timefutebol.py](#timefutebol)
<!--te-->

## Monitor
![image](https://camo.githubusercontent.com/1d2b281547283b669bbf24e572c9cad285a931506446b657206c410df5dac1fc/68747470733a2f2f692e696d6775722e636f6d2f7650457051416a2e706e67)

## Teste Monitor
![image](https://camo.githubusercontent.com/dc6c0d473b4a68e866d54a8699d53ca49b5e435ab5c19fa48a271862a3d0f7ee/68747470733a2f2f692e696d6775722e636f6d2f6b5654746658352e706e67)

## Time de Futebol
![image](https://camo.githubusercontent.com/fb339bb1aa7ab7cf33ef0465966ff37156a40f4287f0a150716774a9feb787d1/68747470733a2f2f692e696d6775722e636f6d2f327031555155632e706e67)

## Teste Time de Futebol
![image](https://camo.githubusercontent.com/fae8dcfde795b867dee802b4ef51056c9e8f466aeab6226ad60724cdfc3aed80/68747470733a2f2f692e696d6775722e636f6d2f706c596f4849642e706e67)

## Game
![image](https://camo.githubusercontent.com/d95e92db9233b6d0408276c3fda7ee3518417f5beeedbf7b3ad0b647a7c0f036/68747470733a2f2f692e696d6775722e636f6d2f634175426454652e706e67)

## Teste Game
![image](https://camo.githubusercontent.com/0729c833cbf5523efa886ca42f708e9ab8998a52bd7ca1731fdf58d8462414d8/68747470733a2f2f692e696d6775722e636f6d2f70636950306b412e706e67)
