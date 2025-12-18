# llm-metrics-lite
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)
[![PyPI version](https://img.shields.io/pypi/v/llm-metrics-lite)](https://pypi.org/project/llm-metrics-lite/)
[![Downloads](https://img.shields.io/pypi/dm/llm-metrics-lite)](https://pypi.org/project/llm-metrics-lite/)
# llm-metrics-lite


PyPI: https://pypi.org/project/llm-metrics-lite/

<h1 align="center">
  <br>
  <a href="https://github.com/supriyabachal/llm_metrics_lite">
    <img src="https://raw.githubusercontent.com/supriyabachal/llm_metrics_lite/main/docs/llm-metrics-lite-logo.png" alt="llm-metrics-lite" width="350">
  </a>
  <br>
</h1>

<h4 align="center">A lightweight, dependency-minimal evaluation toolkit for Large Language Model (LLM) output quality.</h4>

<p align="center">
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
  </a>
  <a href="https://pypi.org/project/llm-metrics-lite/">
    <img src="https://img.shields.io/pypi/v/llm-metrics-lite?color=brightgreen" alt="Version">
  </a>
  <a href="https://pypi.org/project/llm-metrics-lite/">
    <img src="https://img.shields.io/pypi/pyversions/llm-metrics-lite.svg" alt="Python Versions">
  </a>
</p>

<br>

<p align="center">
  <a href="#quick-start">Quick Start</a> •
  <a href="#features">Features</a> •
  <a href="#examples">Examples</a> •
  <a href="#cli-usage">CLI Usage</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  llm-metrics-lite provides simple, reliable metrics to evaluate generated text from LLMs.  
  It offers coherence scoring, reference-free perplexity, groundedness checks, token statistics, latency utilities, and a clean CLI interface — all without heavy dependencies.
</p>

---

## Quick Start

Install from PyPI:

```bash
pip install llm-metrics-lite

# llm-metrics-lite

A lightweight, dependency-minimal evaluation toolkit for Large Language Model (LLM) output quality.

## Why This Library Exists

Existing LLM evaluation tools often:

- require large models or embeddings  
- are part of heavy research frameworks  
- depend on GPU or complex installations  
- lack simple, general-purpose APIs  

llm-metrics-lite was created to be:

- minimal and fast  
- easy to install anywhere  
- suitable for research and production  
- extendable and open-source  

## Features

### Core Capabilities

- **Coherence Scoring**  
  Measures similarity between consecutive sentences to estimate textual flow.

- **Reference-Free Perplexity**  
  Character-level n-gram perplexity that works without any pretrained models.

- **Groundedness and Factuality Checks**  
  Compares model output against reference context for basic factual alignment.

- **Latency Measurement**  
  Simple utilities to benchmark model inference time.

- **Token Statistics**  
  Word count, character count, and approximate token usage.

- **Command Line Interface (CLI)**  
  Evaluate text files directly in the terminal.

### Why it is lightweight

- Zero heavy dependencies  
- No transformers, no GPU required  
- Pure Python implementation  

## Quick Start

Install from PyPI:

```
pip install llm-metrics-lite
```

Install from source:

```
git clone https://github.com/supriyabachal/llm_metrics_lite.git
cd llm_metrics_lite
pip install -e .
```

## Examples

### Basic Python Usage

```python
from llm_metrics_lite import train_default_perplexity_model, evaluate_output

corpus = [
    "Artificial intelligence enables machines to learn from data.",
    "Language models process and generate human-like text."
]

model = train_default_perplexity_model(corpus)

output = "Generative AI models help automate reasoning tasks."
context = "AI systems can understand language and produce responses."

result = evaluate_output(
    output_text=output,
    context_text=context,
    perplexity_model=model
)

print(result)
```

## CLI Usage

Evaluate output text:

```
llm-metrics-lite evaluate output.txt
```

Evaluate with context reference:

```
llm-metrics-lite evaluate output.txt --context reference.txt
```

```
llm-metrics-lite --help
```

## Roadmap

Planned enhancements include:

- Embedding-based coherence evaluation  
- Semantic groundedness metrics  
- Batch evaluation support  
- Model-output comparison tools  
- Evaluation dashboard and visualizations  
- Integration helpers for RAG pipelines  



Show help:

```
llm-metrics-lite --help
```

