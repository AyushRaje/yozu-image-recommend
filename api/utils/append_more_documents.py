import pickle
import numpy as np
from create_new_embeddings import generate_embeddings_for_entities


def append_new_documents(existing_embeddings_path, existing_index_map_path, new_documents):
    # Load existing embeddings and index map
    existing_embeddings = np.load(existing_embeddings_path)
    with open(existing_index_map_path, 'rb') as f:
        existing_index_map = pickle.load(f)
    
    # Generate new embeddings and index map for the new documents
    new_embeddings, new_index_map = generate_embeddings_for_entities(new_documents)

    # Append new embeddings to existing embeddings
    updated_embeddings = np.vstack((existing_embeddings, new_embeddings))
    
    # Update the index map
    updated_index_map = existing_index_map + new_index_map

    # Save the updated embeddings and index map
    np.save(existing_embeddings_path, updated_embeddings)
    with open(existing_index_map_path, 'wb') as f:
        pickle.dump(updated_index_map, f)

    return updated_embeddings, updated_index_map

if __name__=='__main__':
    pass

    # # Assuming `new_image_documents` is a list of your new MongoDB documents
    # new_image_documents = list(collection.find())

    # # Paths to the existing embeddings and index map
    # existing_embeddings_path = 'embeddings_with_entities.npy'
    # existing_index_map_path = 'index_to_doc_map.pkl'

    # # Append new documents to the existing embeddings and index map
    # updated_embeddings, updated_index_map = append_new_documents(existing_embeddings_path, existing_index_map_path, new_image_documents)