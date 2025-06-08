# 📚 Gerenciador de Bibioteca de Livros

Um projeto open-source elegante para gerenciar um sistema de biblioteca com registro de livros e leitores, empréstimos e devoluções.

---

## Sobre o Projeto

O Gerenciador de Livros permite que você:
- Gerencie livros, incluindo status de disponibilidade.
- Registre leitores com IDs únicos.
- Acompanhe empréstimos e devoluções de livros com controle de datas.
- Pesquise e adicione livros via integração com a API OpenLibrary.
- Salve e carregue dados a partir de arquivos JSON.
- Utilize através de uma interface de linha de comando (CLI) ou uma interface gráfica moderna (GUI) construída com Tkinter.

---

## Versão do Python

Este projeto é compatível com **Python 3.10+**.  

---

## Requisitos

Instale as dependências com:

```bash
pip install -r requirements.txt
```

Dependências:
- `requests==2.32.3` — Para acesso à API OpenLibrary.
- `readkeys==1.0.2` — Para melhor manuseio de entrada de teclas no terminal.

---

## Estrutura do Projeto

| Arquivo              | Descrição                                   |
|----------------------|---------------------------------------------|
| `main.py`            | Interface CLI para terminal                 |
| `gui.py`             | Interface gráfica moderna usando Tkinter    |
| `gestorlivros.py`    | Gerenciador de livros, empréstimos e devoluções |
| `gestorLeitor.py`    | Gerenciador de leitores                     |
| `livro.py`, `leitor.py`, `emprestimo.py` | Modelos de dados              |
| `terminal.py`        | Utilitários para terminal                   |
| Arquivos JSON        | Persistência de dados: `livros.json`, `leitores.json`, `emprestimos.json`, `devolucoes.json` |

---

## Uso

- Execute a interface de terminal:

  ```bash
  python main.py
  ```

- Execute a interface gráfica:

  ```bash
  python gui.py
  ```

---

## Contribuição

Contribuições são bem-vindas! Você pode:
- Reportar bugs via Issues.
- Sugerir melhorias.
- Enviar Pull Requests seguindo o estilo de codificação do projeto.

---

## Licença

Licenciado sob os termos especificados no arquivo `LICENSE`.

---

## 🎉 Emojis Gitmoji Usados em Commits

| Emoji | Código               | Significado                                   |
|-------|----------------------|-----------------------------------------------|
| ✨    | `:sparkles:`         | Introduzir novas funcionalidades ou melhorias  |
| 🐛    | `:bug:`              | Corrigir um bug ou erro no código             |
| 📝    | `:memo:`             | Adicionar ou atualizar documentação            |
| 🚀    | `:rocket:`           | Implantar ou liberar alterações                |
| 🎨    | `:art:`              | Melhorar a estrutura ou formato do código     |
| ⚡    | `:zap:`              | Melhorar o desempenho                          |
| 🔥    | `:fire:`             | Remover código ou arquivos                     |
| 🎉    | `:tada:`             | Criação de uma nova versão ou lançamento      |
| 🚧    | `:construction:`     | Work in progress                              |
| ♻️    | `:recycle:`          | Refatorar código ou melhorar a estrutura      |
| ➕    | `:heavy_plus_sign:`  | Adicionar uma nova dependência                |
| 🚚    | `:truck:`            | Renomear                                      |

---