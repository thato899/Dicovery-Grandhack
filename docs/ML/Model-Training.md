<html>
<body>
<!--StartFragment--><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">markdown</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">#</span> Model Training Guide</span></span>
<span></span>
<span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">##</span> What Is Model Training?</span></span>
<span></span>
<span><span class="token bold" style="font-weight: 700;"><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span><span class="token content">Model training</span><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span></span> is the process of teaching the XGBoost algorithm to predict risk scores from feature vectors.</span>
<span></span>
<span>Think of it like teaching a student:</span>
<span><span class="token list punctuation" style="color: rgb(56, 58, 66);">-</span> <span class="token bold" style="font-weight: 700;"><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span><span class="token content">Features</span><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span></span> = The textbook (information)</span>
<span><span class="token list punctuation" style="color: rgb(56, 58, 66);">-</span> <span class="token bold" style="font-weight: 700;"><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span><span class="token content">Labels</span><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span></span> = The answer key (correct risk scores)</span>
<span><span class="token list punctuation" style="color: rgb(56, 58, 66);">-</span> <span class="token bold" style="font-weight: 700;"><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span><span class="token content">Model</span><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span></span> = The student who learns the patterns</span>
<span></span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">┌─────────────────────────────────────────────────────────────────┐</span><br><span class="">│ TRAINING PROCESS │</span><br><span class="">├─────────────────────────────────────────────────────────────────┤</span><br><span class="">│ │</span><br><span class="">│ Features + Labels → XGBoost → Trained Model │</span><br><span class="">│ (What we know) (Learns) (Predicts risk) │</span><br><span class="">│ │</span><br><span class="">│ "2.3 risk score" │</span><br><span class="">│ "3.1 risk score" ┌─────┐ ┌─────────────────┐ │</span><br><span class="">│ "0.5 risk score" ───→│XGBoost│────→│ risk_model.pkl │ │</span><br><span class="">│ "4.0 risk score" └─────┘ └─────────────────┘ │</span><br><span class="">│ │</span><br><span class="">└─────────────────────────────────────────────────────────────────┘</span></p><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">text</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span></span>
<span>&gt; **Why this matters:** A well-trained model accurately predicts risk, keeping users safe.</span>
<span></span>
<span>---</span>
<span></span>
<span>## For Different Team Members</span>
<span></span>
<span>| Role | What to Look For |</span>
<span>|------|------------------|</span>
<span>| **ML Engineer** | All training code - this is your main deliverable |</span>
<span>| **Backend Developer** | How to load the trained model |</span>
<span>| **Mobile Developer** | Nothing (you use exported ONNX model) |</span>
<span>| **QA/Testing** | Training validation metrics |</span>
<span>| **Project Manager** | Training timeline and requirements |</span>
<span></span>
<span>---</span>
<span></span>
<span>## Part 1: Training Pipeline Overview</span>
<span></span>
<span>### 1.1 The 5 Steps of Training</span>
<span></span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Step 1: Data Preparation Step 2: Feature Engineering Step 3: Train/Val/Test Split</span><br><span class="">───────────────────── ──────────────────────── ─────────────────────────</span><br><span class="">Raw CSV files → Feature vectors → 70% Training</span></p><ul style="margin: 16px 0px; padding-left: 18px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><li><p class="ds-markdown-paragraph" style="margin-top: 0px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px;"><span class="">crime_data.csv - crime_density 15% Validation</span></p></li><li style="margin-top: 6px;"><p class="ds-markdown-paragraph" style="margin-top: 0px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px;"><span class="">reports.csv - hour_sin 15% Test</span></p></li><li style="margin-top: 6px;"><p class="ds-markdown-paragraph" style="margin-top: 0px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px;"><span class="">env_data.csv - lighting_risk</span></p></li></ul><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Step 4: Model Training Step 5: Evaluation</span><br><span class="">───────────────────── ─────────────────</span><br><span class="">Training data → XGBoost learns → Evaluate on test set</span><br><span class="">Labels (risk scores) patterns Accuracy: 83%</span><br><span class="">F1 Score: 0.81</span></p><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">text</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span></span>
<span>### 1.2 Training Flow Diagram</span>
<span></span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">┌──────────────────┐</span><br><span class="">│ RAW DATA │</span><br><span class="">│ (CSV files) │</span><br><span class="">└────────┬─────────┘</span><br><span class="">│</span><br><span class="">▼</span><br><span class="">┌──────────────────┐</span><br><span class="">│ VALIDATION │ ← Check data quality</span><br><span class="">│ Check schemas │ (no nulls, correct types)</span><br><span class="">└────────┬─────────┘</span><br><span class="">│</span><br><span class="">▼</span><br><span class="">┌──────────────────┐</span><br><span class="">│ FEATURE ENGG │ ← Convert to numbers</span><br><span class="">│ Pipeline │ (13 features)</span><br><span class="">└────────┬─────────┘</span><br><span class="">│</span><br><span class="">▼</span><br><span class="">┌──────────────────┐</span><br><span class="">│ TRAIN/VAL/TEST │ ← Split data</span><br><span class="">│ Split (70/15/15)│ (stratified by risk)</span><br><span class="">└────────┬─────────┘</span><br><span class="">│</span><br><span class="">▼</span><br><span class="">┌──────────────────┐</span><br><span class="">│ HYPERPARAMETER │ ← Optuna finds best</span><br><span class="">│ TUNING │ parameters</span><br><span class="">└────────┬─────────┘</span><br><span class="">│</span><br><span class="">▼</span><br><span class="">┌──────────────────┐</span><br><span class="">│ MODEL TRAINING │ ← Train final model</span><br><span class="">│ XGBoost │ with best params</span><br><span class="">└────────┬─────────┘</span><br><span class="">│</span><br><span class="">▼</span><br><span class="">┌──────────────────┐</span><br><span class="">│ EVALUATION │ ← Test on unseen data</span><br><span class="">│ Metrics │ (F1, ROC-AUC, etc.)</span><br><span class="">└────────┬─────────┘</span><br><span class="">│</span><br><span class="">▼</span><br><span class="">┌──────────────────┐</span><br><span class="">│ MODEL EXPORT │ ← Save .pkl and .onnx</span><br><span class="">│ Save to disk │ for deployment</span><br><span class="">└──────────────────┘</span></p><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">text</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span></span>
<span>---</span>
<span></span>
<span>## Part 2: Data Preparation</span>
<span></span>
<span>### 2.1 Loading and Merging Data</span>
<span></span>
<span>```python</span>
<span>import pandas as pd</span>
<span>import numpy as np</span>
<span>from datetime import datetime</span>
<span></span>
<span>def load_and_merge_data(</span>
<span>    crime_path: str,</span>
<span>    reports_path: str,</span>
<span>    env_path: str</span>
<span>) -&gt; pd.DataFrame:</span>
<span>    """</span>
<span>    Load all data sources and merge into a single DataFrame.</span>
<span>    </span>
<span>    Args:</span>
<span>        crime_path: Path to crime data CSV</span>
<span>        reports_path: Path to community reports CSV</span>
<span>        env_path: Path to environmental data CSV</span>
<span>    </span>
<span>    Returns:</span>
<span>        Merged DataFrame with all features and labels</span>
<span>    """</span>
<span>    </span>
<span>    # Load data</span>
<span>    crime_df = pd.read_csv(crime_path)</span>
<span>    reports_df = pd.read_csv(reports_path)</span>
<span>    env_df = pd.read_csv(env_path)</span>
<span>    </span>
<span>    print(f"Loaded {len(crime_df)} crime records")</span>
<span>    print(f"Loaded {len(reports_df)} community reports")</span>
<span>    print(f"Loaded {len(env_df)} environmental records")</span>
<span>    </span>
<span>    # Convert timestamps</span>
<span>    crime_df['timestamp'] = pd.to_datetime(crime_df['timestamp'])</span>
<span>    reports_df['timestamp'] = pd.to_datetime(reports_df['timestamp'])</span>
<span>    env_df['timestamp'] = pd.to_datetime(env_df['timestamp'])</span>
<span>    </span>
<span>    # Merge on location and time (simplified - in production, use spatial joins)</span>
<span>    # For this example, we'll assume data is already aligned</span>
<span>    </span>
<span>    # Create target variable (risk score) from multiple sources</span>
<span>    # This is the "answer key" the model learns from</span>
<span>    </span>
<span>    # Option 1: Use reported risk level as target</span>
<span>    df = reports_df[['latitude', 'longitude', 'timestamp', 'risk_level']].copy()</span>
<span>    df.rename(columns={'risk_level': 'target_risk'}, inplace=True)</span>
<span>    </span>
<span>    # Add environmental features</span>
<span>    df = df.merge(</span>
<span>        env_df[['latitude', 'longitude', 'timestamp', </span>
<span>                'street_lighting_score', 'crowd_density', 'weather']],</span>
<span>        on=['latitude', 'longitude', 'timestamp'],</span>
<span>        how='left'</span>
<span>    )</span>
<span>    </span>
<span>    # Add crime density (calculated, not directly merged)</span>
<span>    # This will be done in feature engineering</span>
<span>    </span>
<span>    return df</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">2.2 Data Validation</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">python</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token keyword" style="color: rgb(166, 38, 164);">def</span> <span class="token function" style="color: rgb(64, 120, 242);">validate_training_data</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>df<span class="token punctuation" style="color: rgb(56, 58, 66);">:</span> pd<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>DataFrame<span class="token punctuation" style="color: rgb(56, 58, 66);">)</span> <span class="token operator" style="color: rgb(64, 120, 242);">-</span><span class="token operator" style="color: rgb(64, 120, 242);">&gt;</span> <span class="token builtin" style="color: rgb(80, 161, 79);">bool</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span></span>
<span>    <span class="token triple-quoted-string string" style="color: rgb(80, 161, 79);">"""</span></span>
<span>    Validate data quality before training.</span>
<span>    </span>
<span>    Returns:</span>
<span>        True if data passes all checks</span>
<span>    """</span>
<span>    </span>
<span>    checks_passed <span class="token operator" style="color: rgb(64, 120, 242);">=</span> <span class="token boolean" style="color: rgb(183, 107, 1);">True</span></span>
<span>    </span>
<span>    <span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Check 1: No missing values in critical columns</span></span>
<span>    critical_cols <span class="token operator" style="color: rgb(64, 120, 242);">=</span> <span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token string" style="color: rgb(80, 161, 79);">'latitude'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> <span class="token string" style="color: rgb(80, 161, 79);">'longitude'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> <span class="token string" style="color: rgb(80, 161, 79);">'target_risk'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span></span>
<span>    <span class="token keyword" style="color: rgb(166, 38, 164);">for</span> col <span class="token keyword" style="color: rgb(166, 38, 164);">in</span> critical_cols<span class="token punctuation" style="color: rgb(56, 58, 66);">:</span></span>
<span>        missing <span class="token operator" style="color: rgb(64, 120, 242);">=</span> df<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span>col<span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>isnull<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span><span class="token builtin" style="color: rgb(80, 161, 79);">sum</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>        <span class="token keyword" style="color: rgb(166, 38, 164);">if</span> missing <span class="token operator" style="color: rgb(64, 120, 242);">&gt;</span> <span class="token number" style="color: rgb(183, 107, 1);">0</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span></span>
<span>            <span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string-interpolation"><span class="token string" style="color: rgb(80, 161, 79);">f"❌ </span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span>col<span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);">: </span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span>missing<span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);"> missing values"</span></span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>            checks_passed <span class="token operator" style="color: rgb(64, 120, 242);">=</span> <span class="token boolean" style="color: rgb(183, 107, 1);">False</span></span>
<span>    </span>
<span>    <span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Check 2: Target variable has all 5 classes</span></span>
<span>    unique_risks <span class="token operator" style="color: rgb(64, 120, 242);">=</span> df<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token string" style="color: rgb(80, 161, 79);">'target_risk'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>unique<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>    expected_risks <span class="token operator" style="color: rgb(64, 120, 242);">=</span> <span class="token punctuation" style="color: rgb(56, 58, 66);">{</span><span class="token number" style="color: rgb(183, 107, 1);">0</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> <span class="token number" style="color: rgb(183, 107, 1);">1</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> <span class="token number" style="color: rgb(183, 107, 1);">2</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> <span class="token number" style="color: rgb(183, 107, 1);">3</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> <span class="token number" style="color: rgb(183, 107, 1);">4</span><span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span>
<span>    <span class="token keyword" style="color: rgb(166, 38, 164);">if</span> <span class="token keyword" style="color: rgb(166, 38, 164);">not</span> expected_risks<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>issubset<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>unique_risks<span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span></span>
<span>        missing_classes <span class="token operator" style="color: rgb(64, 120, 242);">=</span> expected_risks <span class="token operator" style="color: rgb(64, 120, 242);">-</span> <span class="token builtin" style="color: rgb(80, 161, 79);">set</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>unique_risks<span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>        <span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string-interpolation"><span class="token string" style="color: rgb(80, 161, 79);">f"❌ Missing risk classes: </span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span>missing_classes<span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);">"</span></span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>        checks_passed <span class="token operator" style="color: rgb(64, 120, 242);">=</span> <span class="token boolean" style="color: rgb(183, 107, 1);">False</span></span>
<span>    </span>
<span>    <span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Check 3: No extreme outliers in coordinates</span></span>
<span>    valid_lat <span class="token operator" style="color: rgb(64, 120, 242);">=</span> <span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>df<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token string" style="color: rgb(80, 161, 79);">'latitude'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span> <span class="token operator" style="color: rgb(64, 120, 242);">&gt;=</span> <span class="token operator" style="color: rgb(64, 120, 242);">-</span><span class="token number" style="color: rgb(183, 107, 1);">90</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span> <span class="token operator" style="color: rgb(64, 120, 242);">&amp;</span> <span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>df<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token string" style="color: rgb(80, 161, 79);">'latitude'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span> <span class="token operator" style="color: rgb(64, 120, 242);">&lt;=</span> <span class="token number" style="color: rgb(183, 107, 1);">90</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>    valid_lon <span class="token operator" style="color: rgb(64, 120, 242);">=</span> <span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>df<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token string" style="color: rgb(80, 161, 79);">'longitude'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span> <span class="token operator" style="color: rgb(64, 120, 242);">&gt;=</span> <span class="token operator" style="color: rgb(64, 120, 242);">-</span><span class="token number" style="color: rgb(183, 107, 1);">180</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span> <span class="token operator" style="color: rgb(64, 120, 242);">&amp;</span> <span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>df<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token string" style="color: rgb(80, 161, 79);">'longitude'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span> <span class="token operator" style="color: rgb(64, 120, 242);">&lt;=</span> <span class="token number" style="color: rgb(183, 107, 1);">180</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>    </span>
<span>    <span class="token keyword" style="color: rgb(166, 38, 164);">if</span> <span class="token keyword" style="color: rgb(166, 38, 164);">not</span> valid_lat<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span><span class="token builtin" style="color: rgb(80, 161, 79);">all</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span></span>
<span>        <span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string-interpolation"><span class="token string" style="color: rgb(80, 161, 79);">f"❌ Invalid latitudes: </span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span>df<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token operator" style="color: rgb(64, 120, 242);">~</span>valid_lat<span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token string" style="color: rgb(80, 161, 79);">'latitude'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>tolist<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);">"</span></span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>        checks_passed <span class="token operator" style="color: rgb(64, 120, 242);">=</span> <span class="token boolean" style="color: rgb(183, 107, 1);">False</span></span>
<span>    </span>
<span>    <span class="token keyword" style="color: rgb(166, 38, 164);">if</span> <span class="token keyword" style="color: rgb(166, 38, 164);">not</span> valid_lon<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span><span class="token builtin" style="color: rgb(80, 161, 79);">all</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span></span>
<span>        <span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string-interpolation"><span class="token string" style="color: rgb(80, 161, 79);">f"❌ Invalid longitudes: </span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span>df<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token operator" style="color: rgb(64, 120, 242);">~</span>valid_lon<span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token string" style="color: rgb(80, 161, 79);">'longitude'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>tolist<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);">"</span></span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>        checks_passed <span class="token operator" style="color: rgb(64, 120, 242);">=</span> <span class="token boolean" style="color: rgb(183, 107, 1);">False</span></span>
<span>    </span>
<span>    <span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Check 4: Target variable distribution</span></span>
<span>    risk_distribution <span class="token operator" style="color: rgb(64, 120, 242);">=</span> df<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token string" style="color: rgb(80, 161, 79);">'target_risk'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>value_counts<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>normalize<span class="token operator" style="color: rgb(64, 120, 242);">=</span><span class="token boolean" style="color: rgb(183, 107, 1);">True</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>    <span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">"\nTarget distribution:"</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>    <span class="token keyword" style="color: rgb(166, 38, 164);">for</span> risk <span class="token keyword" style="color: rgb(166, 38, 164);">in</span> <span class="token builtin" style="color: rgb(80, 161, 79);">sorted</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>risk_distribution<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>index<span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span></span>
<span>        <span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string-interpolation"><span class="token string" style="color: rgb(80, 161, 79);">f"  Risk </span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span>risk<span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);">: </span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span>risk_distribution<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span>risk<span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span><span class="token format-spec">.1%</span><span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);">"</span></span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>    </span>
<span>    <span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Check for class imbalance (warn, but don't fail)</span></span>
<span>    min_class <span class="token operator" style="color: rgb(64, 120, 242);">=</span> risk_distribution<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span><span class="token builtin" style="color: rgb(80, 161, 79);">min</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>    <span class="token keyword" style="color: rgb(166, 38, 164);">if</span> min_class <span class="token operator" style="color: rgb(64, 120, 242);">&lt;</span> <span class="token number" style="color: rgb(183, 107, 1);">0.05</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span></span>
<span>        <span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string-interpolation"><span class="token string" style="color: rgb(80, 161, 79);">f"⚠️ Warning: Class imbalance detected (smallest class: </span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span>min_class<span class="token punctuation" style="color: rgb(56, 58, 66);">:</span><span class="token format-spec">.1%</span><span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);">)"</span></span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>    </span>
<span>    <span class="token keyword" style="color: rgb(166, 38, 164);">if</span> checks_passed<span class="token punctuation" style="color: rgb(56, 58, 66);">:</span></span>
<span>        <span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">"\n✅ All validation checks passed!"</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>    </span>
<span>    <span class="token keyword" style="color: rgb(166, 38, 164);">return</span> checks_passed</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><hr style="background: none 0% 0% / auto repeat scroll padding-box border-box rgba(0, 0, 0, 0.1); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; height: 1px; margin: 32px 0px; display: block; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><h2 style="font: 700 22px / 32px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Part 3: Train/Validation/Test Split</span></h2><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">3.1 Why Split Data?</span></h3><div class="ds-scroll-area ds-scroll-area--show-on-focus-within ds-scroll-area--enabled _1210dd7 c03cafe9" style="--dsl-scroll-area-gutters-disappear-delay: 1s; z-index: 0; position: relative; overflow: auto; scrollbar-width: none; --padding-left: calc(( 1280px - (840px - 2 * 44px) ) / 2 + (840px - 2 * 44px - 100%)); --padding-right: 54px; width: calc(100% + 210px); padding-left: calc(-100% + 1016px); padding-right: 54px; margin-left: calc(100% - 1016px); color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="ds-scroll-area__gutters" style="--dsl-scroll-area-scrollbar-bg: #e5e5e5; --dsl-scroll-area-scrollbar-hover: #d4d4d4; --dsl-scroll-area-horizontal-gutter-padding: 2px 0; --dsl-scroll-area-vertical-gutter-padding: 0 2px; pointer-events: none; z-index: 1000; transition: opacity 0.1s ease-out 1s; opacity: 1 !important; display: block; --container-height: 184px; position: sticky; top: 0px; left: 0px; right: 0px; width: 962px; height: 0px;"><div class="ds-scroll-area__horizontal-gutter" style="position: absolute; padding: 2px 0px; left: 0px; right: 0px; display: block; top: 170px; height: 10px;"></div><div class="ds-scroll-area__vertical-gutter" style="position: absolute; padding: 0px 2px; right: 0px; top: 8px; bottom: -176px; width: 10px;"></div></div>
Split | Purpose | Size | Used For
-- | -- | -- | --
Training | Model learns patterns | 70% | Updating model weights
Validation | Tune hyperparameters | 15% | Selecting best model
Test | Final evaluation | 15% | Measuring real performance

</div><hr style="background: none 0% 0% / auto repeat scroll padding-box border-box rgba(0, 0, 0, 0.1); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; height: 1px; margin: 32px 0px; display: block; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><em><span class="">Last updated: June 2026</span></em></p><!--EndFragment-->
</body>
</html>markdown
# Model Training Guide

## What Is Model Training?

**Model training** is the process of teaching the XGBoost algorithm to predict risk scores from feature vectors.

Think of it like teaching a student:
- **Features** = The textbook (information)
- **Labels** = The answer key (correct risk scores)
- **Model** = The student who learns the patterns
┌─────────────────────────────────────────────────────────────────┐
│ TRAINING PROCESS │
├─────────────────────────────────────────────────────────────────┤
│ │
│ Features + Labels → XGBoost → Trained Model │
│ (What we know) (Learns) (Predicts risk) │
│ │
│ "2.3 risk score" │
│ "3.1 risk score" ┌─────┐ ┌─────────────────┐ │
│ "0.5 risk score" ───→│XGBoost│────→│ risk_model.pkl │ │
│ "4.0 risk score" └─────┘ └─────────────────┘ │
│ │
└─────────────────────────────────────────────────────────────────┘

text

> **Why this matters:** A well-trained model accurately predicts risk, keeping users safe.

---

## For Different Team Members

| Role | What to Look For |
|------|------------------|
| **ML Engineer** | All training code - this is your main deliverable |
| **Backend Developer** | How to load the trained model |
| **Mobile Developer** | Nothing (you use exported ONNX model) |
| **QA/Testing** | Training validation metrics |
| **Project Manager** | Training timeline and requirements |

---

## Part 1: Training Pipeline Overview

### 1.1 The 5 Steps of Training
Step 1: Data Preparation Step 2: Feature Engineering Step 3: Train/Val/Test Split
───────────────────── ──────────────────────── ─────────────────────────
Raw CSV files → Feature vectors → 70% Training

crime_data.csv - crime_density 15% Validation

reports.csv - hour_sin 15% Test

env_data.csv - lighting_risk

Step 4: Model Training Step 5: Evaluation
───────────────────── ─────────────────
Training data → XGBoost learns → Evaluate on test set
Labels (risk scores) patterns Accuracy: 83%
F1 Score: 0.81

text

### 1.2 Training Flow Diagram
┌──────────────────┐
│ RAW DATA │
│ (CSV files) │
└────────┬─────────┘
│
▼
┌──────────────────┐
│ VALIDATION │ ← Check data quality
│ Check schemas │ (no nulls, correct types)
└────────┬─────────┘
│
▼
┌──────────────────┐
│ FEATURE ENGG │ ← Convert to numbers
│ Pipeline │ (13 features)
└────────┬─────────┘
│
▼
┌──────────────────┐
│ TRAIN/VAL/TEST │ ← Split data
│ Split (70/15/15)│ (stratified by risk)
└────────┬─────────┘
│
▼
┌──────────────────┐
│ HYPERPARAMETER │ ← Optuna finds best
│ TUNING │ parameters
└────────┬─────────┘
│
▼
┌──────────────────┐
│ MODEL TRAINING │ ← Train final model
│ XGBoost │ with best params
└────────┬─────────┘
│
▼
┌──────────────────┐
│ EVALUATION │ ← Test on unseen data
│ Metrics │ (F1, ROC-AUC, etc.)
└────────┬─────────┘
│
▼
┌──────────────────┐
│ MODEL EXPORT │ ← Save .pkl and .onnx
│ Save to disk │ for deployment
└──────────────────┘

text

---

## Part 2: Data Preparation

### 2.1 Loading and Merging Data

```python
import pandas as pd
import numpy as np
from datetime import datetime

def load_and_merge_data(
    crime_path: str,
    reports_path: str,
    env_path: str
) -> pd.DataFrame:
    """
    Load all data sources and merge into a single DataFrame.
    
    Args:
        crime_path: Path to crime data CSV
        reports_path: Path to community reports CSV
        env_path: Path to environmental data CSV
    
    Returns:
        Merged DataFrame with all features and labels
    """
    
    # Load data
    crime_df = pd.read_csv(crime_path)
    reports_df = pd.read_csv(reports_path)
    env_df = pd.read_csv(env_path)
    
    print(f"Loaded {len(crime_df)} crime records")
    print(f"Loaded {len(reports_df)} community reports")
    print(f"Loaded {len(env_df)} environmental records")
    
    # Convert timestamps
    crime_df['timestamp'] = pd.to_datetime(crime_df['timestamp'])
    reports_df['timestamp'] = pd.to_datetime(reports_df['timestamp'])
    env_df['timestamp'] = pd.to_datetime(env_df['timestamp'])
    
    # Merge on location and time (simplified - in production, use spatial joins)
    # For this example, we'll assume data is already aligned
    
    # Create target variable (risk score) from multiple sources
    # This is the "answer key" the model learns from
    
    # Option 1: Use reported risk level as target
    df = reports_df[['latitude', 'longitude', 'timestamp', 'risk_level']].copy()
    df.rename(columns={'risk_level': 'target_risk'}, inplace=True)
    
    # Add environmental features
    df = df.merge(
        env_df[['latitude', 'longitude', 'timestamp', 
                'street_lighting_score', 'crowd_density', 'weather']],
        on=['latitude', 'longitude', 'timestamp'],
        how='left'
    )
    
    # Add crime density (calculated, not directly merged)
    # This will be done in feature engineering
    
    return df
2.2 Data Validation
python
def validate_training_data(df: pd.DataFrame) -> bool:
    """
    Validate data quality before training.
    
    Returns:
        True if data passes all checks
    """
    
    checks_passed = True
    
    # Check 1: No missing values in critical columns
    critical_cols = ['latitude', 'longitude', 'target_risk']
    for col in critical_cols:
        missing = df[col].isnull().sum()
        if missing > 0:
            print(f"❌ {col}: {missing} missing values")
            checks_passed = False
    
    # Check 2: Target variable has all 5 classes
    unique_risks = df['target_risk'].unique()
    expected_risks = {0, 1, 2, 3, 4}
    if not expected_risks.issubset(unique_risks):
        missing_classes = expected_risks - set(unique_risks)
        print(f"❌ Missing risk classes: {missing_classes}")
        checks_passed = False
    
    # Check 3: No extreme outliers in coordinates
    valid_lat = (df['latitude'] >= -90) & (df['latitude'] <= 90)
    valid_lon = (df['longitude'] >= -180) & (df['longitude'] <= 180)
    
    if not valid_lat.all():
        print(f"❌ Invalid latitudes: {df[~valid_lat]['latitude'].tolist()}")
        checks_passed = False
    
    if not valid_lon.all():
        print(f"❌ Invalid longitudes: {df[~valid_lon]['longitude'].tolist()}")
        checks_passed = False
    
    # Check 4: Target variable distribution
    risk_distribution = df['target_risk'].value_counts(normalize=True)
    print("\nTarget distribution:")
    for risk in sorted(risk_distribution.index):
        print(f"  Risk {risk}: {risk_distribution[risk]:.1%}")
    
    # Check for class imbalance (warn, but don't fail)
    min_class = risk_distribution.min()
    if min_class < 0.05:
        print(f"⚠️ Warning: Class imbalance detected (smallest class: {min_class:.1%})")
    
    if checks_passed:
        print("\n✅ All validation checks passed!")
    
    return checks_passed
Part 3: Train/Validation/Test Split
3.1 Why Split Data?
Split	Purpose	Size	Used For
Training	Model learns patterns	70%	Updating model weights
Validation	Tune hyperparameters	15%	Selecting best model
Test	Final evaluation	15%	Measuring real performance
3.2 Stratified Split
Important: Use stratified splitting to maintain risk class distribution in all sets.

python
from sklearn.model_selection import train_test_split

def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    random_state: int = 42
) -> tuple:
    """
    Split data into train/validation/test sets.
    
    Args:
        X: Feature DataFrame
        y: Target Series (risk scores 0-4)
        random_state: For reproducibility
    
    Returns:
        X_train, X_val, X_test, y_train, y_val, y_test
    """
    
    # First split: 70% train, 30% temp (val + test)
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y,
        test_size=0.30,
        random_state=random_state,
        stratify=y  # Maintains risk class distribution
    )
    
    # Second split: 50% of temp = val, 50% = test (so 15% each of total)
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp,
        test_size=0.50,
        random_state=random_state,
        stratify=y_temp
    )
    
    print(f"Training set: {len(X_train)} samples ({len(X_train)/len(X)*100:.0f}%)")
    print(f"Validation set: {len(X_val)} samples ({len(X_val)/len(X)*100:.0f}%)")
    print(f"Test set: {len(X_test)} samples ({len(X_test)/len(X)*100:.0f}%)")
    
    # Show distribution
    print("\nRisk distribution in each set:")
    for name, y_set in [("Train", y_train), ("Val", y_val), ("Test", y_test)]:
        dist = y_set.value_counts(normalize=True).sort_index()
        print(f"{name}: {dict(round(dist, 2))}")
    
    return X_train, X_val, X_test, y_train, y_val, y_test
3.3 Example Output
text
Training set: 7000 samples (70%)
Validation set: 1500 samples (15%)
Test set: 1500 samples (15%)

Risk distribution in each set:
Train: {0: 0.30, 1: 0.25, 2: 0.20, 3: 0.15, 4: 0.10}
Val:   {0: 0.30, 1: 0.25, 2: 0.20, 3: 0.15, 4: 0.10}
Test:  {0: 0.30, 1: 0.25, 2: 0.20, 3: 0.15, 4: 0.10}
Part 4: Hyperparameter Tuning with Optuna
4.1 What Are Hyperparameters?
Hyperparameters are settings we choose BEFORE training:

Hyperparameter	What It Does	Typical Range
max_depth	How complex the model can be	3-10
learning_rate	How fast the model learns	0.01-0.3
n_estimators	Number of trees	50-300
subsample	% of data used per tree	0.6-1.0
4.2 Optuna Tuning Code
python
import optuna
import xgboost as xgb
from sklearn.model_selection import cross_val_score

def objective(trial, X_train, y_train):
    """
    Objective function for Optuna to optimize.
    
    Args:
        trial: Optuna trial object
        X_train: Training features
        y_train: Training labels
    
    Returns:
        Cross-validation F1 score (to maximize)
    """
    
    # Suggest hyperparameters to try
    params = {
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'n_estimators': trial.suggest_int('n_estimators', 50, 300),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 1.0),
        'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),
        'gamma': trial.suggest_float('gamma', 0, 0.5),
        'reg_alpha': trial.suggest_float('reg_alpha', 0, 1),
        'reg_lambda': trial.suggest_float('reg_lambda', 0, 1),
        
        # Fixed parameters
        'objective': 'multi:softprob',
        'num_class': 5,
        'eval_metric': 'mlogloss',
        'random_state': 42,
        'n_jobs': -1
    }
    
    # Cross-validation (5-fold)
    model = xgb.XGBClassifier(**params)
    
    scores = cross_val_score(
        model, X_train, y_train,
        cv=5,
        scoring='f1_macro',
        n_jobs=-1
    )
    
    return scores.mean()

def run_hyperparameter_tuning(X_train, y_train, n_trials=50):
    """
    Run Optuna hyperparameter optimization.
    
    Args:
        X_train: Training features
        y_train: Training labels
        n_trials: Number of parameter combinations to try
    
    Returns:
        Best parameters found
    """
    
    print(f"Starting hyperparameter tuning with {n_trials} trials...")
    
    # Create study (maximize F1 score)
    study = optuna.create_study(
        direction='maximize',
        study_name='saferoute_optimization',
        storage='sqlite:///optuna_study.db',
        load_if_exists=True
    )
    
    # Run optimization
    study.optimize(
        lambda trial: objective(trial, X_train, y_train),
        n_trials=n_trials,
        show_progress_bar=True
    )
    
    # Print results
    print("\n✅ Optimization complete!")
    print(f"Best F1 score: {study.best_value:.4f}")
    print("\nBest parameters:")
    for param, value in study.best_params.items():
        print(f"  {param}: {value}")
    
    # Plot optimization history
    from optuna.visualization import plot_optimization_history
    fig = plot_optimization_history(study)
    fig.write_image("reports/optuna_history.png")
    
    return study.best_params
4.3 Tuning Progress Example
text
Starting hyperparameter tuning with 50 trials...

Trial 1: F1=0.7234 | max_depth=5, lr=0.12, n_est=120
Trial 2: F1=0.7456 | max_depth=7, lr=0.08, n_est=180
Trial 3: F1=0.7123 | max_depth=3, lr=0.15, n_est=90
...
Trial 25: F1=0.8123 | max_depth=6, lr=0.09, n_est=220
...
Trial 50: F1=0.8145 | max_depth=6, lr=0.09, n_est=210

✅ Optimization complete!
Best F1 score: 0.8145

Best parameters:
  max_depth: 6
  learning_rate: 0.094
  n_estimators: 215
  subsample: 0.85
  colsample_bytree: 0.82
  min_child_weight: 3
  gamma: 0.12
  reg_alpha: 0.05
  reg_lambda: 0.08
Part 5: Training the Final Model
5.1 RiskModel Class
python
import joblib
import xgboost as xgb
from sklearn.metrics import classification_report, f1_score

class RiskModel:
    """XGBoost risk prediction model."""
    
    def __init__(self, params: dict = None):
        """
        Initialize risk model.
        
        Args:
            params: XGBoost parameters (uses defaults if None)
        """
        
        self.params = params or {
            'objective': 'multi:softprob',
            'num_class': 5,
            'max_depth': 6,
            'learning_rate': 0.1,
            'n_estimators': 100,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'min_child_weight': 3,
            'gamma': 0.1,
            'reg_alpha': 0.1,
            'reg_lambda': 0.1,
            'random_state': 42,
            'n_jobs': -1
        }
        
        self.model = None
        self.feature_names = None
        self.training_history = []
    
    def train(self, X_train, y_train, X_val=None, y_val=None):
        """
        Train the XGBoost model.
        
        Args:
            X_train: Training features
            y_train: Training labels
            X_val: Validation features (optional)
            y_val: Validation labels (optional)
        
        Returns:
            Training metrics
        """
        
        # Store feature names
        self.feature_names = X_train.columns.tolist()
        
        print(f"Training XGBoost model...")
        print(f"  Training samples: {len(X_train)}")
        print(f"  Features: {len(self.feature_names)}")
        
        # Create model
        self.model = xgb.XGBClassifier(**self.params)
        
        # Evaluation set for early stopping
        eval_set = []
        if X_val is not None and y_val is not None:
            eval_set = [(X_train, y_train), (X_val, y_val)]
        
        # Train with early stopping
        self.model.fit(
            X_train, y_train,
            eval_set=eval_set,
            eval_metric='mlogloss',
            early_stopping_rounds=20,
            verbose=True
        )
        
        # Calculate training metrics
        train_pred = self.model.predict(X_train)
        train_f1 = f1_score(y_train, train_pred, average='macro')
        
        print(f"\n✅ Training complete!")
        print(f"  Training F1: {train_f1:.4f}")
        
        if X_val is not None:
            val_pred = self.model.predict(X_val)
            val_f1 = f1_score(y_val, val_pred, average='macro')
            print(f"  Validation F1: {val_f1:.4f}")
        
        return {
            'train_f1': train_f1,
            'val_f1': val_f1 if X_val else None,
            'best_iteration': self.model.best_iteration
        }
    
    def predict(self, X):
        """Predict risk scores for new data."""
        if self.model is None:
            raise ValueError("Model not trained yet!")
        
        return self.model.predict(X)
    
    def predict_proba(self, X):
        """Predict risk probabilities for each class."""
        if self.model is None:
            raise ValueError("Model not trained yet!")
        
        return self.model.predict_proba(X)
    
    def save(self, path: str):
        """Save model to disk."""
        joblib.dump({
            'model': self.model,
            'feature_names': self.feature_names,
            'params': self.params
        }, path)
        print(f"✅ Model saved to {path}")
    
    def load(self, path: str):
        """Load model from disk."""
        data = joblib.load(path)
        self.model = data['model']
        self.feature_names = data['feature_names']
        self.params = data['params']
        print(f"✅ Model loaded from {path}")
5.2 Complete Training Script
python
def run_training_pipeline(
    crime_path: str,
    reports_path: str,
    env_path: str,
    output_model_path: str
):
    """
    Run complete training pipeline.
    
    Args:
        crime_path: Path to crime data
        reports_path: Path to reports data
        env_path: Path to environmental data
        output_model_path: Where to save the trained model
    """
    
    print("=" * 60)
    print("SAFEROUTE AI - MODEL TRAINING PIPELINE")
    print("=" * 60)
    
    # Step 1: Load data
    print("\n[1/7] Loading data...")
    df = load_and_merge_data(crime_path, reports_path, env_path)
    
    # Step 2: Validate data
    print("\n[2/7] Validating data...")
    validate_training_data(df)
    
    # Step 3: Feature engineering
    print("\n[3/7] Engineering features...")
    from src.features.pipeline import FeaturePipeline
    
    feature_pipeline = FeaturePipeline(crime_df=pd.read_csv(crime_path))
    X = feature_pipeline.transform(df)
    y = df['target_risk']
    
    print(f"  Created {X.shape[1]} features from {X.shape[0]} samples")
    
    # Step 4: Split data
    print("\n[4/7] Splitting data...")
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)
    
    # Step 5: Hyperparameter tuning
    print("\n[5/7] Tuning hyperparameters...")
    best_params = run_hyperparameter_tuning(X_train, y_train, n_trials=30)
    
    # Step 6: Train final model
    print("\n[6/7] Training final model...")
    model = RiskModel(params=best_params)
    metrics = model.train(X_train, y_train, X_val, y_val)
    
    # Step 7: Evaluate on test set
    print("\n[7/7] Evaluating on test set...")
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)
    
    from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, 
                                 target_names=['Safe', 'Low', 'Medium', 'High', 'Extreme']))
    
    # ROC-AUC (One-vs-Rest)
    auc = roc_auc_score(y_test, y_proba, multi_class='ovr', average='macro')
    print(f"\nROC-AUC (macro): {auc:.4f}")
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("\nConfusion Matrix:")
    print(cm)
    
    # Step 8: Save model
    print("\n[8/7] Saving model...")
    model.save(output_model_path)
    
    # Save feature pipeline for later use
    import joblib
    joblib.dump(feature_pipeline, 'models/production/feature_pipeline.pkl')
    
    print("\n" + "=" * 60)
    print("✅ TRAINING PIPELINE COMPLETE!")
    print("=" * 60)
    
    return model, metrics
Part 6: Training from Command Line
6.1 Training Script
Create scripts/run_training.py:

python
#!/usr/bin/env python
"""Command-line script for training the risk model."""

import argparse
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_training import run_training_pipeline

def main():
    parser = argparse.ArgumentParser(description='Train SafeRoute AI risk model')
    parser.add_argument('--crime-data', type=str, 
                        default='data/raw/crime_data.csv',
                        help='Path to crime data CSV')
    parser.add_argument('--reports-data', type=str,
                        default='data/raw/community_reports.csv',
                        help='Path to community reports CSV')
    parser.add_argument('--env-data', type=str,
                        default='data/raw/environmental_data.csv',
                        help='Path to environmental data CSV')
    parser.add_argument('--output', type=str,
                        default='models/production/risk_model.pkl',
                        help='Path to save trained model')
    parser.add_argument('--quick', action='store_true',
                        help='Skip hyperparameter tuning (use defaults)')
    
    args = parser.parse_args()
    
    print("SafeRoute AI Model Training")
    print(f"Crime data: {args.crime_data}")
    print(f"Reports data: {args.reports_data}")
    print(f"Environmental data: {args.env_data}")
    print(f"Output: {args.output}")
    
    if args.quick:
        print("\n⚠️  Running in QUICK mode (no hyperparameter tuning)")
    
    run_training_pipeline(
        crime_path=args.crime_data,
        reports_path=args.reports_data,
        env_path=args.env_data,
        output_model_path=args.output
    )

if __name__ == "__main__":
    main()
6.2 Running the Training
bash
# Full training (with hyperparameter tuning)
python scripts/run_training.py

# Quick training (no tuning, uses defaults)
python scripts/run_training.py --quick

# Custom data paths
python scripts/run_training.py \
    --crime-data data/raw/my_crime_data.csv \
    --output models/staging/experiment_model.pkl
Part 7: Training Output Examples
7.1 Console Output
text
============================================================
SAFEROUTE AI - MODEL TRAINING PIPELINE
============================================================

[1/7] Loading data...
Loaded 5000 crime records
Loaded 2000 community reports
Loaded 10000 environmental records

[2/7] Validating data...

Target distribution:
  Risk 0: 30.5%
  Risk 1: 25.2%
  Risk 2: 20.1%
  Risk 3: 14.8%
  Risk 4: 9.4%

✅ All validation checks passed!

[3/7] Engineering features...
  Created 13 features from 2000 samples

[4/7] Splitting data...
Training set: 1400 samples (70%)
Validation set: 300 samples (15%)
Test set: 300 samples (15%)

Risk distribution in each set:
Train: {0: 0.30, 1: 0.25, 2: 0.20, 3: 0.15, 4: 0.10}
Val:   {0: 0.30, 1: 0.25, 2: 0.20, 3: 0.15, 4: 0.10}
Test:  {0: 0.30, 1: 0.25, 2: 0.20, 3: 0.15, 4: 0.10}

[5/7] Tuning hyperparameters...
Starting hyperparameter tuning with 30 trials...

Trial 1: F1=0.7234 | max_depth=5, lr=0.12, n_est=120
Trial 2: F1=0.7456 | max_depth=7, lr=0.08, n_est=180
...
Trial 30: F1=0.8145 | max_depth=6, lr=0.09, n_est=215

✅ Optimization complete!
Best F1 score: 0.8145

[6/7] Training final model...
Training XGBoost model...
  Training samples: 1400
  Features: 13
[0] train-mlogloss:1.60432
[10] train-mlogloss:1.20345 val-mlogloss:1.28432
[20] train-mlogloss:0.92345 val-mlogloss:1.01234
...
[210] train-mlogloss:0.42345 val-mlogloss:0.83456

✅ Training complete!
  Training F1: 0.8923
  Validation F1: 0.8145

[7/7] Evaluating on test set...

Classification Report:
              precision    recall  f1-score   support
        Safe       0.88      0.85      0.86        90
     Low Risk       0.84      0.82      0.83        75
   Medium Risk       0.81      0.79      0.80        60
    High Risk       0.79      0.76      0.77        45
     Extreme       0.82      0.79      0.80        30

    accuracy                           0.83       300
   macro avg       0.83      0.80      0.81       300
weighted avg       0.83      0.83      0.83       300

ROC-AUC (macro): 0.9189

Confusion Matrix:
[[77 10  3  0  0]
 [ 8 62  4  1  0]
 [ 2  6 47  4  1]
 [ 0  2  5 34  4]
 [ 0  0  3  3 24]]

[8/7] Saving model...
✅ Model saved to models/production/risk_model.pkl

============================================================
✅ TRAINING PIPELINE COMPLETE!
============================================================
7.2 MLflow UI Output
After training, start MLflow to see experiment tracking:

bash
mlflow ui --backend-store-uri ./mlruns
Open http://localhost:5000/ to see:

Experiment	Date	Parameters	Metrics
saferoute_ml	2026-06-06	max_depth=6, lr=0.09	F1=0.8145, AUC=0.9189
saferoute_ml	2026-06-05	max_depth=5, lr=0.12	F1=0.8023, AUC=0.9102
saferoute_ml	2026-06-04	max_depth=7, lr=0.08	F1=0.7956, AUC=0.9056
Part 8: Handling Class Imbalance
8.1 The Problem
If Extreme Risk (4) is only 9% of data, the model might learn to always predict Safe (0).

8.2 Solutions
Solution 1: Class Weights

python
# Calculate class weights (inverse of frequency)
from sklearn.utils.class_weight import compute_class_weight

classes = np.unique(y_train)
weights = compute_class_weight('balanced', classes=classes, y=y_train)
class_weight_dict = dict(zip(classes, weights))

model = xgb.XGBClassifier(
    **params,
    scale_pos_weight=class_weight_dict  # For binary
)

# For multi-class, use sample weights
sample_weights = np.array([class_weight_dict[y] for y in y_train])
model.fit(X_train, y_train, sample_weight=sample_weights)
Solution 2: SMOTE (Synthetic Data)

python
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

print(f"Original: {len(X_train)} samples")
print(f"Balanced: {len(X_train_balanced)} samples")
Part 9: Reproducibility
9.1 Set Random Seeds
python
def set_seeds(seed=42):
    """Set all random seeds for reproducibility."""
    import random
    import numpy as np
    
    random.seed(seed)
    np.random.seed(seed)
    
    # For PyTorch/TensorFlow if used
    # torch.manual_seed(seed)
    
    print(f"✅ Random seeds set to {seed}")

set_seeds(42)
9.2 Save Training Configuration
python
import json
from datetime import datetime

def save_training_config(config: dict, path: str):
    """Save training configuration for reproducibility."""
    
    config['timestamp'] = datetime.now().isoformat()
    config['python_version'] = sys.version
    
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Config saved to {path}")

# Example
config = {
    'data_sources': ['crime_data.csv', 'reports.csv', 'env.csv'],
    'feature_count': 13,
    'train_size': 1400,
    'val_size': 300,
    'test_size': 300,
    'best_params': best_params,
    'final_f1': 0.8145
}
save_training_config(config, 'reports/training_config.json')
Part 10: Troubleshooting
Problem	Likely Cause	Solution
Out of memory	Too much data	Use chunking or reduce features
Poor validation F1	Overfitting	Reduce max_depth, increase reg_alpha
Class not present	Missing data	Check data source, collect more
Training too slow	Too many estimators	Reduce n_estimators or use early stopping
NaN loss values	Missing values in features	Impute or remove NaN rows
CUDA out of memory	GPU memory	Use CPU: n_jobs=-1, tree_method='hist'
Quick Reference Card
Step	Command	Output
Train model	python scripts/run_training.py	risk_model.pkl
Quick train	python scripts/run_training.py --quick	Faster training
View experiments	mlflow ui	http://localhost:5000
Test model	pytest tests/models/	Test results
Last updated: June 2026