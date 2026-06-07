<html>
<body>
<!--StartFragment--><html><head></head><body><h1>ML Architecture Overview</h1><h2>System Architecture</h2><pre><code class="language-mermaid">flowchart TD

    A[Crime Data] --&gt; D[Feature Engineering]
    B[Community Reports] --&gt; D
    C[Environmental Data] --&gt; D

    D --&gt; E[Feature Store]

    E --&gt; F[XGBoost Training Pipeline]

    F --&gt; G[Model Evaluation]
    G --&gt; H[Model Export]

    H --&gt; I[risk_model.pkl]
    H --&gt; J[risk_model.onnx]

    J --&gt; K[Mobile Inference]

    K --&gt; L[Risk Prediction Engine]

    L --&gt; M[Risk-Aware A* Pathfinding]

    M --&gt; N[Safe Route Recommendation]
</code></pre><hr><h2>High-Level Data Flow</h2><pre><code class="language-mermaid">flowchart LR

    A[Raw Data] --&gt; B[Feature Engineering]

    B --&gt; C[Model Training]

    C --&gt; D[Model Export]

    D --&gt; E[Pathfinding Engine]

    E --&gt; F[Safe Route Generation]
</code></pre><hr><h2>ML Pipeline Overview</h2><pre><code class="language-mermaid">flowchart TD

    A[Crime Data]
    B[Community Reports]
    C[Environmental Data]

    A --&gt; D[Data Validation]
    B --&gt; D
    C --&gt; D

    D --&gt; E[Data Cleaning]

    E --&gt; F[Feature Engineering]

    F --&gt; G[Train Validation Test Split]

    G --&gt; H[XGBoost Training]

    H --&gt; I[Cross Validation]

    I --&gt; J[Model Evaluation]

    J --&gt; K[Export Model]

    K --&gt; L[ONNX Runtime]

    K --&gt; M[Pickle Model]
</code></pre><hr><h2>Risk Prediction Workflow</h2><pre><code class="language-mermaid">sequenceDiagram

    participant User
    participant MobileApp
    participant ONNXModel
    participant Pathfinder

    User-&gt;&gt;MobileApp: Request Route

    MobileApp-&gt;&gt;ONNXModel: Features

    ONNXModel--&gt;&gt;MobileApp: Risk Score

    MobileApp-&gt;&gt;Pathfinder: Route + Risk Scores

    Pathfinder--&gt;&gt;MobileApp: Safest Route

    MobileApp--&gt;&gt;User: Route Recommendation
</code></pre><hr><h1>Data Flow Explanation</h1>
Step | Name | Description
-- | -- | --
1 | Data Collection | Gather crime records, community reports, and environmental information
2 | Feature Engineering | Convert raw data into machine-learning features
3 | Model Training | Train XGBoost to predict safety risk levels
4 | Model Export | Export the trained model to ONNX and Pickle formats
5 | Pathfinding | Use risk-aware A* to determine safer routes

<hr><h1>Risk-Aware Pathfinding</h1><p>The route score combines:</p><pre><code class="language-text">Route Score =
Distance Weight
+ Crime Weight
+ Crowd Density Weight
+ Lighting Weight
+ Community Report Weight
</code></pre><p>Example:</p><pre><code class="language-text">Shortest Route:
A -&gt; B -&gt; E -&gt; G
Risk Score = 10

Safest Route:
A -&gt; D -&gt; E -&gt; G
Risk Score = 9
</code></pre><p>The system dynamically recalculates routes whenever risk conditions change.</p><hr><h1>API Contract</h1><h2>Request</h2><pre><code class="language-json">{
  "latitude": -26.2041,
  "longitude": 28.0473,
  "timestamp": "2026-06-01T18:00:00Z",
  "crowd_density": 0.65,
  "lighting_score": 0.80
}
</code></pre><h2>Response</h2><pre><code class="language-json">{
  "risk_score": 2,
  "confidence": 0.91,
  "risk_level": "Medium Risk"
}
</code></pre><hr><h1>Quick Start</h1><h2>Setup</h2><pre><code class="language-bash">git clone https://github.com/thato899/Dicovery-Grandhack.git

cd Dicovery-Grandhack/ml

python -m venv venv

source venv/bin/activate
</code></pre><p>Windows:</p><pre><code class="language-powershell">venv\Scripts\activate
</code></pre><p>Install dependencies:</p><pre><code class="language-bash">pip install -r requirements.txt
</code></pre><hr><h2>Train Model</h2><pre><code class="language-bash">python scripts/run_training.py
</code></pre><hr><h2>Export ONNX Model</h2><pre><code class="language-bash">python scripts/export_model.py
</code></pre><hr><h2>Run Tests</h2><pre><code class="language-bash">pytest tests/ --cov=src
</code></pre><hr><h1>Team Integration Notes</h1><h3>Backend Team</h3><p>Focus on:</p><pre><code class="language-text">src/api/contracts.py
</code></pre><p>Provides:</p><ul><li><p>Request schemas</p></li><li><p>Response schemas</p></li><li><p>Model integration contracts</p></li></ul><h3>Mobile Team</h3><p>Use:</p><pre><code class="language-text">models/production/risk_model.onnx
</code></pre><p>Input:</p><ul><li><p>Feature vector</p></li></ul><p>Output:</p><ul><li><p>Risk classification</p></li><li><p>Confidence score</p></li></ul><h3>QA Team</h3><p>Run:</p><pre><code class="language-bash">pytest tests/ --cov=src
</code></pre><p>Coverage target:</p><pre><code class="language-text">90%+
</code></pre><h3>Data Analysis Team</h3><p>Start with:</p><pre><code class="language-text">notebooks/01_exploratory_analysis.ipynb
</code></pre><p>Use notebooks for:</p><ul><li><p>Exploratory analysis</p></li><li><p>Visualization</p></li><li><p>Feature investigation</p></li></ul><hr><p><em>Last Updated: June 2026</em></p></body></html><!--EndFragment-->
</body>
</html>