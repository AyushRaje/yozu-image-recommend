from embedding_generator import EmbeddingGenerator

def generate_embeddings_for_entities(image_documents):
    embedding_generator = EmbeddingGenerator()
    all_texts = []
    index_to_doc_map = []

    for doc in image_documents:
        # Add the image title
        all_texts.append(doc['image_title'])
        index_to_doc_map.append(doc)

        # Add each alias entity
        for alias in doc['alias_entities']:
            all_texts.append(alias)
            index_to_doc_map.append(doc)

    embeddings = embedding_generator.generate(all_texts)
    return embeddings, index_to_doc_map


# # Assuming `image_documents` is a list of your MongoDB documents
# image_documents = list(collection.find())
# embeddings, index_to_doc_map = generate_embeddings_for_entities(image_documents)

# # Save embeddings and index to doc map to a .npy file
# np.save('embeddings_with_entities.npy', embeddings)
# with open('index_to_doc_map.pkl', 'wb') as f:
#     pickle.dump(index_to_doc_map, f)