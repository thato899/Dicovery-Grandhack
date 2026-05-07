# 🛡️ SafeRoute AI

> *AI-powered community safety navigation for South Africa*

**Team:** W3cod3  
**Theme:** AI for Safer Communities (Theme 3)  
**Event:** Discovery Gradhack 2026

---

## 📖 Overview

SafeRoute AI is a mobile navigation application that prioritises **safety over speed**. Unlike traditional GPS apps that only consider distance and traffic, SafeRoute AI uses historical crime data, real-time incident reports, lighting conditions, and crowd movement patterns to recommend the safest walking route from point A to point B.

**Built for:** Students, night workers, delivery drivers, and anyone walking in urban South African areas where safety is a genuine daily concern.

---

## 🎯 The Problem

| Current Reality | Gap |
|----------------|-----|
| Google Maps shows fastest route, not safest | No safety scoring for pedestrians |
| Crime happens in predictable patterns (time, place) | Data exists but isn't integrated into navigation |
| Communities know which streets are dangerous | No system to capture and share that knowledge |
| Emergency response is often delayed | No intelligent pre-escalation or ambulance routing |

**SafeRoute AI closes these gaps.**

---

## ✨ Core Features

### 1. 🗺️ Safer Route Recommendation
- Machine learning model predicts risk scores per street block (0–1)
- Features: time of day, day of week, historical crime density, lighting, recent incident reports
- A* pathfinding with risk as edge weight → safest path, not shortest

### 2. 💥 Collision Detection & Ambulance Alert
- Phone accelerometer detects crash patterns
- Automatically notifies nearest Discovery-affiliated ambulance
- Zero-rated emergency data (no airtime required for SOS)
- Fallback: if user unresponsive → auto-escalate + GPS + audio recording

### 3. 🚁 Drone First Responder Integration
- For high-priority incidents (car crash, assault, fire)
- Dispatch nearest drone to stream video to emergency services before they arrive
- Real-time feedback to caller: *"Drone en route, ETA 2 mins"*

### 4. 🏥 Discovery Health Integration
- Ambulance routing prioritises Discovery medical aid members
- Hospital ETA + bed availability shown during transit
- Family notifications with live location sharing

### 5. 📊 Community-Driven Risk Mapping
- Anonymous opt-in location data
- Users can report: *"This street felt unsafe at 10 PM"*
- Reports decay over time (prevents permanent stigmatisation)
- Discovery Vitality points for contributing to community safety

---

## 🧠 AI Models Used

| Model | Purpose | Tech Stack |
|-------|---------|-------------|
| XGBoost / Random Forest | Risk score prediction (tabular: time, location, crime history) | Python, scikit-learn, ONNX |
| Lightweight CNN (TinyML) | Collision detection from accelerometer | TensorFlow Lite, on-device |
| NLP (optional) | Emergency call transcription & classification | Whisper.cpp / Gemini API |
| A* Risk-Weighted Pathfinder | Route calculation with safety as cost | NetworkX + custom heuristic |

All models run **partially on-device** for privacy and offline capability.

---

## 🛠️ Tech Stack

### Frontend (Mobile)