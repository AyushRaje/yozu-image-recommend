import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

class EmbeddingGenerator():
    def __init__(self, model_name="paraphrase-albert-small-v2"):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def embed_query(self, query, open_ai=False):
        if open_ai:
            return self.openai_embed.embed_sentence(sentence=query)
        return self.model.encode(query)

    def new_embeddings(self, sentences):
        embeddings = self.model.encode(sentences, batch_size=32)  # Process in batches
        embeddings = np.array(embeddings, dtype=np.float32)  # Convert to float32
        return embeddings

    def generate(self, text_data_list):
        # Batch process the embedding generation
        embedding_lists = self.new_embeddings(text_data_list)
        print(f"Generated embeddings shape: {embedding_lists.shape}")
        return embedding_lists


