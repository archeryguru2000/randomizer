# randomizer.py

`randomizer.py` is a lightweight, fully generic randomization and CLI-utility module designed for use in engineering, physics, mathematics, and FE‑style problem generators. It provides:

- A **base argument parser** (`build_argparser()`) that can be extended by any problem script  
- A **uniform random number generator** (`uniform_in()`) with configurable decimal precision  
- Optional **reproducibility** via `--seed`
- Clean separation between:
  - **global randomization tools**, and  
  - **problem‑specific logic** (your FE problems, thermodynamics exercises, statics setups, probability problems, etc.)

This module is intentionally domain‑agnostic. It can be reused across any type of calculation or exam generator.

---

## ✨ Features

- **Generic by design** — no domain‑specific assumptions (temperature, mass flow, etc.)  
- **Reproducible outputs** via `--seed`  
- **Configurable numeric precision** for randomized values via `--ndp`  
- **Shell‑friendly range parsing** (`nargs=2` works in PowerShell, Bash, zsh, CMD)  
- Zero side effects at import time  
- Simple, composable, and easy to extend  

---

## 📦 Installation

Simply place `randomizer.py` in your project or utilities folder:

