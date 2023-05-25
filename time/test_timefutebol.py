import pytest
from timefutebol import Time

class TestTime:
    def test_init(self):
        nome = "Barcelona"
        nacionais = 72
        cidade = "Barcelona-ESP"
        
        time = Time(nome, nacionais, cidade)
        
        assert time.nome == nome
        assert time.nacionais == nacionais
        assert time.cidade == cidade