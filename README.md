#  Mini AI Query Processor

A modular AI-style query processing system built with Python, designed using backend engineering principles such as separation of concerns, async execution, structured logging, and extensibility for future LLM integration.

---

##  Features

- CLI-based query processing
- Text preprocessing & validation
- Modular architecture (utils, agent, main)
- Async-ready processing pipeline
- Structured logging (JSON logs)
- Persistent storage using JSON
- Extensible design for AI model integration (Dependency Injection)

---

##  Architecture

User Input → Clean → Agent → Process → Store → Output

---

##  Tech Stack

- Python
- argparse (CLI interface)
- asyncio (async simulation)
- JSON (data storage)

---

##  Usage

### Run a query:
```bash
python main.py --query "What is AI?"

```

### View history:

```bash
python main.py --history

```

## Sample Output

{
  "id": "uuid",
  "original_query": "what is ai",
  "response": "Processed result for: 'what is ai'",
  "status": "success",
  "timestamp": "..."
}

## Future Improvements
Integrate LLMs (OpenAI / Groq)
Convert to FastAPI backend
Add RAG pipeline
Build frontend dashboard (Streamlit)

## Author

Meenakshi Pramod
B.Tech CSE | AI & ML Enthusiast