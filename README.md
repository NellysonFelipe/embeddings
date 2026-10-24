# Geração de Embeddings com Ollama e Python

Este projeto demonstra a instalação local do Ollama e a geração de vetores de embeddings a partir de um texto simples utilizando Python.

## Pré-requisitos
- Python 3.8 ou superior instalado.
- [Ollama](https://ollama.com/) instalado e rodando localmente.

## Instruções para Reprodução

1. **Clone este repositório:**
   ```bash
   git clone  https://github.com/NellysonFelipe/embeddings.git
2. Instale as dependências:

pip install -r requirements.txt

Garanta que o Ollama está ativo e com o modelo baixado:
No seu terminal, certifique-se de que o modelo de embeddings está disponível:

3. No seu terminal, certifique-se de que o modelo de embeddings está disponível
ollama pull nomic-embed-text

4. Execute o script

python gerar_embeddings.py
