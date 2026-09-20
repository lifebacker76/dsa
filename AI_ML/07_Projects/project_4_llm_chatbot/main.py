"""
RAG-Powered Chatbot — LLMs in Practice
=======================================

Build a chatbot that answers questions about your documents
using Retrieval Augmented Generation (RAG).

Usage:
    python main.py
"""

import os
import numpy as np
from pathlib import Path


# =============================================================================
# Step 1: Document Loading
# =============================================================================

def load_text_file(filepath):
    """Load a plain text or markdown file.

    Args:
        filepath (str): Path to the text file.

    Returns:
        dict: {"content": str, "source": str, "type": "text"}
    """
    pass


def load_pdf_file(filepath):
    """Load a PDF file and extract text.

    Args:
        filepath (str): Path to the PDF file.

    Returns:
        dict: {"content": str, "source": str, "type": "pdf", "pages": int}

    Requires:
        pip install PyPDF2
    """
    pass


def load_documents(directory="documents/"):
    """Load all documents from a directory.

    Args:
        directory (str): Path to directory containing documents.

    Returns:
        list[dict]: List of document dicts with content and metadata.

    Supports:
        .txt, .md, .pdf files
    """
    pass


# =============================================================================
# Step 2: Chunking
# =============================================================================

def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks by token count.

    Args:
        text (str): Full document text.
        chunk_size (int): Target tokens per chunk.
        overlap (int): Number of overlapping tokens between chunks.

    Returns:
        list[str]: List of text chunks.

    Notes:
        - Simple approach: split by words (1 word ≈ 1.3 tokens)
        - Better: use tiktoken for exact token counting
        - Overlap prevents losing context at chunk boundaries
    """
    pass


def chunk_documents(documents, chunk_size=500, overlap=50):
    """Chunk all documents and preserve metadata.

    Args:
        documents (list[dict]): Loaded documents.
        chunk_size (int): Tokens per chunk.
        overlap (int): Overlap tokens.

    Returns:
        list[dict]: List of {"text": str, "source": str, "chunk_index": int}
    """
    pass


# =============================================================================
# Step 3: Embeddings
# =============================================================================

def get_embedding_model(model_name="all-MiniLM-L6-v2"):
    """Load a sentence-transformers embedding model.

    Args:
        model_name (str): HuggingFace model name.

    Returns:
        SentenceTransformer model.

    Options:
        - "all-MiniLM-L6-v2" — fast, 384 dims (recommended for start)
        - "all-mpnet-base-v2" — better quality, 768 dims
        - Or use OpenAI API: "text-embedding-3-small"
    """
    pass


def embed_texts(texts, model):
    """Compute embeddings for a list of texts.

    Args:
        texts (list[str]): Texts to embed.
        model: Embedding model.

    Returns:
        np.ndarray: Embeddings matrix [n_texts, embedding_dim].
    """
    pass


def embed_query(query, model):
    """Compute embedding for a single query.

    Args:
        query (str): Query text.
        model: Embedding model.

    Returns:
        np.ndarray: Query embedding [1, embedding_dim].
    """
    pass


# =============================================================================
# Step 4: Vector Index
# =============================================================================

def build_faiss_index(embeddings):
    """Build a FAISS index from embeddings.

    Args:
        embeddings (np.ndarray): Embeddings matrix [n, dim].

    Returns:
        faiss.Index: Built FAISS index.

    Requires:
        pip install faiss-cpu
    """
    pass


def build_chroma_index(chunks, embeddings, collection_name="documents"):
    """Build a ChromaDB collection from chunks and embeddings.

    Args:
        chunks (list[dict]): Chunk dicts with text and metadata.
        embeddings (np.ndarray): Embeddings for each chunk.
        collection_name (str): Name for the collection.

    Returns:
        chromadb.Collection: Built collection.

    Requires:
        pip install chromadb
    """
    pass


def save_index(index, filepath="index/faiss_index.bin"):
    """Save the FAISS index to disk.

    Args:
        index: FAISS index.
        filepath (str): Path to save.
    """
    pass


def load_index(filepath="index/faiss_index.bin"):
    """Load a FAISS index from disk.

    Args:
        filepath (str): Path to saved index.

    Returns:
        faiss.Index: Loaded index.
    """
    pass


# =============================================================================
# Step 5: Retrieval
# =============================================================================

def retrieve(query, model, index, chunks, top_k=5):
    """Retrieve the most relevant chunks for a query.

    Args:
        query (str): User's question.
        model: Embedding model.
        index: FAISS index.
        chunks (list[dict]): All chunk dicts.
        top_k (int): Number of chunks to retrieve.

    Returns:
        list[dict]: Top-k chunks with scores.
            [{"text": ..., "source": ..., "score": ...}, ...]
    """
    pass


# =============================================================================
# Step 6: Generation
# =============================================================================

def build_prompt(query, retrieved_chunks):
    """Build the LLM prompt with retrieved context.

    Args:
        query (str): User's question.
        retrieved_chunks (list[dict]): Retrieved context chunks.

    Returns:
        str: Formatted prompt for the LLM.

    Template:
        Use the following context to answer the question.
        If you can't find the answer in the context, say "I don't know."

        Context:
        [chunk texts here]

        Question: {query}
        Answer:
    """
    pass


def generate_answer_openai(prompt, model="gpt-4o-mini"):
    """Generate an answer using OpenAI API.

    Args:
        prompt (str): Full prompt with context and question.
        model (str): OpenAI model name.

    Returns:
        str: Generated answer.

    Requires:
        pip install openai
        Set OPENAI_API_KEY environment variable.
    """
    pass


def generate_answer_local(prompt, model_name="llama3"):
    """Generate an answer using a local model (via ollama).

    Args:
        prompt (str): Full prompt with context and question.
        model_name (str): Ollama model name.

    Returns:
        str: Generated answer.

    Requires:
        Install ollama and pull a model:
        ollama pull llama3
    """
    pass


# =============================================================================
# Step 7: Full RAG Pipeline
# =============================================================================

def ask(query, model, index, chunks, llm="openai", top_k=5):
    """Full RAG pipeline: retrieve + generate.

    Args:
        query (str): User's question.
        model: Embedding model.
        index: Vector index.
        chunks (list[dict]): All chunks.
        llm (str): "openai" or "local".
        top_k (int): Number of chunks to retrieve.

    Returns:
        dict: {
            "answer": str,
            "sources": list[dict],
            "query": str
        }
    """
    pass


def format_response(result):
    """Pretty-print a RAG response.

    Args:
        result (dict): Output from ask().

    Prints:
        Formatted answer with source citations.
    """
    pass


# =============================================================================
# Interactive Chat Loop
# =============================================================================

def chat_loop(model, index, chunks, llm="openai"):
    """Interactive Q&A loop.

    Args:
        model: Embedding model.
        index: Vector index.
        chunks (list[dict]): All chunks.
        llm (str): Which LLM to use.
    """
    print("\n💬 RAG Chatbot — Ask questions about your documents!")
    print("Type 'quit' to exit.\n")

    while True:
        query = input("You: ").strip()
        if query.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        if not query:
            continue

        # result = ask(query, model, index, chunks, llm=llm)
        # format_response(result)
        print("(Pipeline not yet implemented — fill in the functions above!)\n")


# =============================================================================
# Main Pipeline
# =============================================================================

def main():
    """Run the full RAG pipeline.

    Steps:
        1. Load documents
        2. Chunk documents
        3. Compute embeddings
        4. Build vector index
        5. Start interactive chat
    """
    print("=" * 60)
    print("RAG-Powered Chatbot")
    print("=" * 60)

    # Step 1: Load documents
    print("\n📄 Step 1: Loading documents...")
    # documents = load_documents("documents/")
    # print(f"Loaded {len(documents)} documents")

    # Step 2: Chunk
    print("\n✂️  Step 2: Chunking documents...")
    # chunks = chunk_documents(documents, chunk_size=500, overlap=50)
    # print(f"Created {len(chunks)} chunks")

    # Step 3: Embed
    print("\n🧮 Step 3: Computing embeddings...")
    # embed_model = get_embedding_model()
    # chunk_texts = [c["text"] for c in chunks]
    # embeddings = embed_texts(chunk_texts, embed_model)
    # print(f"Embeddings shape: {embeddings.shape}")

    # Step 4: Index
    print("\n📚 Step 4: Building vector index...")
    # index = build_faiss_index(embeddings)
    # save_index(index)

    # Step 5: Chat
    print("\n🚀 Step 5: Starting chat...")
    # chat_loop(embed_model, index, chunks, llm="openai")

    print("\n✅ Setup complete! Fill in the functions to start chatting.")


if __name__ == "__main__":
    main()
