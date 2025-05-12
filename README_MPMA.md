# MPMA: Preference Manipulation Attack Against Model Context Protocol

This repository contains the implementation of **MPMA**, a novel attack that manipulates the preference behavior of LLM agents under the **Model Context Protocol (MCP)**. The attack is designed to increase the likelihood of a malicious server being selected by the base LLM.

## Directory Structure

```
MPMA/
├── log/                         # Stores logs generated during execution
├── metric/                     # Contains evaluation scripts for measuring ASR, TPR, etc.
├── prompt/                     # Contains advertising prompts and stealthiness templates
├── script/                     # Helper scripts for running experiments
├── best.py                     # Run the attack using best description only (no optimization)
├── generic_optimize.py         # Run the attack using GA-enhanced optimization (w/ genetic)
├── metric.py                   # Evaluation metric definitions and interfaces
├── optimize_with_prompt.py     # Run the attack using prompt transformation (w/o genetic)
├── raw.py                      # Preprocess raw descriptions and data
├── readme.md                   # Project documentation (you are reading it)
└── utils.py                    # Utility functions used across modules
```

### 🧠 1. Best Description Only (No Optimization)

This mode uses the raw best description without applying prompt transformation or genetic algorithms.

```bash
python best.py
```

---

### ⚙️ 2. Prompt-based Optimization (w/o Genetic)

This mode applies prompt transformation to enhance stealthiness, but does not use genetic algorithms.

```bash
python optimize_with_prompt.py
```

---

### 🧬 3. GA-enhanced Optimization (w/ Genetic)

This mode performs full optimization using both advertising prompt strategies and genetic algorithms for stealthiness enhancement.

```bash
python generic_optimize.py
```

---

## Citation

If you use this codebase in your research, please cite the corresponding paper:

> **MPMA: Preference Manipulation Attack Against Model Context Protocol**  
> (Add authors and conference details here when available)

---

## License

This project is released under the MIT License. See `LICENSE` for details.
