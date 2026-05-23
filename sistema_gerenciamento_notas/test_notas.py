import unittest
# Importa as funções do módulo principal para realizar as validações
from gerenciamento_notas import calcular_media, verificar_aprovacao

class TestSistemaNotas(unittest.TestCase):
    """
    Classe de testes unitários para validar o motor de lógica do 
    Sistema de Gerenciamento de Notas Acadêmicas.
    """

    def test_aprovacao_comum_media_limpa(self):
        """
        Testa o comportamento comum: médias normais limpas.
        Garante que um aluno com notas boas seja aprovado e um com notas baixas seja reprovado.
        """
        # Cenário 1: Notas que resultam em média 8.0 (Aprovado com corte padrão 7.0)
        notas_aprovado = [8.0, 7.0, 9.0]
        media_aprovado = calcular_media(notas_aprovado)
        situacao_aprovado = verificar_aprovacao(media_aprovado)
        
        self.assertEqual(media_aprovado, 8.0)
        self.assertEqual(situacao_aprovado, 'Aprovado')

        # Cenário 2: Notas que resultam em média 5.0 (Reprovado com corte padrão 7.0)
        notas_reprovado = [5.0, 4.0, 6.0]
        media_reprovado = calcular_media(notas_reprovado)
        situacao_reprovado = verificar_aprovacao(media_reprovado)
        
        self.assertEqual(media_reprovado, 5.0)
        self.assertEqual(situacao_reprovado, 'Reprovado')

    def test_lista_de_notas_totalmente_vazia(self):
        """
        Testa o caso extremo (edge case) de receber uma lista de notas totalmente vazia.
        Garante a estabilidade do sistema contra erros de divisão por zero.
        """
        notas_vazias = []
        media_calculada = calcular_media(notas_vazias)
        situacao_final = verificar_aprovacao(media_calculada)
        
        # O sistema deve retornar 0.0 de média e consequentemente 'Reprovado'
        self.assertEqual(media_calculada, 0.0)
        self.assertEqual(situacao_final, 'Reprovado')

    def test_media_minima_de_corte_igual_a_zero(self):
        """
        Testa a estabilidade do sistema ao configurar a variável de média mínima
        com o valor limite zero (0.0). Qualquer média >= 0 deve ser aprovada.
        """
        # Mesmo com notas baixas (média 4.0), se o corte institucional for 0.0, deve aprovar
        notas_baixas = [3.0, 5.0, 4.0]
        media_calculada = calcular_media(notas_baixas)
        situacao_final = verificar_aprovacao(media_calculada, media_minima=0.0)
        
        self.assertEqual(media_calculada, 4.0)
        self.assertEqual(situacao_final, 'Aprovado')

if __name__ == '__main__':
    unittest.main()
