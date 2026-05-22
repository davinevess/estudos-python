# 🎮 Jogo da Forca Educativo

Este projeto consiste em um **Jogo da Forca Interativo** desenvolvido em Python para execução diretamente no terminal. O principal objetivo do programa é servir como uma ferramenta pedagógica para a fixação de termos técnicos, conceitos e lógica de programação.

---

## 🛠️ Tecnologias e Conceitos Utilizados

O desenvolvimento deste software foi focado na aplicação de boas práticas de programação e na escolha eficiente de estruturas de dados básicas, tais como:

* **Listas (`list`):** Utilizadas para a manipulação do banco de palavras globais e para a construção da máscara visual da palavra oculta (atualizada dinamicamente a cada acerto).
* **Conjuntos (`set`):** Utilizados para armazenar o histórico de letras já tentadas pelo usuário.
* **Modularização:** O código foi estruturado de forma limpa através de funções com responsabilidades bem definidas (`inicializar_jogo`, `processar_tentativa` e `jogar`).
* **Validação Defensiva:** Implementação de regras para impedir que o usuário insira strings vazias, caracteres numéricos ou tente adivinhar a palavra inteira de uma só vez, evitando o desperdício de tentativas de forma injusta.

---

## 🧠 Justificativa Técnico da Estrutura de Dados

Um dos critérios de avaliação deste projeto foi a escolha fundamentada das estruturas de dados. A opção pela utilização de um **Conjunto (`set`)** para gerenciar as letras tentadas em detrimento de uma lista comum foi baseada em dois pilares:

1. **Unicidade Nativa:** O `set` proíbe automaticamente a existência de elementos duplicados. Isso elimina a necessidade de condicionais `if` adicionais para validar se a letra já existia na coleção antes de inseri-la.
2. **Eficiência de Busca - Complexidade $O(1)$:** A checagem de existência (`if letra in letras_tentadas`) é processada em tempo constante através de tabelas *hash*. Em uma lista convencional, essa operação exigiria uma varredura linear com complexidade $O(n)$, tornando o programa menos eficiente à medida que o volume de dados cresce.

---

## 🚀 Como Executar o Projeto

Certifique-se de ter o Python 3 instalado em sua máquina. Para iniciar o jogo, execute o comando abaixo no terminal:

```bash
python jogo_forca.py
