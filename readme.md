# Form 10-K Knowledge Graph

This repository contains a project for building and querying a knowledge graph from SEC Form 10-K filings. The knowledge graph is implemented using Neo4j and integrates with OpenAI's GPT-based embeddings for advanced text retrieval and question-answering capabilities.

## Features

- **Data Ingestion**: Parses Form 10-K JSON files and splits them into manageable chunks for storage in the Neo4j database.
- **Knowledge Graph Construction**: Builds a graph with nodes and relationships representing companies, managers, addresses, and investments.
- **Vector Search**: Uses OpenAI embeddings to create a vector index for semantic search and retrieval.
- **Question Answering**: Implements retrieval-based question-answering chains using LangChain.
- **Cypher Query Generation**: Dynamically generates Cypher queries for graph-based data retrieval.

## Project Structure

- **`index.ipynb`**: Main notebook for data ingestion, graph construction, and querying.
- **`chatWithKg.ipynb`**: Notebook for interacting with the knowledge graph using Cypher queries and question-answering chains.
- **`chatWithKgComplete.ipynb`**: Extended version of `chatWithKg.ipynb` with additional features and schema exploration.
- **`data/`**: Directory containing Form 10-K JSON files and other input data.
- **`.env`**: Environment file for storing sensitive credentials like Neo4j and OpenAI API keys.

## Setup

1. **Install Dependencies**:
   Ensure you have Python 3.9+ installed. Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Environment Variables**:
   Create a `.env` file in the root directory with the following variables:
   ```
   NEO4J_URI=<your_neo4j_uri>
   NEO4J_USERNAME=<your_neo4j_username>
   NEO4J_PASSWORD=<your_neo4j_password>
   OPENAI_API_KEY=<your_openai_api_key>
   ```

3. **Run Neo4j**:
   Start a Neo4j instance and ensure it is accessible via the URI specified in the `.env` file.

4. **Load Data**:
   Use the `index.ipynb` notebook to parse and load Form 10-K data into the Neo4j database.

## Usage

### 1. Build the Knowledge Graph
Run the cells in `index.ipynb` to:
- Parse Form 10-K JSON files.
- Split text into chunks and store them as nodes in Neo4j.
- Create relationships between nodes (e.g., `:NEXT`, `:PART_OF`, `:OWNS_STOCK_IN`).

### 2. Query the Knowledge Graph
Use `chatWithKg.ipynb` or `chatWithKgComplete.ipynb` to:
- Explore the graph schema.
- Execute Cypher queries to retrieve data.
- Ask natural language questions using the retrieval-based question-answering chain.

### 3. Semantic Search
Leverage the vector index for semantic search:
- Create a retriever using `Neo4jVector`.
- Use the retriever in a `RetrievalQAWithSourcesChain` for advanced question-answering.

## Key Components

### Graph Schema
- **Nodes**:
  - `Chunk`: Represents a chunk of text from a Form 10-K.
  - `Form`: Represents a Form 10-K document.
  - `Company`: Represents a company filing the Form 10-K.
  - `Manager`: Represents an investment manager.
  - `Address`: Represents a physical address.

- **Relationships**:
  - `:NEXT`: Links sequential chunks of text.
  - `:PART_OF`: Links chunks to their parent Form.
  - `:SECTION`: Links Forms to specific sections (e.g., `item1`, `item7`).
  - `:FILED`: Links companies to their filed Forms.
  - `:OWNS_STOCK_IN`: Links managers to companies they invest in.

### Vector Search
- **Embedding**: Text embeddings are generated using OpenAI's GPT-based embeddings.
- **Indexing**: A vector index is created in Neo4j for semantic similarity search.
- **Retrieval**: Questions are answered by retrieving the most relevant chunks using cosine similarity.

### Question Answering
- **LangChain Integration**: Combines Neo4j and OpenAI embeddings for retrieval-based question answering.
- **Chains**:
  - `RetrievalQAWithSourcesChain`: Answers questions with source references.
  - `GraphCypherQAChain`: Generates Cypher queries for graph-based retrieval.

## Example Queries

### Cypher Query
```cypher
MATCH (mgr:Manager)-[:OWNS_STOCK_IN]->(com:Company)
WHERE mgr.managerName = "Royal Bank of Canada"
RETURN com.companyName, mgr.managerName
```

### Natural Language Question
```python
question = "Who are the top investors in NetApp?"
response = chain({"question": question}, return_only_outputs=True)
print(response["answer"])
```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- **Neo4j**: For the graph database platform.
- **OpenAI**: For GPT-based embeddings.
- **LangChain**: For building retrieval-based question-answering chains.

## Contact

For questions or support, please contact [Sachin](mailto:sachin@example.com).