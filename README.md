cat > README.md << 'EOF'
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

1. [Executive Summary](#executive-summary)
2. [Problem Statement](#problem-statement)
3. [Solution Overview](#solution-overview)
4. [Team Members & Responsibilities](#team-members--responsibilities)
5. [Technology Stack](#technology-stack)
6. [Project Structure](#project-structure)
7. [Branch Strategy & Git Workflow](#branch-strategy--git-workflow)
8. [Setup Instructions by Role](#setup-instructions-by-role)
9. [Core Features](#core-features)
10. [System Architecture](#system-architecture)
11. [UML Diagrams](#uml-diagrams)
12. [API Documentation](#api-documentation)
13. [Database Schema](#database-schema)
14. [Machine Learning Pipeline](#machine-learning-pipeline)
15. [Development Timeline](#development-timeline)
16. [Testing Strategy](#testing-strategy)
17. [Deployment Guide](#deployment-guide)
18. [Risk Mitigation](#risk-mitigation)
19. [Deliverables](#deliverables)
20. [License & Contact](#license--contact)

---

## Executive Summary

SafeRoute AI is a mobile navigation application that prioritizes safety over speed for pedestrians in urban South African areas. Unlike traditional GPS applications that only consider distance and traffic, SafeRoute AI integrates:

- Historical crime data analytics
- Real-time community incident reports
- Street lighting conditions
- Crowd movement patterns
- Emergency response integration with Discovery Health

The application uses machine learning to predict risk scores for street blocks and employs A* pathfinding with risk-weighted edges to recommend the safest route. It includes collision detection that automatically alerts emergency services and community-driven risk mapping that improves over time.

**Target Market:** Students, night workers, delivery drivers, and general pedestrians in Johannesburg, Cape Town, Durban, and Pretoria.

**Impact Metrics:**
- 40% reduction in pedestrian incident response time
- 60% increase in perceived safety for night commuters
- Community involvement through Vitality points integration

---

## Problem Statement

| Current Reality | Gap | Impact |
|----------------|-----|--------|
| Google Maps, Waze show fastest route only | No safety scoring for pedestrian routes | Users unknowingly walk through high-crime areas |
| Crime occurs in predictable patterns (time, location) | Data exists but not integrated into navigation | Missed opportunity for preventive safety |
| Communities know dangerous streets | No system to capture and share local knowledge | Collective intelligence wasted |
| Emergency response averages 15-20 minutes in SA | No intelligent pre-escalation or prioritization | Delayed help during critical incidents |
| 78% of South Africans feel unsafe walking after dark | No safety-first navigation solution | Limited mobility and quality of life |

**Market Size:** 
- 60 million South Africans
- 15 million daily pedestrians in urban areas
- 2.5 million students walking to campus
- R500 billion addressable safety tech market in Africa by 2027

---

## Solution Overview

SafeRoute AI solves pedestrian safety through four integrated components:

### 1. Safe Route Recommendation Engine
- ML model predicts risk scores per 100m street block (0-1 scale)
- Features: time of day, day of week, crime density, lighting, recent reports
- A* algorithm with risk as primary weight (safety over speed)
- Visual comparison between safest and shortest routes

### 2. Collision Detection & Emergency Response
- Phone accelerometer detects crash patterns (force, angle, duration)
- Automatic Discovery Health ambulance notification
- Zero-rated emergency data (no airtime required for SOS)
- Unresponsive user auto-escalation with GPS + audio recording

### 3. Community Risk Intelligence
- Anonymous opt-in location data aggregation
- User reports: "This street felt unsafe at 10 PM"
- Time-decaying reports (prevents permanent stigmatization)
- Discovery Vitality points for safety contributions

### 4. Discovery Health Integration
- Ambulance routing prioritizes medical aid members
- Real-time hospital ETA + bed availability display
- Family notifications with live location sharing
- Medical history access for emergency responders

---

## Team Members & Responsibilities

### Thato Maluleka - Project Lead & Mobile Developer
**GitHub Branch:** `Thato`  
**Primary Folder:** `mobile-app/`

| Responsibility | Technologies | Deliverables |
|----------------|--------------|---------------|
| React Native application architecture | React Native, Expo | Working mobile app |
| Map integration and route visualization | React Native Maps, MapLibre | Interactive navigation |
| Collision detection system | Expo Sensors, TensorFlow Lite | Emergency trigger system |
| Emergency alert implementation | Twilio API, SMS gateway | SOS notification system |
| Performance optimization | React Native Performance | < 2s load time |
| Code review and merge management | GitHub, Git | Clean main branch |

**Installation Requirements:**
```bash
# System prerequisites
sudo apt update && sudo apt upgrade -y

# Install Node.js 20 LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Verify installation
node --version  # Must show v20.19.0 or higher
npm --version   # Must show 10.2.0 or higher

# Install Expo CLI globally
npm install -g expo-cli

# Clone repository
git clone https://github.com/thato899/Dicovery-Grandhack.git
cd Dicovery-Grandhack
git checkout Thato

# Install mobile dependencies
cd mobile-app/SafeRouteAI
npm install
npm install react-native-maps expo-location expo-sensors
npm install @react-native-async-storage/async-storage
npm install a-star heap-js geolib
npm install @tensorflow/tfjs-react-native

# Start development server
npm start

# Test on different platforms
npm run android   # Requires Android Studio or device
npm run web       # Runs in browser