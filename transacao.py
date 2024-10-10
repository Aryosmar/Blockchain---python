# transacao.py

class Transacao:
    def __init__(self, remetente, destinatario, valor):
        self.remetente = remetente
        self.destinatario = destinatario
        self.valor = valor

    def __str__(self):
        return f"{self.remetente} envia {self.valor} para {self.destinatario}"
