# Sistema de Gestão de Estoque - DataCode Solutions 🛠️

Este é um sistema interativo em terminal desenvolvido em Python para gerenciar o estoque de uma oficina mecânica. O projeto foi construído focando em estruturas de dados eficientes e validação robusta de dados para evitar quebras durante a execução.

---

## 🚀 Funcionalidades

* **Visualizar Estoque Atual:** Exibe de forma limpa todos os produtos cadastrados, quantidades e preços formatados.
* **Registrar Entrada:** Permite adicionar novas unidades ao estoque de um produto existente.
* **Registrar Saída (Validação Aninhada):** Deduz itens do estoque com dupla camada de segurança (validação de quantidade positiva e checagem de saldo suficiente).
* **Tratamento de Erros (`Try/Except`):** O sistema impede o fechamento inesperado caso o usuário digite letras no lugar de números.

---

## 🧠 Decisões Técnicas & Conceitos Aplicados

* **Dicionário de Dicionários:** Escolha da estrutura para garantir busca rápida de itens com complexidade de tempo de ordem constante $O(1)$.
* **Programação Defensiva:** Uso de blocos `try-except` para capturar `ValueError` em entradas numéricas.
* **Manipulação de Strings:** Utilização de `.strip()` na coleta de dados para evitar que espaços em branco acidentais causem erros de busca.

---

## 💻 Como Executar o Projeto

Certifique-se de ter o Python 3 instalado em sua máquina. Para iniciar o gerenciador de estoque, execute o comando abaixo no terminal dentro da pasta do projeto:

```bash
python sistema_de_gestao_de_estoque.py
