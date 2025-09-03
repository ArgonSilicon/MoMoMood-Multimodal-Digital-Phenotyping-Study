# MoMoMood_survival_analysis
Survival analysis conducted for MoMoMood study, introduced in [1].

The analysis utilizes PHQ-9 scores as proxy for participants adherance, and uses:
1. Kapotebook introduces survivalplan-Meier estimator curves for exploratory analysis and visualizations
2. Log-Rank tests for participant group differences

Analysis is covered in a Jupyter notebook.

### Environment setup in conda/mamba
- mamba env create -f environment.yml
- mamba activate survenv

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
