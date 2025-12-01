# Omie - Pops Backend Developer Challenge

Este repositório contém as soluções propostas para o desafio técnico de Backend. O foco das implementações foi garantir performance, escalabilidade e manutenibilidade, seguindo boas práticas de engenharia de software.

## Estrutura das Soluções

### 1. Hierarquia Organizacional (SQL)
* **Arquivo:** `solution_1_hierarchy.sql`
* **Desafio:** Buscar todos os departamentos subordinados (diretos e indiretos) dado um ID, usando apenas SQL.
* **Abordagem:** Utilização de **CTE Recursiva (Common Table Expression)**. Esta é a forma mais performática e padrão (ANSI SQL) para lidar com estruturas de árvore/grafo em bancos relacionais, evitando múltiplos JOINs ou processamento na aplicação.

### 2. API Timeout & Assincronismo
* **Arquivo:** `solution_2_async_api.py`
* **Desafio:** Lidar com um WAF que limita requisições a 30s, quando uma operação leva 35s+.
* **Abordagem:** Implementação do padrão **Asynchronous Request-Reply**.
    * A API recebe a requisição e retorna imediatamente `202 Accepted`.
    * O processamento ocorre em background (Worker).
    * O cliente consulta o resultado via *Polling* em um endpoint de status.

### 3. Design de Software (CSC)
* **Arquivo:** `solution_3_csc_design.py`
* **Desafio:** Projetar um sistema de Centro de Serviços Compartilhados extensível.
* **Abordagem:** Uso de **Design Patterns** e princípios **SOLID**.
    * **Strategy Pattern:** Para encapsular a lógica de cada serviço (Férias, Carro, Viagem), permitindo adicionar novos sem alterar o código base (Open-Closed Principle).
    * **Factory Pattern:** Para instanciar a estratégia correta dinamicamente.

---

## Como Executar e Testar

Para validar as soluções localmente, certifique-se de ter **Python 3** e **SQLite3** instalados em seu ambiente.

### Executando a Solução 1

O arquivo SQL contém a criação da tabela, inserção de dados de exemplo e a consulta recursiva. Utilizamos o modo `:memory:` do SQLite para rodar o script sem criar arquivos físicos.

No terminal, execute:
```bash
sqlite3 :memory: < solution_1_hierarchy.sql
```

### Executando a Solução 2
Este script simula o servidor API e o Worker rodando em threads paralelas, exibindo o fluxo de logs no terminal para contornar o timeout.

No terminal, execute:
```bash
python solution_2_async_api.py
```

### Executando a Solução 3
Este script roda uma bateria de testes automática (função main), simulando a chegada de requisições de diferentes tipos (Férias, Carro, Viagem) para o Centro de Serviços.

No terminal, execute:
```bash
python solution_3_csc_design.py
```

**Autor:** [Gislane Francisco Nunes]