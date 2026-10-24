import ollama

def gerar_embeddings_exemplo():
    
    texto = "Inteligência Artificial e Processamento de Linguagem Natural são áreas fascinantes."
    
    print(f"Texto original: '{texto}'\n")
    print("Conectando ao Ollama e gerando embeddings com o modelo 'nomic-embed-text'...")
    
    # Chamada para gerar o embedding usando o modelo baixado
    resposta = ollama.embeddings(
        model='nomic-embed-text',
        prompt=texto
    )
    
    vetor = resposta['embedding']
    
    # Exibindo um sumário do vetor de embeddings
    print("\n--- Resultados ---")
    print(f"Dimensão/Tamanho do vetor: {len(vetor)}")
    print(f"Primeiros 5 valores do vetor: {vetor[:5]}")

if __name__ == "__main__":
    gerar_embeddings_exemplo()