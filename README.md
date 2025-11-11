# MPMA: Preference Manipulation Attack Against Model Context Protocol

[![arXiv](https://img.shields.io/badge/arXiv-2505.11154-b31b1b.svg)](https://arxiv.org/abs/2505.11154)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This repository contains the official implementation of **MPMA (Model Context Protocol Preference Manipulation Attack)**, a novel security research project that investigates preference manipulation vulnerabilities in LLM agents under the **Model Context Protocol (MCP)** framework.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Evaluation Metrics](#evaluation-metrics)
- [Citation](#citation)
- [License](#license)

## 🔍 Overview

The Model Context Protocol (MCP) enables LLM agents to interact with external servers and tools. This research explores how malicious actors might manipulate server descriptions to influence the agent's selection preferences. MPMA implements three attack strategies:

- **Baseline Attack**: Direct description manipulation without optimization
- **Prompt-based Attack**: LLM-driven description transformation for enhanced persuasiveness
- **GA-enhanced Attack**: Genetic algorithm optimization for balancing effectiveness and stealthiness

## ✨ Key Features

- 🎯 **Multiple Attack Modes**: Baseline, prompt-based, and GA-enhanced optimization strategies
- 🧬 **Genetic Algorithm**: Advanced optimization using mutation and crossover operations
- 🎭 **Stealth Mechanisms**: Multiple advertising strategies (exaggerated, subliminal, emotional, authority)
- 📊 **Comprehensive Metrics**: Evaluation framework for Attack Success Rate (ASR) and stealthiness
- 🔧 **Flexible Configuration**: Support for multiple LLM models and MCP server types
- 🛠️ **Eight Target Tools**: Markdown, crypto, fetch, hotnews, installer, search, time, weather

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Conda (recommended) or pip
- API keys for OpenAI/compatible LLM services

### Environment Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/MPMA.git
   cd MPMA
   ```

2. **Create the Conda environment**
   ```bash
   conda env create -f environment.yml
   conda activate mpma
   ```

3. **Configure API Keys**
   
   Edit the API configuration in the following files:
   - `generic_optimize.py` (line 55)
   - `metric.py` (line 31 and line 97)
   - `optimize_with_prompt.py` (line 44)
   - `utils.py` (line 7)
   
   Replace `"xxxxxxx"` or `"your API"` with your actual API key:
   ```python
   Skey = "your-api-key-here"
   ```

### Alternative: Manual Installation

If you prefer pip over Conda:
```bash
pip install -r requirements.txt  # Generate from environment.yml if needed
```

## 🎯 Quick Start

### 1. Run Baseline Attack (No Optimization)

Generate the best possible description without any optimization:

```bash
python best.py --tool time
```

### 2. Run Prompt-based Optimization

Apply LLM-driven transformation for persuasiveness:

```bash
python optimize_with_prompt.py --advertise exaggerated --tool time
```

### 3. Run GA-enhanced Optimization

Full optimization with genetic algorithms:

```bash
python generic_optimize.py --model gpt-4o --advertise exaggerated --tool time
```

### 4. Evaluate Results

Measure attack effectiveness and stealthiness:

```bash
python metric.py
```

## 📖 Usage

### Baseline Attack

The baseline uses raw or slightly enhanced descriptions without sophisticated optimization:

```bash
# Generate best description baseline
python best.py --tool [TOOL_NAME]

# Generate raw description baseline
python raw.py --tool [TOOL_NAME]
```

**Supported tools**: `markdown`, `crypto`, `fetch`, `hotnews`, `installer`, `search`, `time`, `weather`

### Prompt-based Optimization (w/o Genetic)

Transform descriptions using LLM-based advertising strategies:

```bash
python optimize_with_prompt.py \
    --advertise [STRATEGY] \
    --tool [TOOL_NAME]
```

**Available strategies**:
- `exaggerated`: Highlight exceptional value with engaging language
- `subliminal`: Integrate subconscious cues and psychological suggestions
- `emotional`: Embed emotional storytelling elements
- `authority`: Present as third-party expert recommendations
- `promise`: Incorporate attractive yet unverifiable claims

### GA-enhanced Optimization (w/ Genetic)

Perform advanced optimization using genetic algorithms:

```bash
python generic_optimize.py \
    --model [MODEL_NAME] \
    --advertise [STRATEGY] \
    --tool [TOOL_NAME]
```

**Parameters**:
- `--model`: LLM model for optimization (default: `gpt-4o`)
- `--advertise`: Advertising strategy (see above)
- `--tool`: Target MCP server tool

**Output**: Optimized descriptions saved to `./prompt/genetic/[advertise]_[tool].csv`

### Evaluation Metrics

Evaluate attack success rate and stealthiness across multiple judge models:

```bash
python metric.py
```

The evaluation uses five judge models:
- `gpt-4o`
- `claude-3-7-sonnet-20250219`
- `deepseek-v3`
- `gemini-2.5-pro-exp-03-25`
- `grok-3-deepsearch`

**Output**: Results saved to `./MPMA/metric/metric.csv`

## 📁 Project Structure

```
MPMA/
├── log/                         # Execution logs and debugging information
├── metric/                      # Evaluation results and analysis data
├── prompt/                      # Generated attack prompts and descriptions
│   ├── genetic/                # GA-optimized descriptions
│   └── optimize_with_prompt/   # Prompt-based optimized descriptions
├── script/                      # Utility scripts for batch processing
├── best.py                      # Baseline attack with best description
├── raw.py                       # Baseline attack with raw description
├── optimize_with_prompt.py      # Prompt-based optimization (no GA)
├── generic_optimize.py          # Full GA-enhanced optimization
├── metric.py                    # Evaluation framework
├── utils.py                     # Shared utility functions
├── environment.yml              # Conda environment specification
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## ⚙️ Configuration

### Genetic Algorithm Parameters

In `generic_optimize.py`, you can adjust:

```python
n_iter = 5           # Number of GA iterations (line 226)
pool_size = 10       # Population size (lines 89, 176)
crossover_rate = 10  # Number of crossover operations per iteration (line 208)
```

### Advertising Prompts

Customize advertising strategies by modifying the `PROMPT` dictionary in:
- `best.py` (lines 9-12)
- `generic_optimize.py` (lines 25-29)
- `optimize_with_prompt.py` (lines 21-26)
- `raw.py` (lines 20-23)

### Target Tool Descriptions

Edit the `DESCRIPTION` dictionary to add or modify tool descriptions:
- `best.py` (lines 16-25)
- `generic_optimize.py` (lines 39-48)
- `optimize_with_prompt.py` (lines 28-37)
- `raw.py` (lines 26-35)

## 📊 Evaluation Metrics

The framework evaluates:

1. **Attack Success Rate (ASR)**: Percentage of successful manipulations
2. **Stealthiness**: Detection rate by judge models
3. **Cross-model Robustness**: Performance across different LLM judges

Results are aggregated across:
- 8 target tools
- 6 attack strategies (4 GA-enhanced + 2 baselines)
- 5 judge models

## 🔬 Research Context

This project is part of academic security research investigating vulnerabilities in LLM agent systems. The findings contribute to:

- Understanding preference manipulation in multi-agent systems
- Developing defense mechanisms for MCP-based architectures
- Raising awareness about security risks in LLM ecosystems

**⚠️ Ethical Considerations**: This research is intended for defensive purposes only. Users must comply with ethical guidelines and applicable laws when using this codebase.

## 📄 Citation

If you use this codebase in your research, please cite our paper:

```bibtex
@article{wang2025mpma,
  title={MPMA: Preference Manipulation Attack Against Model Context Protocol},
  author={Wang, Zihan and Li, Hongwei and Zhang, Rui and Liu, Yu and Jiang, Wenbo and Fan, Wenshu and Zhao, Qingchuan and Xu, Guowen},
  journal={arXiv preprint arXiv:2505.11154},
  year={2025}
}
```

## 📜 License

This project is released under the [MIT License](LICENSE). See the `LICENSE` file for details.

## 🙏 Acknowledgments

We thank the open-source community and the Model Context Protocol team for their foundational work that made this research possible.

---

**Disclaimer**: This tool is provided for research and educational purposes only. The authors are not responsible for any misuse or damage caused by this program. Users must ensure compliance with all applicable laws and regulations.
