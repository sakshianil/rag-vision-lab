# RAG Vision Lab

A polished Gradio + OpenRouter project that demonstrates **basic** and **advanced RAG-ready multimodal chat foundations**. The apps support text and image input, streamed model responses, configurable OpenRouter models, temperature, max token controls, and provider-side data collection denial.

> Current scope: these scripts are a strong multimodal chat foundation for RAG-style assistants. The next step is to add document ingestion, embeddings, a vector store, and retrieved-context injection.

## Why this project matters

This repository is useful for showcasing the transition from a single-file prototype to a cleaner advanced architecture:

- **Basic app:** one-file Gradio multimodal chat prototype.
- **Advanced app:** modular message-building utilities and shared response-cleaning helpers.
- **OpenRouter support:** switch between OpenAI, Gemini, Claude, and other compatible routed models.
- **Vision support:** upload an image and ask questions about it.
- **Streaming UI:** responses appear token-by-token inside Gradio.

## Repository structure

```text
rag-vision-lab/
├── src/
│   ├── app.py
│   ├── basic_gradio_chat.py
│   ├── advanced_gradio_chat.py
│   └── multimodal_messages.py
├── docs/
│   └── rag_upgrade_plan.md
├── .env.example
├── .gitignore
├── requirements.txt
└── requirements-freeze.txt
```

## Quick start

```bash
git clone https://github.com/sakshianil/rag-vision-lab.git
cd rag-vision-lab

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
```

Add your OpenRouter API key in `.env`, or paste it directly in the Gradio UI.

## Run the basic app

```bash
cd src
python basic_gradio_chat.py
```

## Run the advanced app

```bash
cd src
python advanced_gradio_chat.py
```

## Suggested GitHub description

```text
Basic and advanced RAG-ready multimodal Gradio chat apps using OpenRouter, streaming, model selection, and image input.
```

## Suggested topics

```text
rag, gradio, openrouter, multimodal-ai, vision-language-models, python, llm-apps, ai-agents
```

## Safety note

Do not commit `.env` or API keys. Keep keys in environment variables or local secret managers.

## Roadmap

See [`docs/rag_upgrade_plan.md`](docs/rag_upgrade_plan.md) for the next steps to turn this into a full RAG project with document ingestion and vector search.
