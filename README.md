# SafeRoute AI

### AI-Powered Community Safety Navigation for South Africa

[![Discovery Gradhack 2026](https://img.shields.io/badge/Discovery-Gradhack%202026-blue)](https://github.com/thato899/Dicovery-Grandhack)
[![React Native](https://img.shields.io/badge/React%20Native-0.81.5-61DAFB)](https://reactnative.dev/)
[![Expo](https://img.shields.io/badge/Expo-49.0.23-000020)](https://expo.dev/)
[![Firebase](https://img.shields.io/badge/Firebase-latest-FFCA28)](https://firebase.google.com/)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.x-orange)](https://xgboost.ai/)

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
7. Branch Strategy & Git Workflow
8. Setup Instructions by Role
9. Core Features
10. System Architecture
11. UML Diagrams
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

### Thato Maluleka — Project Lead and Mobile Developer

**GitHub Branch:** `Thato`  
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

### Treasure Ramatshila — Backend Developer

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

### Bongani Mahlangu — Machine Learning Engineer

**GitHub Branch:** `ml-engine`  
**Primary Folder:** `ml/`

#### Responsibilities

- Risk prediction model development
- Crime data preprocessing
- Feature engineering
- A* pathfinding and risk weighting
- ONNX export
- Model evaluation and monitoring

#### Deliverables

- Trained XGBoost model
- ONNX mobile model
- Pathfinding algorithm
- Evaluation notebooks

---

### Tharollo Sebe — UI/UX Designer and Frontend Developer

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

### Shared Integration and Testing

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

### Machine Learning

| Technology | Purpose |
|----------|----------|
| XGBoost | Risk classification |
| scikit-learn | Preprocessing |
| Pandas | Data analysis |
| NetworkX | Graph algorithms |
| ONNX Runtime | Mobile inference |

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
│   └── SafeRouteAI/
│       ├── app/
│       │   ├── screens/
│       │   ├── components/
│       │   ├── services/
│       │   ├── hooks/
│       │   ├── utils/
│       │   ├── types/
│       │   └── styles/
│       ├── config/
│       ├── assets/
│       ├── App.tsx
│       ├── package.json
│       └── tsconfig.json
│
├── backend/
│   ├── src/
│   │   ├── routes/
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── middleware/
│   │   ├── services/
│   │   └── utils/
│   ├── tests/
│   ├── package.json
│   └── tsconfig.json
│
├── ml/
│   ├── data/
│   ├── notebooks/
│   ├── models/
│   ├── training/
│   ├── src/
│   └── requirements.txt
│
├── frontend-ui/
│   ├── design/
│   ├── components/
│   ├── screens/
│   └── figma/
│
├── docs/
│   ├── api/
│   ├── architecture/
│   └── user-guide/
│
├── .github/
│   └── workflows/
│
├── README.md
├── CONTRIBUTING.md
└── .gitignore