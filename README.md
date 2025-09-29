## Process email - Project to learn LangGraph, Langfuse

This code is referred from HuggingFace, but modified for completion/correct response.
This is an attempt to understand the LangGraph and the state maintenance.

LangGraph - helps to build the complex state graph for a deterministic output. LangGraph is more matrued and production ready.
Langfuse - is to build guardrails around the agents to trace and monitor the agents actions

## command to update requirement.txt - Freezing the working environment
pip freeze > requirements.txt 

## create a virtual environment
python -m venv .venv
  ## Activate the virtual environment
    .venv\Scripts\activate
