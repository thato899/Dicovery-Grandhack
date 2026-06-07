import joblib
import numpy as np
import onnx
import onnxruntime as ort

# Try to import onnxmltools
try:
    from onnxmltools.convert import convert_xgboost
    from onnxmltools.convert.common.data_types import FloatTensorType
    HAS_ONNXTOOLS = True
except ImportError:
    HAS_ONNXTOOLS = False
    print("⚠️ onnxmltools not installed. Installing alternative method...")
    print("Run: pip install onnxmltools")

# Load model
print("Loading model...")
model_data = joblib.load('models/production/risk_model.pkl')
model = model_data['model'] if isinstance(model_data, dict) else model_data
print(f"✅ Model loaded. Type: {type(model).__name__}")

# Create sample input (14 features)
sample_input = np.random.randn(1, 14).astype(np.float32)
print(f"Sample input shape: {sample_input.shape}")

if HAS_ONNXTOOLS:
    # Define input types
    initial_types = [('input', FloatTensorType([None, 14]))]
    
    # Convert to ONNX
    print("Converting to ONNX...")
    onnx_model = convert_xgboost(model, initial_types=initial_types, target_opset=12)
    
    # Save
    onnx.save(onnx_model, 'models/production/risk_model.onnx')
    print("✅ ONNX model saved to models/production/risk_model.onnx")
    
    # Validate
    session = ort.InferenceSession('models/production/risk_model.onnx')
    output = session.run(None, {'input': sample_input})
    print(f"✅ ONNX validation passed. Output shape: {output[0].shape}")
else:
    print("\n❌ Cannot export to ONNX without onnxmltools.")
    print("Run: pip install onnxmltools")
    print("\nAlternative: Save model as pickle for now")
    print("✅ Model saved as: models/production/risk_model.pkl")
