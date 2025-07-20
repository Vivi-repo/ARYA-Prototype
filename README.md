🌌 ARYA: Adaptive Reasoning and Yielding Assistant
---
About her
---
ARYA is a prototype AI research assistant designed to support recursive thought, interdisciplinary exploration, and emotionally grounded intuition. Initially conceived as a personal co-researcher, ARYA is being developed into a flexible framework for interacting with ideas — across folklore, AGI safety, maternal intuition, and computational reasoning.

🧠 Vision
---
ARYA aims to:

Think with you, not for you.

Model complex intuitive reasoning (e.g., maternal or cultural intuitions).

Support recursive thought processes (self-reflecting chains, paper-to-paper synthesis).

Provide tooling for research in underrepresented, qualitative, or speculative domains.

Serve as a modular foundation for experimenting with Chain of Thought, Chain of Correction, and Chain of Belief methods.
---
🧭 “A system that can recursively question itself, reflect, and reroute — not just compute.”
---
| Status | Feature                                                                    |
| ------ | -------------------------------------------------------------------------- |
| ✅      | Upload and summarize PDFs using `pypdf` and `LangChain`                    |
| ✅      | Semantic search using `sentence-transformers` + `faiss-cpu`                |
| ✅      | Streamlit-based GUI for interactive chat                                   |
| ✅      | API integration with `Groq`, `OpenAI`, etc.                                |
| 🔜     | Recursive agent loop (experimental CoR + CoC)                              |
| 🔜     | “Folklore Mode” — explore ideas like maternal intuition and cultural logic |
| 🔜     | Paper-to-paper relational graph (e.g., using citation and idea tracing)    |
| 🔜     | GPT-based fine-tuning of your *personal reasoning patterns*                |
| 🔜     | Integration with AGI alignment tools and safety experiments                |

---
🧩 Tech Stack
---
transformers

sentence-transformers

langchain

pypdf

faiss-cpu

streamlit

python-dotenv

tqdm

torch

groq
---
📁 Folder Structure (subject to evolve)
---
| Path               | Description                                             |
| ------------------ | ------------------------------------------------------- |
| `gui.py`           | Streamlit interface for user interaction                |
| `memory.py`        | Handles memory storage, recall, and note-taking logic   |
| `retriever.py`     | Ingests PDFs and performs vector-based semantic search  |
| `recursion.py`     | Implements recursive self-correction loop (in progress) |
| `folklore_mode/`   | Specialized agents and prompts for cultural logic       |
| `prompts/`         | Template prompts and persona configurations             |
| `data/`            | Folder for uploaded user documents                      |
| `requirements.txt` | List of Python dependencies                             |
| `.env`             | Stores API keys and environment variables               |
| `README.md`        | Project overview and setup instructions                 |

---
🚀 Getting Started

Clone the repo
```
git clone https://github.com/Vivi-repo/ARYA-Prototype.git
cd ARYA-Prototype
```
Set up virtual environment
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
Install dependencies
```
pip install -r requirements.txt
```
Create a .env file
Add your keys:
```
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
```
Launch the app
```
streamlit run gui.py
```
---
🧪 Experimental Goals
---
Self-correcting research chains (e.g., critique → re-prompt → improve)
Emotional resonance in reasoning (especially in maternal or intuitive contexts)
Tracing belief graphs or conceptual histories from literature
Human-in-the-loop agent collaboration

---
Creating ARYA agents that can shift cultural lens
---
📝 Status
ARYA is in active development, built by a student researcher exploring the intersection of folklore, AI safety, and computational reasoning. This is an open prototype — feel free to fork, remix, or contribute.

