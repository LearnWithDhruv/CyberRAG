
# Cybersecurity RAG System

This project implements a **Retrieval-Augmented Generation (RAG)** system using **LangGraph** and **LangChain** for a cybersecurity and penetration testing use case. The RAG pipeline ingests data, builds a dynamic graph structure, and retrieves relevant information in response to queries using an inference pipeline. The data is structured to model cybersecurity entities like hosts, ports, services, vulnerabilities, and credentials, using data from walkthroughs as references.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Setup Instructions](#setup-instructions)
5. [Usage](#usage)
6. [Modules](#modules)
    - [Data Ingestion](#data-ingestion)
    - [Graph Management](#graph-management)
    - [Inference Pipeline](#inference-pipeline)
7. [Benchmarking](#benchmarking)
8. [Diagrams](#diagrams)
9. [Future Improvements](#future-improvements)

---

## Project Overview

This RAG pipeline ingests raw text and images related to cybersecurity, builds and updates a knowledge graph, and uses an inference pipeline to answer queries based on the data stored. It’s designed to help security professionals quickly retrieve information about targets like open ports, outdated services, common vulnerabilities, and login forms. 

The data can be ingested from MongoDB and stored in a vector database like Chroma for efficient retrieval.

## Features

- **Data Ingestion** from MongoDB, including raw text and images.
- **Dynamic Graph Construction** with entities like hosts, ports, vulnerabilities, and credentials.
- **Contextual Query Handling** for efficient information retrieval using LLMs.
- **Benchmarking** to track response times and optimize performance.

## Project Structure

```plaintext
cybersec_rag_project/
├── README.md                        # Documentation
├── Dockerfile                       # Docker configuration
├── requirements.txt                 # Dependencies for pip
├── .env                             # Environment variables (API keys, database URIs)
├── src/                             # Main source code directory
│   ├── main.py                      # Main entry point for running the project
│   ├── config.py                    # Configuration and environment settings
│   ├── ingestion/                   # Data ingestion modules
│   ├── graph/                       # Graph creation and storage
│   ├── inference/                   # Query and inference pipeline
│   ├── utils/                       # Utility functions
│   └── tests/                       # Unit tests
└── benchmarks/                      # Directory to store benchmarking results
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cybersec_rag_project.git
cd cybersec_rag_project
```

### 2. Set Up a Virtual Environment

Create a virtual environment using `venv`:

```bash
python3 -m venv venv
```

Activate the environment:

- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```plaintext
MONGO_URI="your_mongodb_uri"
CHROMA_PATH="path_to_chroma_vectors"
OPENAI_API_KEY="your_openai_api_key"
```

### 5. Running the Project

Run the main pipeline:

```bash
python src/main.py
```

---

## Usage

The project can be run by executing the `main.py` file. This file:

1. **Ingests Data** from MongoDB.
2. **Processes Text** to extract entities and relationships.
3. **Builds and Updates a Knowledge Graph**.
4. **Handles User Queries** by retrieving relevant information.
5. **Generates Responses** using an LLM model.

---

## Modules

### Data Ingestion

- **DataIngestor**: Connects to MongoDB to fetch raw data.
- **TextProcessor**: Uses Langchain to process text, extracting entities like `hosts`, `ports`, and `vulnerabilities`.
- **EntityRelationBuilder**: Organizes extracted entities and relationships into a graph-compatible format.

### Graph Management

- **GraphBuilder**: Constructs a graph with nodes (entities) and edges (relationships).
- **GraphStorage**: Stores the graph embeddings in Chroma for fast and efficient retrieval.

### Inference Pipeline

- **QueryHandler**: Parses and interprets user queries.
- **ContextRetriever**: Fetches relevant context from the Chroma database.
- **ResponseGenerator**: Generates natural-language responses using OpenAI’s API based on the retrieved context.

---

## Benchmarking

Benchmarking data is stored in the `benchmarks/` directory. This module measures response time and performance for query handling and retrieval.

1. **Measure Time**: Logs the time taken for each query from context retrieval to response generation.
2. **Save Results**: Saves benchmarking results in `response_times.json`.

Example usage for benchmarking:

```python
from src.inference.benchmarks import Benchmark

benchmark = Benchmark()
query = "What services are running on target.com?"
response = benchmark.measure_time(response_generator.generate_response, context, query)
benchmark.save_results()
```

---

## Diagrams

All diagrams for data flow, entity relationships, and pipeline architecture are stored in the `diagrams/` directory. Use these to understand the RAG pipeline's architecture.

- **pipeline_flow.png**: Visual representation of the data ingestion and inference pipeline.
- **graph_structure.png**: Diagram illustrating the knowledge graph structure.

---

## Future Improvements

1. **Real-Time Updates**: Allow continuous updates to the graph as new data arrives in MongoDB.
2. **Enhanced Image Processing**: Expand the image processing capabilities to better support visual data related to vulnerabilities.
3. **Scalable Deployment**: Deploy the pipeline on a cloud service like AWS with API endpoints.
4. **Advanced Query Parsing**: Improve the query parser to handle more complex queries accurately.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

Special thanks to:
- [LangChain](https://www.langchain.com) and [LangGraph](https://www.langgraph.com) for their core technology support.
- [Chroma](https://www.trychroma.com) for vector-based storage.
- [HackTheBox](https://www.hackthebox.com/) for providing relevant cybersecurity walkthrough data.

---

For further information or questions, please contact [your_email@example.com].
