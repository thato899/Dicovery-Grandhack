# SafeRoute AI

### AI-Powered Community Safety Navigation for South Africa

[![Discovery Gradhack 2026](https://img.shields.io/badge/Discovery-Gradhack%202026-blue)](https://github.com/thato899/Dicovery-Grandhack)
[![React Native](https://img.shields.io/badge/React%20Native-0.81.5-61DAFB)](https://reactnative.dev/)
[![Expo](https://img.shields.io/badge/Expo-49.0.23-000020)](https://expo.dev/)
[![Firebase](https://img.shields.io/badge/Firebase-latest-FFCA28)](https://firebase.google.com/)
[![XGBoost](https://img.shields.io/badge/XGBoost-3.2.0-orange)](https://xgboost.ai/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB)](https://python.org/)

**Event:** Discovery Gradhack 2026  
**Theme:** AI for Safer Communities (Theme 3)  
**Repository:** https://github.com/thato899/Dicovery-Grandhack

---

## Table of Contents

1. Executive Summary
2. Problem Statement
3. Solution Overview
4. Team Members & Responsibilities
5. Technology Stack
6. Project Structure
7. ML System Highlights (NEW)
8. Branch Strategy & Git Workflow
9. Setup Instructions by Role
10. Core Features
11. System Architecture
12. API Documentation
13. Database Schema
14. Machine Learning Pipeline
15. Development Timeline
16. Testing Strategy
17. Deployment Guide
18. Risk Mitigation
19. Deliverables
20. License & Contact

---

## Executive Summary

SafeRoute AI is a mobile navigation application that prioritizes safety over speed for pedestrians in urban South African areas. Unlike traditional GPS applications that only consider distance and traffic, SafeRoute AI integrates:

- Historical crime data analytics
- Real-time community incident reports
- Street lighting conditions
- Crowd movement patterns
- Emergency response integration with Discovery Health

The application uses machine learning to predict risk scores for street blocks and employs the A* pathfinding algorithm with risk-weighted edges to recommend the safest route. It includes collision detection that automatically alerts emergency services and community-driven risk mapping that improves over time.

### Target Users

- University students
- Night-shift workers
- Delivery drivers
- Tourists
- General pedestrians

### Geographic Focus

- Johannesburg
- Cape Town
- Durban
- Pretoria

### Expected Impact

- 40% reduction in emergency response time
- 60% improvement in perceived safety for night commuters
- Increased community participation through incentive-based reporting

---

## Problem Statement

| Current Reality | Gap | Impact |
|----------------|-----|--------|
| Navigation apps prioritize shortest or fastest routes | No pedestrian safety scoring | Users may walk through dangerous areas |
| Crime follows time and location patterns | Crime data is not integrated into route planning | Preventive insights are unused |
| Communities know dangerous areas | No platform to share this information | Local knowledge is lost |
| Emergency response may be delayed | No automatic intelligent alerting | Delayed medical assistance |
| Many South Africans avoid walking after dark | No safety-first navigation tool | Reduced mobility and quality of life |

---

## Solution Overview

SafeRoute AI combines four major systems.

### 1. Safe Route Recommendation Engine

- Machine learning predicts a risk score for each street segment
- Features include crime density, lighting, time, and recent reports
- A* pathfinding calculates the safest route
- Comparison between shortest and safest routes

### 2. Collision Detection and Emergency Response

- Accelerometer detects collisions and sudden impact
- Automatic emergency alerts are triggered
- GPS coordinates are sent to responders
- Unresponsive users are automatically escalated

### 3. Community Risk Intelligence

- Users submit incident reports
- Reports decay over time
- Anonymous crowd data improves predictions
- Incentive system encourages participation

### 4. Discovery Health Integration

- Ambulance dispatch and ETA
- Family notifications
- Hospital and bed availability
- Medical profile access for responders

---

## Team Members & Responsibilities

### Zinhle Sibisi — Project Lead and Mobile Developer

**GitHub Branch:** `main`  
**Primary Folder:** `mobile-app/SafeRouteAI/`

#### Responsibilities

- React Native application architecture
- GPS and map integration
- Safe route visualization
- Collision detection
- Emergency SOS implementation
- Mobile performance optimization
- Code reviews and merge management

#### Deliverables

- Mobile application
- Navigation screens
- Emergency screen
- Sensor integration
- Production-ready Expo build

---

### Rorisang Mokoalase — Backend Developer

**GitHub Branch:** `backend-api`  
**Primary Folder:** `backend/`

#### Responsibilities

- Firebase project configuration
- Firestore schema design
- Express REST API development
- Authentication system
- Incident reporting endpoints
- Emergency dispatch endpoints
- Data backup and persistence

#### Deliverables

- Authentication API
- Risk scoring API
- Incident reporting API
- Emergency API
- Firestore rules and indexes

---

### Thato Maluleka — Machine Learning Engineer

**GitHub Branch:** `main` / `Thato`  
**Primary Folder:** `ml/`

#### Responsibilities (✅ ALL COMPLETED)

- Risk prediction model development using XGBoost
- Crime data preprocessing and validation
- Feature engineering (14 features from raw data)
- A* pathfinding algorithm with risk weighting
- ONNX export for mobile deployment
- Model evaluation and monitoring

#### Deliverables (✅ ALL COMPLETED)

- ✅ Trained XGBoost risk model (risk_model.pkl)
- ✅ ONNX export script for mobile deployment
- ✅ Complete feature engineering pipeline
- ✅ RiskPredictor wrapper class for easy integration
- ✅ 14-page comprehensive documentation (docs/ML/)

---

### Pontsho Treasure Ramatshila — UI/UX Designer and Frontend Developer

**GitHub Branch:** `frontend-ui`  
**Primary Folder:** `frontend-ui/`

#### Responsibilities

- Design system and branding
- Component library
- Screen layouts
- Accessibility compliance
- Loading and error states
- Responsive design

#### Deliverables

- Figma prototype
- Design tokens
- Component library
- High-fidelity screens

---

### Bongani Mahlangu — Integration and Testing Lead

**GitHub Branch:** `integration`

#### Responsibilities

- Continuous integration
- Unit and end-to-end testing
- API contract validation
- Performance benchmarking
- Deployment coordination
- Documentation maintenance

---

## Technology Stack

### Mobile Application

| Technology | Version | Purpose |
|----------|----------|----------|
| React Native | 0.81.5 | Mobile development |
| Expo | 49.0.23 | Development platform |
| React Native Maps | 1.27.2 | Map rendering |
| Expo Location | Latest | GPS services |
| Expo Sensors | Latest | Accelerometer |
| React Navigation | 6.x | Screen navigation |
| TensorFlow Lite | Latest | On-device inference |

### Backend

| Technology | Purpose |
|----------|----------|
| Firebase | Backend services |
| Firestore | NoSQL database |
| Firebase Auth | Authentication |
| Cloud Functions | Serverless API |
| Express.js | REST API |
| Twilio | SMS alerts |

### Machine Learning (✅ COMPLETED)

| Technology | Version | Purpose |
|----------|----------|----------|
| XGBoost | 3.2.0 | Risk classification ✅ |
| scikit-learn | 1.4.0 | Preprocessing ✅ |
| Pandas | 3.0.3 | Data analysis ✅ |
| NumPy | 2.4.6 | Numerical operations ✅ |
| NetworkX | 3.6.1 | Graph algorithms ✅ |
| ONNX Runtime | 1.26.0 | Mobile inference ✅ |
| BallTree | - | Geospatial queries ✅ |

### DevOps and Quality

| Technology | Purpose |
|----------|----------|
| Git | Version control |
| GitHub Actions | CI/CD |
| Jest | Unit testing |
| Cypress | End-to-end testing |
| ESLint | Code quality |
| Prettier | Code formatting |

---

## Project Structure

```text
Dicovery-Grandhack/
│
├── mobile-app/
│   └── SafeRouteAI/          # React Native mobile app
│
├── backend/                   # Express/Firebase backend
│
├── ml/                        # ✅ MACHINE LEARNING (COMPLETED)
│   ├── src/
│   │   ├── data/             # Pydantic data schemas
│   │   ├── features/         # Feature engineering (14 features)
│   │   ├── models/           # XGBoost risk model
│   │   ├── pathfinding/      # A* algorithm (ready)
│   │   └── api/              # API contracts
│   ├── scripts/              # Training, test, export scripts
│   ├── data/                 # Raw and processed data
│   ├── models/               # Trained models (.pkl, .onnx)
│   ├── notebooks/            # Jupyter notebooks
│   └── requirements.txt      # Python dependencies
│
├── frontend-ui/              # Web UI components
│
├── docs/
│   ├── ML/                   # ✅ COMPLETE ML DOCUMENTATION
│   │   ├── Home.md
│   │   ├── ML-Architecture-Overview.md
│   │   ├── Setup-Installation.md
│   │   ├── Data-Models-Schemas.md
│   │   ├── Feature-Engineering.md
│   │   ├── Model-Training.md
│   │   ├── Model-Evaluation.md
│   │   ├── Pathfinding-Engine.md
│   │   ├── ONNX-Export.md
│   │   ├── API-Contracts.md
│   │   ├── Testing-Guide.md
│   │   ├── MLOps-Strategy.md
│   │   └── Troubleshooting.md
│   ├── api/
│   └── architecture/
│
├── .github/
│   └── workflows/
│
├── README.md
└── .gitignore