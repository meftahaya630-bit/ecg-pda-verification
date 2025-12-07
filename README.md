# Hierarchical Verification Patterns in Expert ECG Interpretation

A Pushdown Automata Framework for Detecting Incomplete Diagnostic Workflows

**Authors:** SAFAR Fatima Ezzahra, ELANSARI Zineb  
**Institution:** UM6P College of Computing, Mohammed VI Polytechnic University  
**Course:** Computational Theory, Fall 2024

## Overview

This repository contains our computational theory course project analyzing expert ECG interpretation patterns using formal language theory. We model verification behavior as a context-free language and use pushdown automata to detect incomplete diagnostic workflows.

### Key Findings

- **94.3% accuracy** in detecting incomplete verification
- Expert cardiologists: **87.5% verification completeness** vs novices: **22.0%**
- Incomplete verification → **4.7x higher false-positive rate**
- Formal proof that ECG reading is **context-free but non-regular**

## Research Paper

Our full research paper is available in `docs/paper.pdf`:

*"Hierarchical Verification Patterns in Expert ECG Interpretation: A Pushdown Automata Framework for Detecting Incomplete Diagnostic Workflows"*

**Abstract:** We formalize expert ECG verification patterns as a context-free language using pushdown automata. Analysis of 630 scanpaths from PhysioNet shows experts achieve 87.5% verification completeness versus 22.0% for novices. Our PDA detects incomplete verification with 94.3% accuracy and proves correlation with diagnostic errors.

## The Formal Model

### Pushdown Automaton Specification

```
M = (Q, Σ, Γ, δ, q0, Z0, F)
```

Where:
- **Q** = {q0, q1, q2, q3, q4, q5, q6} - 7 states
- **Σ** = ECG leads, features, actions, verification symbols
- **Γ** = {Z0, Rm, Lm, Fm, Vm} - Stack alphabet
- **q0** = Initial state
- **Z0** = Initial stack symbol
- **F** = {q6} - Accepting state
- **δ** = Transition function (47 transitions)

### State Meanings

- **q0:** Initial (awaiting overview)
- **q1:** Overview completed
- **q2:** Rhythm assessment
- **q3:** Lead examination (context stacking)
- **q4:** Feature examination (nested context)
- **q5:** Verification phase (context unwinding)
- **q6:** Complete verification ✓

## Quick Start

### Installation

```bash
git clone https://github.com/YOUR-USERNAME/ecg-pda-verification.git
cd ecg-pda-verification
pip install -r requirements.txt
```

### Run the Demo

```python
python src/pda/automaton.py
```

### Example Usage

```python
from src.pda.automaton import ECGPDA

# Initialize PDA
pda = ECGPDA()

# Expert pattern (complete verification)
expert = "O R II P Q S T V1 P Q V II ✓ V1 ✓ O"
print(pda.accepts(expert))  # True

# Novice pattern (no verification)
novice = "O R II P Q V1 P"
print(pda.accepts(novice))  # False

# Compute metrics
max_depth = pda.get_max_stack_depth(expert)  # ~5 (experts)
vcs = pda.compute_vcs(expert)  # 1.0 (complete)
```

## Dataset

We used the **PhysioNet ECG Eye-Tracking Dataset**:

- 63 participants (students to expert cardiologists)
- 630 ECG interpretation sessions  
- 10 different cardiac pathologies
- Available at: https://physionet.org/content/eye-tracking-ecg/1.0.0/

**Citation:**
```bibtex
@misc{badr2022ecg,
  author = {Badr, S. and Elola, L. and Aramendi, E. and Irusta, U. and Pueyo, E. and Martínez, P.},
  title = {Eye tracking dataset for the 12-lead electrocardiogram interpretation},
  year = {2022},
  publisher = {PhysioNet},
  doi = {10.13026/kbke-6310}
}
```

## Project Structure

```
ecg-pda-verification/
├── src/
│   ├── pda/
│   │   └── automaton.py          # Main PDA implementation
│   ├── preprocessing/             # PhysioNet data processing
│   └── evaluation/                # Metrics and analysis
├── experiments/                   # Evaluation scripts
├── tests/                         # Unit tests
├── docs/
│   └── paper.pdf                 # Full research paper
├── data/
│   ├── raw/                      # PhysioNet data (download separately)
│   └── processed/                # Processed scanpaths
└── results/                      # Experimental results
```

## Key Results

### Classification Performance (Table II from paper)

| Metric | Value | 95% CI |
|--------|-------|--------|
| Accuracy | 94.3% | [89.7, 98.9] |
| Sensitivity | 91.2% | [84.8, 97.6] |
| Specificity | 97.5% | [94.1, 100.0] |
| F1-Score | 0.939 | [0.907, 0.971] |

### Verification vs Diagnostic Accuracy (Table V)

| Pattern | Correct Diagnosis | False Positive | False Negative |
|---------|------------------|----------------|----------------|
| Complete Verification | 92.5% | 7.5% | 0.0% |
| Incomplete Verification | 73.3% | 18.9% | 7.8% |
| No Verification | 58.7% | 35.2% | 6.1% |

### Stack Depth Analysis (Table IV)

| Group | Mean Depth | Std Dev | 95th Percentile |
|-------|------------|---------|-----------------|
| Experts (complete) | 5.2 | 1.1 | 7 |
| Experts (incomplete) | 3.8 | 0.9 | 5 |
| Novices | 2.1 | 0.7 | 3 |

## Theoretical Contributions

### Theorem 1: Non-Regularity

**ECG reading patterns form a context-free but non-regular language.**

**Proof:** Using the pumping lemma for regular languages, we prove that verification patterns cannot be recognized by finite automata due to balanced examination-verification structure requiring stack memory.

### Theorem 2: Time Complexity

**Recognition can be solved in O(n) time.**

**Proof:** Our PDA processes each symbol exactly once with O(1) per-symbol operations. Total: n × O(1) = O(n).

## Why Pushdown Automata?

1. **Explicit Context Representation:** Stack maintains diagnostic context
2. **Hierarchical Structure:** Overview → Rhythm → Lead → Feature
3. **Verification as Stack Unwinding:** Systematic confirmation of nested findings

### Comparison with Alternatives

| Model | Accuracy | Interpretable | Provable |
|-------|----------|---------------|----------|
| Finite Automaton | 76.3% | Yes | Yes |
| HMM (3 states) | 88.1% | No | No |
| LSTM (64 units) | 91.7% | No | No |
| **Our PDA** | **94.3%** | **Yes** | **Yes** |

## Running Tests

```bash
pytest tests/ -v
```

## Citation

If you use this work, please cite:

```bibtex
@article{safar2024ecg,
  title={Hierarchical Verification Patterns in Expert ECG Interpretation: 
         A Pushdown Automata Framework for Detecting Incomplete Diagnostic Workflows},
  author={SAFAR, Fatima Ezzahra and ELANSARI, Zineb},
  year={2024},
  institution={Mohammed VI Polytechnic University},
  course={Computational Theory}
}
```

## Acknowledgments

- **PhysioNet** for the ECG Eye-Tracking dataset
- **UM6P Computational Theory course** for project guidance
- We used Claude AI for LaTeX formatting and debugging assistance. All theoretical analysis, PDA design, and experimental work are our original contributions.

## License

MIT License - See LICENSE file for details

---

**Course Project - Computational Theory**  
Mohammed VI Polytechnic University  
Fall 2024
