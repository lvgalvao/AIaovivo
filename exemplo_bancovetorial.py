import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="expansao_zapflow")

collection.upsert(
    documents=[
        "A Zapflow vai abrir escritório no Brasil.",
        "A Zapflow vai abrir escritório na França.",
        "A Zapflow vai abrir escritório no Japão.",
        "A Zapflow vai abrir escritório na Alemanha.",
        "A Zapflow vai abrir escritório no Canadá.",
        "A Zapflow vai abrir escritório na Austrália.",
        "A Zapflow vai abrir escritório na Itália.",
        "A Zapflow vai abrir escritório na Argentina.",
        "A Zapflow vai abrir escritório na Espanha.",
        "A Zapflow vai abrir escritório na Rússia."
    ],
    ids=["pais1", "pais2", "pais3", "pais4", "pais5", "pais6", "pais7", "pais8", "pais9", "pais10"]
)

resultado = collection.query(
    query_texts=["The Zapflow will have an office at Osaka?"],
    n_results=3
)

print(resultado)