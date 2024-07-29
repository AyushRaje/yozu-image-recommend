import faiss
import numpy as np
import pandas as pd
import pickle

class FaissSearch():
    def __init__(self, embeddings_path, embedding_generator, index_to_doc_map_path):
        vectors = np.load(embeddings_path)
        self.encoder = embedding_generator
        # self.database = sqlite3.connect(db_file, check_same_thread=False)
        # self.cursor = self.database.cursor()

        with open(index_to_doc_map_path, 'rb') as f:
            self.index_to_doc_map = pickle.load(f)

        vector_dimension = vectors.shape[1]
        self.index = faiss.IndexFlatL2(vector_dimension)
        faiss.normalize_L2(vectors)
        self.index.add(vectors)

    def mongo_search(self,query, k):
        search_vector = self.encoder.embed_query(query)
        _vector = np.array([search_vector])
        faiss.normalize_L2(_vector)
        distances, ann = self.index.search(_vector, k=k)
        results = pd.DataFrame({'distances': distances[0], 'ann': ann[0]}).sort_values(by="distances", ascending=True)

        matched_indices = results['ann'].to_list()
        matched_documents = []
        for index in matched_indices:
            matched_documents.append(self.index_to_doc_map[index])

        image_documents = [doc for doc in matched_documents if 'image_urls/blob' in doc]

        return image_documents