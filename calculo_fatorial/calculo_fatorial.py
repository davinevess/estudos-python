import math # Importa a biblioteca para o cálculo de fatorial

# Solicita a entrada de dados do usuário
entrada_usuario = input("Digite um número inteiro entre 1 e 10 para calcular o fatorial: ")

# Realiza a conversão explícita (casting) de string para int para permitir cálculos
# Este comentário explica a transformação do tipo de dado de texto para inteiro.
numero_escolhido = int(entrada_usuario)

# Utiliza o método factorial da biblioteca math
resultado_fatorial = math.factorial(numero_escolhido)

# Exibe o resultado final formatado com f-string
print(f"O fatorial de {numero_escolhido} é {resultado_fatorial}.")
