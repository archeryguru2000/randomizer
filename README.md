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

- **Generic by design** — no domain‑specific assumptions  
- **Reproducible outputs** via `--seed`  
- **Configurable numeric precision** via `--ndp`  
- **Shell‑friendly range parsing** (`nargs=2` works in PowerShell, Bash, zsh, CMD)  
- Zero side effects at import time  
- Simple, composable, and easy to extend  

---

## 📦 Installation

Place `randomizer.py` in your project folder:


## 📄 License
This utility is designed for free and open educational use.
You may incorporate it into teaching materials, assignments, generators, or research tools.

## 🤝 Contributing
If you want to extend this module (Gaussian generators, discrete sampling, symbolic placeholders, etc.), feel free to fork and submit pull requests.

## 📬 Contact
Created as part of a suite of engineering education tools.