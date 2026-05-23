"""
Sistema de Gerenciamento de Notas
Módulo Principal
Disciplina: Programação de Computadores - Experiência Prática IV

Este sistema gerencia o cadastro de estudantes, calcula médias aritméticas,
avalia a situação de aprovação institucional e gera relatórios consolidados.
"""

# 1. Definição da Estrutura de Dados (Banco de dados em memória)
estudantes_db = []


# 2. Funções de Cálculo e Regras Institucionais
def calcular_media(notas: list[float]) -> float:
    """
    Calcula a média aritmética de uma lista de notas.

    Garante o processamento correto dos dados numéricos e faz o tratamento
    de casos extremos para evitar erros de divisão por zero caso a lista
    esteja vazia.

    Args:
        notas (list[float]): Uma lista contendo as notas do estudante em formato float.

    Returns:
        float: A média aritmética das notas. Retorna 0.0 se a lista estiver vazia.
    """
    if not notas:
        return 0.0
    
    return sum(notas) / len(notas)


def verificar_aprovacao(media: float, media_minima: float = 7.0) -> str:
    """
    Avalia a situação acadêmica do estudante com base na média obtida.

    Compara a média calculada com o critério mínimo de corte da instituição.

    Args:
        media (float): A média final calculada do estudante.
        media_minima (float, optional): A nota mínima exigida para aprovação. 
            O valor padrão é 7.0.

    Returns:
        str: 'Aprovado' se a média for maior ou igual à média mínima, 
            ou 'Reprovado' caso contrário.
    """
    if media >= media_minima:
        return 'Aprovado'
    
    return 'Reprovado'


# 3. Geração de Relatório de Desempenho
def gerar_relatorio(alunos: list[dict]) -> None:
    """
    Gera e exibe no terminal um relatório formatado com o desempenho acadêmico.
    
    A função percorre a lista de estudantes, calcula a média e define a situação
    de cada um utilizando as funções lógicas previamente implementadas.
    """
    if not alunos:
        print("\n--- NENHUM ESTUDANTE CADASTRADO NO SISTEMA ---")
        return

    print(f"\n{'NOME':<25} | {'MÉDIA':<6} | {'SITUAÇÃO':<10}")
    print("-" * 49)

    for estudante in alunos:
        nome = estudante["nome"]
        notas = estudante["notas"]
        
        media = calcular_media(notas)
        situacao = verificar_aprovacao(media)
        
        print(f"{nome:<25} | {media:<6.2f} | {situacao:<10}")
