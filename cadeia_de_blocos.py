# cadeia_de_blocos.py

from bloco import Bloco

class CadeiaDeBlocos:
    def __init__(self):
        self.cadeia = [self.criar_bloco_genesis()]

    def criar_bloco_genesis(self):
        return Bloco(0, ["Bloco Gênesis"], "0")

    def obter_ultimo_bloco(self):
        return self.cadeia[-1]

    def adicionar_bloco(self, novas_transacoes):
        ultimo_bloco = self.obter_ultimo_bloco()
        novo_bloco = Bloco(len(self.cadeia), novas_transacoes, ultimo_bloco.hash_atual)
        self.cadeia.append(novo_bloco)
        print(f"Bloco adicionado: {novo_bloco}")

    def validar_integridade(self):
        for i in range(1, len(self.cadeia)):
            bloco_atual = self.cadeia[i]
            bloco_anterior = self.cadeia[i - 1]

            # Verificar se o hash do bloco atual é válido
            if bloco_atual.hash_atual != bloco_atual.gerar_hash():
                print(f"Bloco {bloco_atual.indice} foi alterado!")
                return False

            # Verificar se o hash anterior do bloco atual é igual ao hash do bloco anterior
            if bloco_atual.hash_anterior != bloco_anterior.hash_atual:
                print(f"Bloco {bloco_atual.indice} é inválido!")
                return False

        return True

    def mostrar_cadeia(self):
        for bloco in self.cadeia:
            print(bloco)
