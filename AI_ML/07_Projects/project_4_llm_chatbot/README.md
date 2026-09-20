# 🤖 Project 4: RAG-Powered Chatbot

**LLMs in Practice — Retrieval Augmented Generation**

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐⭐ Advanced |
| **Time Estimate** | 12–18 hours |
| **Prerequisites** | NLP, Transformers, Deep Learning, basic API usage |

---

## Overview

Build a chatbot that answers questions about **your own documents** using RAG (Retrieval Augmented Generation). Instead of relying solely on an LLM's training data, you'll retrieve relevant passages from your documents and feed them as context — giving the LLM grounded, accurate answers.

**Goal:** Ask natural language questions about your documents and get accurate, sourced answers.

---

## Architecture

```
User Question
     │
     ▼
┌──────────┐     ┌──────────────┐     ┌───────────┐
│ Embed    │────▶│ Vector Search │────▶│ Top K     │
│ Question │     │ (FAISS/Chroma)│     │ Chunks    │
└──────────┘     └──────────────┘     └─────┬─────┘
                                            │
                                            ▼
                                  ┌──────────────────┐
                                  │ Prompt:           │
                                  │ Context: {chunks} │
                                  │ Question: {query} │
                                  └────────┬─────────┘
                                           │
                                           ▼
                                  ┌──────────────────┐
                                  │   LLM (GPT/etc)  │
                                  │   Generate Answer │
                                  └────────┬─────────┘
                                           │
                                           ▼
                                   Grounded Answer
```

---

## Dataset

Use **your own documents** — that's the whole point of RAG!

Ideas:
- Your study notes (PDFs, markdown files)
- A textbook chapter (PDF)
- Company documentation
- Wikipedia articles on a topic you're learning
- Any collection of text files

---

## Steps

### Step 1: Prepare Documents
- Collect 5–20 documents (PDFs, text files, markdown)
- Load them into Python (use `PyPDF2` for PDFs, plain `open()` for text)
- Preview the content — make sure it loaded correctly

### Step 2: Chunk Documents into Passages
- Split each document into overlapping chunks (e.g., 500 tokens with 50-token overlap)
- Experiment with chunk sizes — too small loses context, too large dilutes relevance
- Store metadata: source filename, chunk index, page number
- Example: a 10-page PDF → ~40 chunks

### Step 3: Compute Embeddings
- Choose an embedding model:
  - OpenAI: `text-embedding-3-small` (API, easy)
  - Local: `sentence-transformers/all-MiniLM-L6-v2` (free, runs locally)
- Embed all chunks → each becomes a dense vector (e.g., 384 or 1536 dimensions)
- This is done once and cached

### Step 4: Store in a Vector Index
- Choose a vector store:
  - **FAISS** — Facebook's library, fast, lightweight, in-memory
  - **ChromaDB** — Higher-level, persistent, good for prototyping
- Index all chunk embeddings
- Test: embed a query → search → check if top results are relevant

### Step 5: Retrieval Pipeline
- For a user question:
  1. Embed the question (same model as chunks)
  2. Search the vector index for top-k similar chunks (k=3–5)
  3. Return the chunk texts + metadata (source, page)

### Step 6: Generation with LLM
- Construct a prompt:
  ```
  Use the following context to answer the question.
  If you can't find the answer in the context, say "I don't know."

  Context:
  {chunk_1}
  {chunk_2}
  {chunk_3}

  Question: {user_question}
  Answer:
  ```
- Send to LLM:
  - **OpenAI API**: `gpt-4o-mini` or `gpt-4o`
  - **Local**: Use `ollama` with `llama3` or similar
- Parse and return the answer

### Step 7: Put It All Together
- Build a simple interactive loop:
  ```
  > Ask a question: What is gradient descent?
  Answer: Gradient descent is an optimization algorithm...
  Sources: [notes_ch3.pdf, page 12], [lecture_5.md, chunk 4]
  ```
- (Optional) Add a Streamlit or Gradio UI

---

## What You'll Learn

| Skill | Notebook Topic |
|-------|---------------|
| Text embeddings | `09_NLP/`, `11_LLMs/` |
| Vector similarity search | `11_LLMs/` |
| Document chunking strategies | `11_LLMs/` |
| LLM API usage | `11_LLMs/` |
| Prompt engineering | `11_LLMs/` |
| RAG architecture | `11_LLMs/` |
| Building interactive apps | `12_MLOps/` |

---

## Deliverables Checklist

- [ ] Document loading pipeline (supports PDF + text)
- [ ] Chunking with configurable size and overlap
- [ ] Embedding pipeline (batch process all chunks)
- [ ] Vector index built and queryable
- [ ] Retrieval function: question → relevant chunks
- [ ] LLM generation with context injection
- [ ] End-to-end Q&A working on your documents
- [ ] Source attribution in answers
- [ ] At least 10 test questions with quality assessment
- [ ] Clean `main.py` with modular functions
- [ ] Brief write-up: chunk size experiments, retrieval quality observations

---

## Starter Code

See [`main.py`](main.py) for the project skeleton.

```
project_4_llm_chatbot/
├── README.md
├── main.py              # Main RAG pipeline
├── notebook.ipynb       # Experimentation (create this)
├── documents/           # Your source documents (create this)
│   ├── notes.pdf
│   ├── chapter1.txt
│   └── ...
└── index/               # Saved vector index (create this)
```
