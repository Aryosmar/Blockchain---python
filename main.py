# main.py

from cadeia_de_blocos import CadeiaDeBlocos
from transacao import Transacao

if __name__ == "__main__":
    minha_cadeia = CadeiaDeBlocos()

    # Criar algumas transações
    transacao1 = Transacao("Alice", "Bob", 50)
    transacao2 = Transacao("Bob", "Carlos", 20)
    transacao3 = Transacao("Carlos", "Alice", 10)

    # Adicionar blocos com transações
    minha_cadeia.adicionar_bloco([transacao1, transacao2])
    minha_cadeia.adicionar_bloco([transacao3])

    # Mostrar a cadeia de blocos
    print("\nCadeia de Blocos:")
    minha_cadeia.mostrar_cadeia()

    # Validar a integridade da blockchain
    if minha_cadeia.validar_integridade():
        print("\nCadeia de blocos é válida.")
    else:
        print("\nCadeia de blocos é inválida!")
