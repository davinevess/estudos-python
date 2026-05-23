🚀 Estudos Python

Repositório dedicado aos meus primeiros passos na programação com Python, focado no desenvolvimento de lógica, manipulação de dados, tratamento de exceções e automação de processos funcionais.

📂 Organização do Repositório

Para acessar o código-fonte de cada atividade, basta navegar pelas pastas clicando nos links abaixo:
* 🛠️ [Atividade 1: Conversor de Temperatura](./conversor_temperatura/) — Script focado em manipulação de tipos decimais.
* 🧠 [Atividade 2: Cálculo Fatorial](./calculo_fatorial/) — Implementação utilizando bibliotecas nativas de matemática.
* 📦 [Atividade 3: Sistema de Gestão de Estoque](./sistema_gestao_estoque/) — Aplicação interativa completa com programação defensiva.
* 🎮 [Atividade 4: Jogo da Forca Educativo](./jogo-da-forca/) — Aplicação focada em manipulação de strings, coleções e busca performática.
* 📊 [Atividade 5: Sistema de Gerenciamento de Notas](./sistema_gerenciamento_notas/) — Arquitetura de software com funções modulares e suíte completa de testes unitários automatizados.

---

🛠️ Detalhes das Atividades

### 1. Conversor de Temperatura
* **Objetivo:** Converter graus Celsius para Fahrenheit.
* **Conceitos Aplicados:** Entrada de dados (`input`), manipulação de números decimais (`float`) e formatação de saída de dados.

### 2. Cálculo Fatorial
* **Objetivo:** Calcular o fatorial de um número inteiro entre 1 e 10.
* **Conceitos Aplicados:** Importação de bibliotecas nativas (`math`), tratamento de números inteiros (`int`) e aplicação de Casting para conversão de tipos de dados.

### 3. Sistema de Gestão de Estoque (DataCode Solutions)
* **Objetivo:** Gerenciar o estoque de uma oficina mecânica com funções de visualização, entrada e saída de produtos.
* **Conceitos Aplicados:** Estrutura de dados complexa (Dicionário de Dicionários), controle de fluxo interativo (`while True`), validações aninhadas e Programação Defensiva com tratamento de erros (`try/except`).

### 4. Jogo da Forca Educativo
* **Objetivo:** Criar um jogo interativo no terminal focado no aprendizado e fixação de termos técnicos de programação.
* **Conceitos Aplicados:** Sorteio aleatório (`random.choice`), manipulação de strings (`.join()`, `.strip()`, `.upper()`), modularização com funções de responsabilidade única e uso estratégico de coleções.

### 5. Sistema de Gerenciamento de Notas
* **Objetivo:** Desenvolver o núcleo lógico de um sistema acadêmico para cadastro de estudantes, cálculo de médias aritméticas, relatórios formatados e validação institucional de aprovação.
* **Conceitos Aplicados:** Estrutura de dados em memória (Lista de Dicionários), funções puras de responsabilidade única (SRP), documentação rigorosa com Docstrings (PEP 8) e blindagem contra erros de divisão por zero.

---

🧪 Engenharia de Validação (Testes Automatizados)

A Atividade 5 introduz rotinas de **Garantia de Qualidade (QA)** através do módulo nativo `unittest`, cobrindo cenários críticos de execução:
* **Fluxo Padrão:** Checagem automatizada de limites para aprovação (médias $\ge 7.0$) e reprovação.
* **Casos Extremos (*Edge Cases*):** Validação de estabilidade matemática ao processar listas de notas totalmente vazias.
* **Limites de Fronteira:** Teste de comportamento do operador lógico ao configurar a nota de corte institucional para o valor limite zero (`0.0`).

---

🧠 Competências Desenvolvidas

* **Casting e Conversão:** Entendimento profundo sobre a transformação de strings em tipos numéricos de forma segura.
* **Programação Defensiva:** Domínio na captura de exceções (`ValueError`) e validações de tamanho/tipo de dados de entrada para impedir a quebra de sistemas em produção causadas por ações inesperadas dos usuários.
* **Estruturas de Dados e Performance:** Uso estratégico de dicionários para otimização de buscas e aplicação de Conjuntos (`set`) para garantir a unicidade nativa de elements e buscas eficientes com complexidade em tempo constante $O(1)$.
* **Qualidade e Validação de Software:** Habilidade prática na escrita de testes unitários isolados do código principal, garantindo a imunidade do sistema contra falhas de regressão durante futuras manutenções.
* **Boas Práticas:** Documentação limpa através de Docstrings no padrão de mercado, comentários explicativos detalhados, modularização rigorosa e foco na experiência do usuário (UX) em aplicações via terminal.
