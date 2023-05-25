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
Apresentaremos alguns testes de unidade feitos com a ferramenta de testes, ***Pytest***. Para isso desenvolvemos cada um um problema em ***python***.
Igor(Horário de monitoria)
Lucas(Quantidade de títulos de um time de futebol)
Rodrigo()

## Equipe
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/89806466?s=400&u=e8107d3d169b3775f289e49470b097b45d778d68&v=4" width="100px;" alt="Igor Luiz Rodrigues"/></td>
    
    <td align="center"><img src="https://avatars.githubusercontent.com/u/89883718?v=4" width="100px;" alt="Lucas Henrique"/></td>
    
    <td align="center"><img src="https://avatars.githubusercontent.com/u/77506652?v=4" width="100px;" alt="Rodrigo Braga"/></td>
    
    <td align="center"><img src="URL_DA_IMAGEM" width="100px;" alt="NOME_DO_INTEGRANTE"/></td> <!-- Adicione esta linha para a terceira imagem -->
  </tr>
</table>

   

## Instalação ⚙💻
Se você gostaria de saber um pouco mais das informações sobre essa ferramenta de teste, você pode acessar a documentação oficial do <a href="https://docs.pytest.org/en/stable/index.html">Pytest</a>.<br> , O processo de instalação é simples, basta seguir o passo a passo abaixo:

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
![image]([https://imgur.com/6FSDgDf](https://i.imgur.com/6FSDgDf.png))

## Teste Monitor
![image](https://imgur.com/i0IeGbF)

## Time de Futebol
![image](https://imgur.com/2p1UQUc)

## Teste Time de Futebol
![image](https://imgur.com/plYoHId)

## Time de Futebol
![image](https://user-images.githubusercontent.com/73140691/139708100-b411dcec-753f-46ff-931c-5f01a6965640.png)

## Teste Time de Futebol
![image](https://user-images.githubusercontent.com/73140691/139708280-9f5f391f-7802-4c33-a0ad-a0faf8abd680.png)
