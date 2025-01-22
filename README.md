# Semantic Kernel learning

Basic hack to learn a bit of Semantic Kernel

- `main.py`: Calls Azure OpenAI to start a chat session, and has some basic tools/plugins running
- `phi3.py`: Calls a locally running phi 3 model which is running on the default port with Ollama

```
    cd semantic-learning
    poetry install
    az login
    poetry run python3 semantic_learning/main.py
```