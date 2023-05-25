import pytest
from monitoria import Monitor

class TestMonitor:
    def test_init(self):
        nome = "Igor Luiz"
        dia_horario = "Segunda-feira, 10:00"
        local = "Sala 16-1"
        
        monitor = Monitor(nome, dia_horario, local)
        
        assert monitor.nome == nome
        assert monitor.dia_horario == dia_horario
        assert monitor.local == local