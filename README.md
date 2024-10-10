# Sistema de Blockchain

## Pré-Requisitos

Antes de executar a aplicação, você precisará dos seguintes pré-requisitos:

- Python 3.6 ou superior
- Biblioteca `hashlib` (já incluída no Python padrão)
- Biblioteca `time` (já incluída no Python padrão)

## Configuração Inicial

### Clone o repositório:
`git clone https://github.com/Aryosmar/Blockchain---python.git`

**Navegue até o diretório do projeto:**
`cd "Blockchain em python"`

## Executando a Aplicação

Para executar a aplicação, siga os passos abaixo:

## **No Terminal:**

Navegue até o diretório onde o arquivo `main.py` está localizado.

Execute o arquivo `main.py`: 

`python main.py`

## No Visual Studio Code

1. **Abra o Visual Studio Code.**

2. **Abra o diretório do projeto:**
   - Vá em `File > Open Folder...` e selecione a pasta "Blockchain em python".

3. **Abra o terminal integrado:**
   - Vá em `Terminal > New Terminal`. O terminal será aberto na parte inferior do VS Code, no diretório do projeto.

4. **Execute o arquivo `main.py`:**
   - Você pode executar o script diretamente no terminal com o comando:
   `python main.py`


Alternativamente, você pode executar o script usando o recurso de execução de código do VS Code:

- Clique com o botão direito do mouse no arquivo `main.py` no Explorer e selecione **Run Python File in Terminal**.
- Também é possível usar a opção **Run Python File**, que executará o arquivo diretamente.

Isso iniciará a aplicação e exibirá a cadeia de blocos atual.

## Explicação do Código

### Estrutura do Projeto

O projeto é estruturado em cinco arquivos principais:

1. **transacao.py:** Define a classe `Transacao`, que representa uma transação entre usuários.
2. **bloco.py:** Define a classe `Bloco`, que representa um bloco na cadeia de blocos, incluindo a lógica para calcular seu hash.
3. **cadeia_de_blocos.py:** Define a classe `CadeiaDeBlocos`, que gerencia a coleção de blocos e implementa a lógica para adicionar novos blocos e validar a cadeia.
4. **arvore_merkle.py:** Define a classe `ArvoreMerkle`, que organiza e valida transações dentro de um bloco.
5. **main.py:** Executa a aplicação principal, criando transações e adicionando blocos à cadeia.

### Detalhes das Classes

### Classe Transacao

**Atributos:**
- **remetente:** Nome do remetente da transação.
- **destinatario:** Nome do destinatário da transação.
- **valor:** Valor da transação.

**Métodos:**
- `__str__():` Retorna uma representação em string da transação.

### Classe Bloco

**Atributos:**
- **indice:** Índice do bloco na cadeia.
- **transacoes:** Lista de transações incluídas no bloco.
- **timestamp:** Timestamp da criação do bloco.
- **hash_anterior:** Hash do bloco anterior.
- **arvore_merkle:** Instância da árvore de Merkle das transações do bloco.
- **hash_atual:** Hash atual do bloco.

**Métodos:**
- `gerar_hash():` Gera o hash atual do bloco com base nos seus atributos.
- `__str__():` Retorna uma representação em string do bloco.

### Classe CadeiaDeBlocos

**Atributos:**
- **cadeia:** Lista de blocos na cadeia.

**Métodos:**
- `criar_bloco_genesis():` Cria o bloco gênesis da cadeia.
- `obter_ultimo_bloco():` Obtém o último bloco da cadeia.
- `adicionar_bloco(novas_transacoes):` Adiciona um novo bloco à cadeia com as novas transações.
- `validar_integridade():` Valida a integridade da cadeia de blocos.
- `mostrar_cadeia():` Mostra todos os blocos na cadeia.

### Classe ArvoreMerkle

**Descrição:** A árvore de Merkle é uma estrutura de dados que permite organizar e validar transações dentro de um bloco de forma eficiente.

**Atributos:**
- **transacoes:** Lista de transações que serão organizadas na árvore.
- **raiz:** Hash da raiz da árvore de Merkle, que representa todas as transações.

**Métodos:**
- `__init__(self, transacoes):` Construtor que inicializa a árvore de Merkle com as transações e constrói a árvore.
- `construir_arvore(transacoes):` Constrói a árvore de Merkle a partir das transações, calculando os hashes de cada par de transações e subindo até obter o hash da raiz.
- `calcular_hash(data):` Calcula o hash SHA-256 de uma string de dados.



```python
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
```
# Funcionalidades

Este projeto permite a criação de uma blockchain que contém transações, adição de blocos, validação da cadeia e exibição dos detalhes da cadeia de blocos atual.



