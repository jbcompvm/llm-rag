# LLM with RAG Front-end

This project provides a front-end interface for interacting with an LLM API, enhanced with Retrieval Augmented Generation (RAG) capabilities.

## Installation

1.  Clone the repository.
2.  Run `./install_llm.sh`.
3.  Follow the on-screen instructions to run the front-end and RAG backend.

## Configuration

* Replace `http://your-llm-api:8000/v1/completions` in `frontend/config.py` with your LLM API endpoint.
* Place your documents in the `rag_backend/data` directory.

## Usage

1.  Activate the virtual environment: `source llm_env/bin/activate`.
2.  Run the RAG backend: `python rag_backend/rag_logic.py`.
3.  In a separate terminal, run the front-end: `cd frontend; streamlit run Home.py`.
4.  Enter your query in the front-end interface.

## Contributing

Contributions are welcome!