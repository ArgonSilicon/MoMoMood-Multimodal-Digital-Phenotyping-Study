# Multimodal Digital Phenotyping Study in Patients With Major Depressive Episodes and Healthy Controls (Mobile Monitoring of Mood): Observational Longitudinal Study

This repository covers the analysis conducted in the MoMo-Mood study, introduced in [1](https://doi.org/10.2196/63622).

The analysis comprises of:
1. Survival analysis utilizing PHQ-9 scores as a proxy for participants' adherence, using:
  - Kaplan-Meier estimator curves for exploratory analysis and visualizations
  - Log-Rank tests for analyzing participant group differences
2. Analysis of the quantity and temporal patterns of smartphone usage
3. Analysis of the between-group difference in the quantity and temporal patterns of behaviors
4. Analysis of similarity in temporal rhythms of smartphone use, social activity, and physical activity within subcohorts
5. Linear mixed model analysis using sensor measures as predictors of depression severity

## 1. Project structure
```bash
├── notebooks/
│   └── MMM-survival-analysis.ipynb
├── output/
├── src/
├── LICENSE
├── README.md
├── config.yaml
├── environment.yml
└── settings.py
```
## 2. How to run
###2.1 Local execution
```bash
- mamba env create -f environment.yml
- mamba activate survenv
```
## 3. Updating the configuration


## References
1. Aledavood, T., Luong, N., Baryshnikov, I., Darst, R., Heikkilä, R., Holmén, J., ... & Isometsä, E. (2025). Multimodal digital phenotyping study in patients with major depressive episodes and healthy controls (mobile monitoring of mood): Observational longitudinal study. JMIR Mental Health, 12, e63622 [doi: 10.2196/63622](https://doi.org/10.2196/63622).

![Survival](https://img.shields.io/badge/analysis-survival%20curves-blueviolet)
![Python](https://img.shields.io/badge/python-3.11-blue)
![lifelines](https://img.shields.io/badge/lifelines-0.30-orange)
![License](https://img.shields.io/github/license/digitraceslab/MoMoMood_survival_analysis)
![Last Commit](https://img.shields.io/github/last-commit/digitraceslab/MoMoMood_survival_analysis)
![DOI](https://img.shields.io/badge/DOI-10.2196%2F63622-blue)
![Mood](https://img.shields.io/badge/mood-happy-green)
![Coffee](https://img.shields.io/badge/coffee-strong-brown)
