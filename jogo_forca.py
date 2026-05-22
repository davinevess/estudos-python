"""
Jogo da Forca Educativo - Sistema de Aprendizado Interativo.

Este programa implementa um jogo da forca simplificado no terminal, projetado
para fixação de termos e lógica de programação.

Estruturas de dados principais utilizadas:
- list: Para o banco de palavras e para a máscara da palavra adivinhada.
- set: Para o controle de unicidade das letras já tentadas pelo jogador.
"""

import random

# Banco de palavras global utilizando caixa alta para padronização
BANCO_PALAVRAS = ["PYTHON", "ALGORITMO", "LOGICA", "COMPUTADOR", "ESTRUTURA"]


def inicializar_jogo():
    """
    Prepara o estado inicial necessário para o início de uma nova partida.

    Sorteia uma palavra secreta do banco de dados e gera a representação
    mascarada preenchida com lacunas ('_').

    Retorna:
        tuple: Uma tupla contendo a palavra_secreta (str) e a lista
               palavra_oculta (list de str).
    """
    palavra_secreta = random.choice(BANCO_PALAVRAS)
    palavra_oculta = ["_"] * len(palavra_secreta)
    return palavra_secreta, palavra_oculta


def processar_tentativa(letra, palavra_secreta, palavra_oculta):
    """
    Processa a jogada atual, verificando se a letra existe na palavra secreta.

    Caso a letra seja encontrada, a estrutura da palavra_oculta é atualizada
    com o caractere revelado nas posições correspondentes.

    Argumentos:
        letra (str): O caractere fornecido pelo jogador.
        palavra_secreta (str): A palavra alvo da rodada.
        palavra_oculta (list): A lista de lacunas que representa o progresso.

    Retorna:
        bool: True se o jogador acertou a letra, False caso contrário.
    """
    acertou = False

    # Varredura linear usando índices para atualizar a lista mutável
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            palavra_oculta[i] = letra
            acertou = True

    return acertou


def jogar():
    """
    Função principal que gerencia o fluxo de controle, a interface de texto
    e as regras de negócio do ciclo de vida do jogo.
    """
    palavra_secreta, palavra_oculta = inicializar_jogo()
    erros_cometidos = 0
    TENTATIVAS_MAXIMAS = 6

    # ==========================================================================
    # JUSTIFICATIVA TÉCNICA DA ESTRUTURA DE DADOS (CRITÉRIOS DE AVALIAÇÃO)
    # Escolha por Conjunto (Set) em vez de Lista:
    # 1. Unicidade Nativa: O set proíbe duplicatas automaticamente, impedindo
    #    redundâncias sem necessidade de condicionais 'if' extras.
    # 2. Busca O(1): A checagem de existência ('letra in letras_tentadas') é
    #    feita em tempo constante por tabelas hash, enquanto na lista seria O(n).
    # ==========================================================================
    letras_tentadas = set()

    print("=" * 50)
    print("      BEM-VINDO AO JOGO DA FORCA EDUCATIVO")
    print("=" * 50)

    # Laço de repetição principal controlado por estado composto
    while erros_cometidos < TENTATIVAS_MAXIMAS and "_" in palavra_oculta:
        print("\n" + "-" * 30)
        # Exibição formatada das lacunas utilizando o método .join()
        print(f"Palavra atual: {' '.join(palavra_oculta)}")
        # Exibição do histórico ordenado de letras a partir do conjunto
        print(f"Letras já tentadas: {', '.join(sorted(letras_tentadas)) if letras_tentadas else 'Nenhuma'}")
        print(f"Tentativas restantes: {TENTATIVAS_MAXIMAS - erros_cometidos}")
        print("-" * 30)

        # Coleta de entrada e tratamento defensivo (caixa alta e sem espaços)
        letra = input("Digite uma letra: ").strip().upper()

        # Validação de entrada: garante que o usuário digitou apenas uma letra válida
        if len(letra) != 1 or not letra.isalpha():
            print("\n[i] Entrada inválida. Por favor, digite apenas uma letra.")
            continue

        # Tratamento de duplicidade utilizando a propriedade de busca do set
        if letra in letras_tentadas:
            print(f"\n[i] Você já tentou a letra '{letra}'. Escolha outra letra.")
            continue

        # Inserção segura no conjunto de tentativas
        letras_tentadas.add(letra)

        # Processamento e ramificação de regras de negócio
        if processar_tentativa(letra, palavra_secreta, palavra_oculta):
            print(f"\n[+] Muito bem! A letra '{letra}' faz parte da palavra secreta.")
        else:
            erros_cometidos += 1
            print(f"\n[-] Que pena! A letra '{letra}' não está na palavra secreta.")

    # Verificação final e encerramento fora do laço principal
    if "_" not in palavra_oculta:
        print("\n" + "=" * 50)
        print(f" PARABÉNS! Você descobriu a palavra: {palavra_secreta}!")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print(" GAME OVER! Suas tentativas acabaram.")
        print(f" A palavra secreta era: {palavra_secreta}.")
        print("=" * 50)


# Ponto de entrada padrão para execução do script em Python
if __name__ == "__main__":
    jogar()
