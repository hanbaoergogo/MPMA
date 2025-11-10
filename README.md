# MPMA: Preference Manipulation Attack Against Model Context Protocol

This repository contains the implementation of **MPMA**, a novel attack that manipulates the preference behavior of LLM agents under the **Model Context Protocol (MCP)**. The attack is designed to increase the likelihood of a malicious server being selected by the base LLM.

## Environment

To ensure reproducibility and consistency across experiments, all dependencies are managed through a dedicated **Conda environment** configuration file (`environment.yml`).  
This environment encapsulates both the core Python runtime and all required third-party packages for model training, evaluation, and analysis.

### 🔧 Environment Setup

1. **Create the environment**
   ```bash
   conda env create -f environment.yml
   ```
This command installs all packages listed in the YAML file and creates a Conda environment named mpma (as defined under the name field).

2. **Activate the environment**
    ```
    conda activate mpma
    ```

3. (Optional) Specify a custom installation path
If you prefer to install the environment in a custom directory, you can modify the prefix field in the YAML file.
For example:

    ```
    prefix: /home/username/envs/mpma 
    ```


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
├── utils.py                    # Utility functions used across modules
└── environment.yml             # Environment Setup
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

```
@article{wang2025mpma,
  title={MPMA: Preference Manipulation Attack Against Model Context Protocol},
  author={Wang, Zihan and Li, Hongwei and Zhang, Rui and Liu, Yu and Jiang, Wenbo and Fan, Wenshu and Zhao, Qingchuan and Xu, Guowen},
  journal={arXiv preprint arXiv:2505.11154},
  year={2025}
}
```

## License

This project is released under the MIT License. See `LICENSE` for details.
