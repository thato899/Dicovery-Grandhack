

---



## Page 6: Troubleshooting



```markdown

# Troubleshooting Guide



## Common Issues & Solutions



### Issue 1: Git Authentication Failed



**Error:**

remote: Invalid username or token

fatal: Authentication failed



text



**Cause:** GitHub no longer accepts passwords.



**Solution:**

```bash

# Use Personal Access Token

git clone https://thato899:YOUR_TOKEN_HERE@github.com/thato899/Dicovery-Grandhack.git



# Or use SSH

git clone git@github.com:thato899/Dicovery-Grandhack.git

Issue 2: ImportError: No module named 'xgboost'

Error:



text

ModuleNotFoundError: No module named 'xgboost'

Cause: Dependencies not installed or virtual environment not activated.



Solution:



bash

# Activate virtual environment

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows



# Install dependencies

pip install -r requirements.txt

Issue 3: MemoryError during training

Error:



text

MemoryError: Unable to allocate array

Cause: Dataset too large for available RAM.



Solution:



python

# Use chunking

for chunk in pd.read_csv('large_file.csv', chunksize=10000):

    process(chunk)



# Or reduce feature size

X = X.astype('float32')  # Half the memory



# Or use subsample

params['subsample'] = 0.5  # Use 50% of data

Issue 4: ONNX Export Fails

Error:



text

RuntimeError: Unsupported operator type

Cause: XGBoost version incompatible with ONNX.



Solution:



bash

# Use specific compatible versions

pip install xgboost==1.7.6

pip install onnxmltools==1.12.0

pip install onnx==1.14.0



# Or use older opset

convert_xgboost(model, initial_types, target_opset=11)

Issue 5: No Path Found

Error:



text

ValueError: No path found between start and end

Cause: Graph is disconnected or nodes too far apart.



Solution:



python

# Check graph connectivity

import networkx as nx

print(f"Graph connected: {nx.is_connected(graph)}")



# Get connected components

components = list(nx.connected_components(graph))

print(f"Number of components: {len(components)}")



# Increase search radius

nearest_node = find_nearest_node(lat, lon, max_distance=1000)  # 1km

Issue 6: Poor Model Performance

Error:



text

F1 Score: 0.65 (below threshold)

Causes & Solutions:



Cause	Solution

Not enough data	Collect more or use data augmentation

Class imbalance	Use SMOTE or class weights

Wrong features	Add new features, remove noisy ones

Overfitting	Reduce max_depth, increase regularization

python

# Fix class imbalance

from imblearn.over_sampling import SMOTE

smote = SMOTE()

X_balanced, y_balanced = smote.fit_resample(X, y)



# Fix overfitting

params = {

    'max_depth': 4,        # Reduce

    'reg_alpha': 0.5,      # Increase

    'reg_lambda': 0.5,     # Increase

    'subsample': 0.7       # Reduce

}

Issue 7: Slow Inference

Error:



text

Prediction latency: 250ms (too slow)

Solutions:



python

# Use quantized model

quantized_model = convert_to_onnx(model, quantize=True)

# 1.2ms → 0.8ms



# Batch predictions

batch_results = model.predict(batch_locations)

# 250ms × 100 → 500ms (5x faster per item)



# Use smaller model

params['n_estimators'] = 100  # Reduce from 200

params['max_depth'] = 4        # Reduce from 6

Issue 8: Data Validation Fails

Error:



text

ValidationError: latitude must be between -90 and 90

Cause: Invalid coordinates in input.



Solution:



python

# Fix in preprocessing

def fix_coordinates(df):

    df['latitude'] = df['latitude'].clip(-90, 90)

    df['longitude'] = df['longitude'].clip(-180, 180)

    return df



# Or filter out bad data

df = df[(df['latitude'].between(-90, 90)) & 

        (df['longitude'].between(-180, 180))]

Getting Help

1. Check Logs

bash

tail -f logs/training.log

tail -f logs/api.log

2. Run Debug Mode

bash

python scripts/run_training.py --debug



# Or set log level

import logging

logging.basicConfig(level=logging.DEBUG)

3. Test Individual Components

bash

# Test data loading only

python -c "from src.data.loaders import load_data; load_data('test')"



# Test model loading

python -c "from src.models.risk_model import RiskModel; m = RiskModel(); m.load('model.pkl')"

4. Open GitHub Issue

Go to: https://github.com/thato899/Dicovery-Grandhack/issues



Include:



Error message



What you tried



Environment (Python version, OS)



Relevant code snippet



Quick Diagnostic Script

python

# diagnostic.py



import sys

import platform



def run_diagnostic():

    print("=" * 50)

    print("SafeRoute AI Diagnostic")

    print("=" * 50)

    

    # Python version

    print(f"Python: {sys.version}")

    

    # OS

    print(f"OS: {platform.system()} {platform.release()}")

    

    # Check imports

    packages = ['xgboost', 'sklearn', 'pandas', 'numpy', 'networkx', 'onnx']

    for pkg in packages:

        try:

            __import__(pkg)

            print(f"✅ {pkg}")

        except ImportError:

            print(f"❌ {pkg}")

    

    # Check folders

    import os

    folders = ['data/raw', 'src', 'tests', 'models']

    for folder in folders:

        if os.path.exists(folder):

            print(f"✅ {folder}/")

        else:

            print(f"❌ {folder}/")

    

    # GPU availability

    try:

        import torch

        print(f"GPU Available: {torch.cuda.is_available()}")

    except:

        print("⚠️ PyTorch not installed (GPU check skipped)")



if __name__ == "__main__":

    run_diagnostic()

bash

# Run diagnostic

python diagnostic.py

Last updated: June 2026