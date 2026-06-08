# RAG Upgrade Plan

This project currently provides the chat and multimodal interface layer. To make it a complete RAG system, add these layers next.

## Phase 1 — Basic RAG

- Add PDF/TXT/Markdown upload.
- Chunk documents with metadata.
- Create embeddings through a selected embedding model.
- Store vectors locally with Chroma or FAISS.
- Retrieve top-k chunks based on the user query.
- Inject retrieved context into the system/user prompt.
- Display citations or source snippets in the response.

## Phase 2 — Advanced RAG

- Add hybrid retrieval: vector search + keyword/BM25 search.
- Add query rewriting for better retrieval.
- Add reranking before generation.
- Add multimodal retrieval for image-heavy documents.
- Add evaluation: faithfulness, answer relevance, retrieval precision, context recall.
- Add conversation memory with source-aware follow-up handling.

## Phase 3 — Portfolio-grade polish

- Add clean landing page.
- Add sample datasets.
- Add screenshots/GIFs.
- Add GitHub Actions linting.
- Add Dockerfile.
- Add Hugging Face Spaces deployment instructions.
