import pytest
from generalgame import Game

class TestGame:
    def test_init(self):
        nome = "Elden Ring"
        indie = False
        genero = "Soulslike, RPG, Open World"
        goty = True
        
        game = Game(nome, indie, genero, goty)
        
        assert game.nome == nome
        assert game.indie == indie
        assert game.genero == genero
        assert game.goty == goty