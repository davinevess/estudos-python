# Utilitário de conversão de temperatura para a DataCode Solutions

# Recebe a entrada do usuário como texto (string)
entrada_usuario = input("Digite a temperatura em graus Celsius: ")

# Realiza a conversão explícita (casting) de string para float
# Utilizamos float pois temperaturas podem conter casas decimais
temperatura_celsius = float(entrada_usuario)

# Processamento: Aplicação da fórmula de conversão para Fahrenheit 
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Saída de dados formatada com f-string, limitando a 2 casas decimais
print(f"A temperatura convertida é {temperatura_fahrenheit:.2f} graus Fahrenheit.")