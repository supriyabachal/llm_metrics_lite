# llm-metrics-lite
llm-metrics-lite provides a clean, dependency-minimal Python toolkit to evaluate generated text from Large Language Models (LLMs).
It offers coherence, perplexity, groundedness/factuality heuristics, token statistics, and CLI support — all in a fast and portable package.

 Why This Exists

Evaluating LLM outputs is currently fragmented across:

heavyweight frameworks

ad-hoc scripts

application-specific scoring tools

This library gives a simple, general-purpose evaluation layer that:

can be used in research, production, or benchmarking

is easy to install and extend

supports CLI + Python usage

Features

 Coherence Score
Lexical cosine similarity between sentences

 Perplexity (Reference-Free)
Character-level n-gram perplexity (no model dependencies)

 Groundedness / Factuality
Measures overlap between output and supporting context

 Latency Utilities
Measure latency around inference calls

 Token Statistics
Word count, character count, token approximation

🖥 CLI Interface
Run directly from terminal against files

Zero Heavy Dependencies
Portable, lightweight, easy to extend

📦 Installation
pip install llm-metrics-lite


(If you’re installing from source)

pip install -e .

 Python Example
from llm_metrics_lite import train_default_perplexity_model, evaluate_output

# Minimal corpus to train perplexity model
corpus = [
    "Artificial intelligence enables machines to learn from data.",
    "Language models process and generate human-like text.",
]

ppl_model = train_default_perplexity_model(corpus)

output_text = "Generative AI models help automate reasoning tasks."
context_text = "AI models are capable of understanding language and generating responses."

result = evaluate_output(output_text, context_text=context_text, perplexity_model=ppl_model)
print(result)

🖥 CLI Usage
Evaluate directly from text files
llm-metrics-lite evaluate output.txt

Evaluate with a context reference
llm-metrics-lite evaluate output.txt --context context.txt

Example Notebook

See the notebook in examples/example_llm_metrics_lite.ipynb
It demonstrates end-to-end evaluation in Python.
