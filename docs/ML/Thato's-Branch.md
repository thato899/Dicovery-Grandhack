# SafeRoute AI Wiki

Welcome to the SafeRoute AI documentation wiki. This wiki contains comprehensive documentation for the Machine Learning component of the SafeRoute AI project.

## Quick Navigation

- [ML Architecture Overview](ML-Architecture-Overview)
- [Setup & Installation](Setup-Installation)
- [Data Models & Schemas](Data-Models-Schemas)
- [Feature Engineering](Feature-Engineering)
- [Model Training](Model-Training)
- [Model Evaluation](Model-Evaluation)
- [Pathfinding Engine](Pathfinding-Engine)
- [ONNX Export](ONNX-Export)
- [API Contracts](API-Contracts)
- [Testing Guide](Testing-Guide)
- [MLOps Strategy](MLOps-Strategy)
- [Troubleshooting](Troubleshooting)

## Project Overview

SafeRoute AI uses machine learning to predict risk scores for streets and neighborhoods in South African urban areas, providing safer walking routes instead of simply the shortest route.

### Key Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| Risk Prediction | XGBoost | Predict street safety scores (0-4) |
| Feature Engineering | Python/Pandas | Transform raw data into ML features |
| Pathfinding | NetworkX/A* | Calculate safest routes |
| Model Export | ONNX | Mobile deployment |

### Risk Categories

| Score | Level | Description |
|-------|-------|-------------|
| 0 | Safe | No significant risks |
| 1 | Low Risk | Minor concerns |
| 2 | Medium Risk | Exercise caution |
| 3 | High Risk | Avoid if possible |
| 4 | Extreme Risk | Do not use |

## Team Contact

- **ML Engineer**: Thato Maluleka
- **Repository**: https://github.com/thato899/Dicovery-Grandhack