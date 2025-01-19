# Flipkart ChatBot

This repository contains a chatbot project developed using Flipkart data, LangChain, AstraDB, and Qroq Cloud. The chatbot leverages modern AI techniques to provide contextual responses based on user queries and historical chat data.

## System Architecture

The chatbot is divided into two main processes:

### 1. **History-Aware Retriever**
- **Input Query & Chat History**: The chatbot takes the user's input query along with the conversation history.
- **"Contextualize Query" Prompt**: A prompt is created to contextualize the query using the conversation history.
- **LLM (Large Language Model)**: The contextualized query is refined using a large language model.
- **Retriever**: The refined query is used to fetch relevant documents from the knowledge base.

### 2. **Question-Answer Chain**
- **Documents**: Relevant documents retrieved from the knowledge base are used to answer the query.
- **"Answer Question" Prompt**: A prompt is created to generate the answer using the retrieved documents.
- **LLM**: The large language model generates the final response.
- **Answer**: The chatbot provides the user with the response.

## Features
- **Context-Aware Responses**: The chatbot takes conversation history into account for generating relevant responses.
- **Dynamic Retrieval**: Uses a retriever mechanism to fetch the most relevant documents.
- **Scalable Architecture**: Powered by AstraDB for database management and Qroq Cloud for scalability.

## Tech Stack
- **LangChain**: Framework for building applications powered by language models.
- **AstraDB**: NoSQL database for storing conversation history and documents.
- **Qroq Cloud**: Cloud platform for hosting and scaling the application.
- **Google Colab**: Python environment for development and experimentation.
- **Flask**: Lightweight Python framework for building web applications.

## Installation

### Prerequisites
- Python 3.8+
- [LangChain](https://docs.langchain.com/)
- [AstraDB](https://www.datastax.com/astra)
- [Qroq Cloud](https://qroq.cloud/)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/13Ananya/Flipkart.git
   cd Flipkart
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up AstraDB:
   - Create a database on [AstraDB](https://www.datastax.com/astra).

4. Obtain your all credentials and store them in a `.env` file:
     ```env
     GROQ_API_KEY = 
     ASTRA_DB_API_ENDPOINT = 
     ASTRA_DB_APPLICATION_TOKEN = 
     ASTRA_DB_KEYSPACE = "default_keyspace"
     HF_TOKEN = 
     ```
5. Use Setup.py for installing local package.

## Usage
1. Start the chatbot locally:
   ```bash
   python app.py
   ```

2. Access the chatbot through the provided URL (e.g., `http://localhost:5000`).

3. Input queries and interact with the chatbot.

## Project Structure
```plaintext
Flipkart/
├── app.py                 # Main application script
├── requirements.txt       # Dependencies
├── .env                   # Environment variables
├── assets/                # Contains system flow diagram
├── modules/               # Contains custom modules for chatbot functionality
├── templates/             # HTML templates for the web interface
├── static/                # Static files (CSS, JS, images)
└── README.md              # Project documentation
```

## Contributing
We welcome contributions to improve the chatbot. Feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any queries or suggestions, feel free to contact:
- **Ananya** (Project Maintainer): [GitHub Profile](https://github.com/13Ananya)
