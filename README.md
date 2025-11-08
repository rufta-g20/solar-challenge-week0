# solar-challenge-week0 🌞

This project is part of the **10 Academy Artificial Intelligence Mastery Program (Week 0 Challenge)**.
[span_0](start_span)It focuses on exploring solar radiation data from **Benin, Sierra Leone, and Togo** to identify high-potential areas for solar energy production[span_0](end_span).

---

## 💡 Project Overview

[span_1](start_span)[span_2](start_span)The core objective of this challenge is to develop a strategic approach for MoonLight Energy Solutions by analyzing solar farm data to identify high-potential regions for solar installation[span_1](end_span)[span_2](end_span). This repository serves as the foundation for that analysis, demonstrating strong skills in Git, environment setup, and basic project organization.

---

## ⚙️ Environment Setup (How to Reproduce)

To clone this repository and set up the working environment on a Windows machine (using PowerShell):

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/rufta-g20/solar-challenge-week0.git](https://github.com/rufta-g20/solar-challenge-week0.git)
    cd solar-challenge-week0
    ```

2.  **Create and Activate Virtual Environment**
    This step sets up a dedicated Python environment for project dependencies.
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    Install all required Python packages (including `pandas`, `numpy`, `matplotlib`, `seaborn`) using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Analysis**
    You can now run the analysis notebooks located in the `notebooks/` folder or scripts in `scripts/`.

---

## 🗂️ Suggested Folder Structure

The project follows a standard structure to separate code, notebooks, and configuration files:

solar-challenge-week0/
├── data/              # Stores cleaned CSV files (ignored by Git)
├── notebooks/         # Jupyter notebooks for EDA and analysis
├── scripts/           # Helper Python scripts/modules
├── .github/           # Configuration files for GitHub Actions (CI)
[cite_start]├── .gitignore         # Ensures data/ and *.csv are not committed [cite: 41]
[cite_start]├── requirements.txt   # Lists Python dependencies [cite: 41]
└── README.md

---

*Author: Rufta Gaiem Weldegiorgis*
*Program: 10 Academy – AI Mastery (Week 0)*
