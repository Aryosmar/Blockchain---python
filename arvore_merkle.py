
import hashlib

def calcular_hash(data): 
    return hashlib.sha256(data.encode()).hexdigest()

class ArvoreMerkle:
    def __init__(self, transacoes):
        self.transacoes = transacoes
        self.raiz = self.construir_arvore(transacoes)

    def construir_arvore(self, transacoes):
        if len(transacoes) == 0:
            return ''
        # Calcular os hashes das transações
        hashes = [calcular_hash(str(transacao)) for transacao in transacoes]

        # Construir a árvore até obter a raiz
        while len(hashes) > 1:
            if len(hashes) % 2 != 0:  # Se o número de hashes é ímpar, duplicamos o último
                hashes.append(hashes[-1])
            # Agrupar e calcular os hashes dos pares
            hashes = [calcular_hash(hashes[i] + hashes[i + 1]) for i in range(0, len(hashes), 2)]

        return hashes[0]  # Retornar o hash raiz
