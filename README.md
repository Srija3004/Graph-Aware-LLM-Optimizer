# 🧠 Graph-Aware LLM Optimizer

An AI-powered web application for solving NP-Hard graph optimization problems using classical graph algorithms and Mistral AI for intelligent solution analysis.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![React](https://img.shields.io/badge/React-18-61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688)
![MistralAI](https://img.shields.io/badge/Mistral-AI-purple)

---

## 📖 Overview

Graph-Aware LLM Optimizer is an interactive AI-powered platform that enables users to create graphs, solve complex NP-Hard optimization problems, visualize solutions, and receive AI-generated explanations.

The application combines efficient graph algorithms with **Mistral AI** to provide not only optimized solutions but also detailed reasoning, quality assessment, and improvement suggestions.

---

# ✨ Features

✅ Interactive Graph Visualization

- Create custom graphs
- Generate random graphs
- Drag-and-drop graph visualization
- Zoom and explore graph structures

---

✅ Supported Optimization Problems

- 🚗 Traveling Salesman Problem (TSP)
- 🎨 Graph Coloring
- 👥 Maximum Clique
- 🛡 Vertex Cover
- 🔗 Hamiltonian Path

---

✅ AI-Powered Analysis

After computing the solution, Mistral AI provides:

- Detailed explanation
- Quality assessment
- Optimization suggestions
- Algorithm insights

---

✅ Beautiful Modern UI

- Dark theme
- Responsive design
- Smooth animations
- Interactive cards
- Gradient components

---

# 🏗 System Architecture

```
                End User
                    │
                    ▼
        React + Vite Frontend
                    │
      D3.js Graph Visualization
                    │
                    ▼
           FastAPI Backend
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
 Graph Algorithms  NetworkX   Mistral AI
```

---

# 🖼 Application Screenshots

## Home Page

*A modern landing page introducing Graph-Aware LLM Optimizer.*
<img width="1920" height="1080" alt="Screenshot (246)" src="https://github.com/user-attachments/assets/234de31e-1a63-4098-a8a6-86775b327d2e" />

---

## Optimization Problems

Users can choose from multiple NP-Hard optimization problems including:

- Traveling Salesman
- Graph Coloring
- Maximum Clique
- Vertex Cover
- Hamiltonian Path

---

## Interactive Graph Visualization

- Create graphs
- Visualize nodes and edges
- Drag nodes dynamically
- Zoom and explore

---

## Graph Solver

Users can

- Define nodes
- Enter weighted edges
- Generate random graphs
- Solve optimization problems

---

## Solution Results

Displays

- Algorithm used
- Execution time
- Total cost
- Optimal path

---

## AI Analysis

Mistral AI generates

- Explanation
- Quality Assessment
- Suggestions

---

# ⚙ Tech Stack

## Frontend

- React
- Vite
- D3.js
- CSS3

---

## Backend

- FastAPI
- Python

---

## Graph Processing

- NetworkX

---

## AI Integration

- Mistral AI API

---

## Development Tools

- VS Code
- Git
- GitHub

---

# 📂 Project Structure

```
Graph-Aware-LLM-Optimizer/

│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── algorithms/
│   ├── api/
│   ├── llm/
│   ├── config.py
│   ├── main.py
│   └── requirements.txt
│
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Srija3004/Graph-Aware-LLM-Optimizer.git
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Run Backend

```bash
uvicorn main:app --reload

Or, id that doesn't work:

python -m uvicorn main:app --reload
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend folder.

```
mistral_api_key=YOUR_API_KEY
mistral_model=mistral-medium
```

> **Note:** Never upload your actual API key to GitHub.

---

# 💡 Algorithms Used

| Problem | Algorithm |
|----------|-----------|
| Traveling Salesman | Christofides Approximation |
| Graph Coloring | DSatur Algorithm |
| Maximum Clique | Bron–Kerbosch |
| Vertex Cover | 2-Approximation |
| Hamiltonian Path | Backtracking |

---

# 📈 Future Enhancements

- User authentication
- Save graph history
- Export graph as PDF
- Additional optimization algorithms
- Multiple LLM support
- Cloud deployment
- Graph upload via CSV

---

# 👩‍💻 Author

**Mandarapu Srija**

Computer Science Engineering Student

GitHub:
https://github.com/Srija3004

---
