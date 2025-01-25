import asyncio
from src.models.managers.pdf_manager import PDFManager
from src.models.managers.pdf_extraction_manager import PDFExtractionManager
from src.models.managers.chunk_manager import ChunkManager
from src.models.managers.embedding_manager import EmbeddingManager
from src.models.managers.vector_store_manager import VectorStoreManager

async def main():
    # 1. File Ingestion: Save a PDF file
    print("Step 1: File Ingestion")
    ingestion_manager = PDFManager()
    pdf_file_path = "./sample.pdf"  # Replace with the path to your test PDF
    file = open(pdf_file_path, "rb")
    file_path = await ingestion_manager.save_file(file)
    print(f"PDF saved at: {file_path}")

    # 2. Text Extraction: Extract text from the PDF
    print("\nStep 2: Text Extraction")
    text_extraction_manager = PDFExtractionManager()
    extracted_text = text_extraction_manager.extract_text(file_path)
    print(f"Extracted Text:\n{extracted_text[:500]}...")  # Print first 500 characters

    # 3. Chunking: Split extracted text into smaller, overlapping chunks
    print("\nStep 3: Chunking")
    chunking_manager = ChunkManager()
    chunks = chunking_manager.chunk_text(extracted_text)
    print(f"Generated {len(chunks)} chunks. Sample:\n{chunks[:3]}")  # Display 3 chunks

    # 4. Embedding Generation: Generate embeddings for text chunks
    print("\nStep 4: Embedding Generation")
    embedding_manager = EmbeddingManager()
    embeddings = embedding_manager.generate_embeddings(chunks)
    print(f"Generated {len(embeddings)} embeddings.")

    # 5. Storing in Pinecone: Save embeddings on the server
    print("\nStep 5: Storing in Pinecone")
    pinecone_manager = VectorStoreManager()
    index_name = "test-index"  # Replace with your Pinecone index name
    pinecone_manager.save_embeddings(chunks, embeddings, index_name)
    print("Embeddings stored in Pinecone.")

    # 6. Querying Pinecone: Retrieve similar chunks from the server
    print("\nStep 6: Querying Pinecone")
    query_text = "Sample query text"  # Replace with a relevant query
    query_embedding = embedding_manager.generate_embeddings([query_text])[0]
    pinecone_results = pinecone_manager.query_embedding(query_embedding, index_name, top_k=3)
    print(f"Pinecone Query Results:\n{pinecone_results}")


# Run the test script
if __name__ == "__main__":
    asyncio.run(main())
