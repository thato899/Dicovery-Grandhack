<html>
<body>
<!--StartFragment--><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><br class="Apple-interchange-newline">---</span>
<span></span>
<span>## Page 2: Model-Evaluation</span>
<span></span>
<span>```markdown</span>
<span># Model Evaluation Guide</span>
<span></span>
<span>## What is Model Evaluation?</span>
<span></span>
<span>**Model evaluation** measures how well our risk prediction model performs on unseen data.</span>
<span></span>
<span>Think of it like a final exam for the model:</span>
<span>- **Training** = Studying (learning from known data)</span>
<span>- **Validation** = Practice tests (tuning parameters)</span>
<span>- **Test** = Final exam (unseen data only)</span>
<span></span>
<span>&gt; **Why this matters:** A model that performs well on training data but poorly on test data is USELESS in production.</span>
<span></span>
<span>---</span>
<span></span>
<span>## For Different Team Members</span>
<span></span>
<span>| Role | What to Look For |</span>
<span>|------|------------------|</span>
<span>| **ML Engineer** | All metrics - validates your work |</span>
<span>| **Project Manager** | Overall accuracy and readiness |</span>
<span>| **QA/Testing** | Thresholds for passing |</span>
<span>| **Backend/Mobile** | Model quality before integration |</span>
<span></span>
<span>---</span>
<span></span>
<span>## Part 1: Evaluation Metrics</span>
<span></span>
<span>### 1.1 What Each Metric Means</span>
<span></span>
<span>| Metric | What It Measures | Formula | Target |</span>
<span>|--------|------------------|---------|--------|</span>
<span>| **Accuracy** | Overall correctness | (TP + TN) / Total | &gt;0.85 |</span>
<span>| **Precision** | When it says "High Risk", how often is it right? | TP / (TP + FP) | &gt;0.80 |</span>
<span>| **Recall** | Of all actual "High Risk", how many did we catch? | TP / (TP + FN) | &gt;0.80 |</span>
<span>| **F1 Score** | Harmonic mean of precision &amp; recall | 2 × (P × R) / (P + R) | &gt;0.80 |</span>
<span>| **ROC-AUC** | Ability to separate classes | Area under ROC curve | &gt;0.90 |</span>
<span></span>
<span>### 1.2 Understanding Confusion Matrix</span>
<span></span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Predicted → Safe Low Medium High Extreme</span><br><span class="">Actual</span><br><span class="">Safe 382 45 18 5 0</span><br><span class="">Low 38 312 24 4 2</span><br><span class="">Medium 12 28 253 22 5</span><br><span class="">High 3 8 31 160 8</span><br><span class="">Extreme 0 4 12 13 111</span></p><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Legend:</span><br><span class="">✅ Correct predictions (diagonal): 382 + 312 + 253 + 160 + 111 = 1,218</span><br><span class="">❌ Wrong predictions (off-diagonal): Everything else = 282</span><br><span class="">📊 Accuracy = 1,218 / 1,500 = 0.812 (81.2%)</span></p><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">text</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span></span>
<span>---</span>
<span></span>
<span>## Part 2: Complete Evaluation Script</span>
<span></span>
<span>```python</span>
<span># scripts/run_evaluation.py</span>
<span></span>
<span>import joblib</span>
<span>import numpy as np</span>
<span>import pandas as pd</span>
<span>import matplotlib.pyplot as plt</span>
<span>import seaborn as sns</span>
<span>from sklearn.metrics import (</span>
<span>    accuracy_score,</span>
<span>    precision_score,</span>
<span>    recall_score,</span>
<span>    f1_score,</span>
<span>    roc_auc_score,</span>
<span>    confusion_matrix,</span>
<span>    classification_report</span>
<span>)</span>
<span>from datetime import datetime</span>
<span>import json</span>
<span></span>
<span>class ModelEvaluator:</span>
<span>    """</span>
<span>    Comprehensive model evaluation suite.</span>
<span>    """</span>
<span>    </span>
<span>    def __init__(self, model_path: str):</span>
<span>        """</span>
<span>        Initialize evaluator with trained model.</span>
<span>        </span>
<span>        Args:</span>
<span>            model_path: Path to .pkl model file</span>
<span>        """</span>
<span>        </span>
<span>        data = joblib.load(model_path)</span>
<span>        </span>
<span>        if isinstance(data, dict):</span>
<span>            self.model = data['model']</span>
<span>            self.feature_names = data.get('feature_names')</span>
<span>        else:</span>
<span>            self.model = data</span>
<span>            self.feature_names = None</span>
<span>        </span>
<span>        print(f"✅ Loaded model from {model_path}")</span>
<span>    </span>
<span>    def evaluate(</span>
<span>        self,</span>
<span>        X_test: pd.DataFrame,</span>
<span>        y_test: pd.Series,</span>
<span>        output_dir: str = "reports"</span>
<span>    ):</span>
<span>        """</span>
<span>        Run full evaluation on test set.</span>
<span>        </span>
<span>        Args:</span>
<span>            X_test: Test features</span>
<span>            y_test: Test labels</span>
<span>            output_dir: Directory to save reports</span>
<span>        """</span>
<span>        </span>
<span>        print("=" * 60)</span>
<span>        print("MODEL EVALUATION")</span>
<span>        print("=" * 60)</span>
<span>        </span>
<span>        # Make predictions</span>
<span>        y_pred = self.model.predict(X_test)</span>
<span>        y_proba = self.model.predict_proba(X_test)</span>
<span>        </span>
<span>        # Calculate metrics</span>
<span>        metrics = self._calculate_metrics(y_test, y_pred, y_proba)</span>
<span>        </span>
<span>        # Print results</span>
<span>        self._print_metrics(metrics)</span>
<span>        </span>
<span>        # Generate confusion matrix</span>
<span>        cm = confusion_matrix(y_test, y_pred)</span>
<span>        self._plot_confusion_matrix(cm, output_dir)</span>
<span>        </span>
<span>        # Generate classification report</span>
<span>        report = classification_report(</span>
<span>            y_test, y_pred,</span>
<span>            target_names=['Safe', 'Low Risk', 'Medium Risk', 'High Risk', 'Extreme Risk']</span>
<span>        )</span>
<span>        print("\n📊 Classification Report:")</span>
<span>        print(report)</span>
<span>        </span>
<span>        # Feature importance</span>
<span>        self._plot_feature_importance(output_dir)</span>
<span>        </span>
<span>        # ROC curves</span>
<span>        self._plot_roc_curves(y_test, y_proba, output_dir)</span>
<span>        </span>
<span>        # Per-class performance</span>
<span>        self._analyze_per_class_performance(y_test, y_pred, output_dir)</span>
<span>        </span>
<span>        # Save metrics to JSON</span>
<span>        self._save_metrics(metrics, output_dir)</span>
<span>        </span>
<span>        # Determine if model passes</span>
<span>        passes = self._check_thresholds(metrics)</span>
<span>        </span>
<span>        return {</span>
<span>            'metrics': metrics,</span>
<span>            'passes': passes,</span>
<span>            'confusion_matrix': cm.tolist(),</span>
<span>            'classification_report': report</span>
<span>        }</span>
<span>    </span>
<span>    def _calculate_metrics(self, y_true, y_pred, y_proba):</span>
<span>        """Calculate all evaluation metrics."""</span>
<span>        </span>
<span>        # Basic metrics</span>
<span>        accuracy = accuracy_score(y_true, y_pred)</span>
<span>        precision_macro = precision_score(y_true, y_pred, average='macro')</span>
<span>        recall_macro = recall_score(y_true, y_pred, average='macro')</span>
<span>        f1_macro = f1_score(y_true, y_pred, average='macro')</span>
<span>        f1_weighted = f1_score(y_true, y_pred, average='weighted')</span>
<span>        </span>
<span>        # ROC-AUC (One-vs-Rest)</span>
<span>        try:</span>
<span>            roc_auc = roc_auc_score(y_true, y_proba, multi_class='ovr', average='macro')</span>
<span>        except:</span>
<span>            roc_auc = 0.0</span>
<span>        </span>
<span>        # Per-class metrics</span>
<span>        precision_per_class = precision_score(y_true, y_pred, average=None)</span>
<span>        recall_per_class = recall_score(y_true, y_pred, average=None)</span>
<span>        f1_per_class = f1_score(y_true, y_pred, average=None)</span>
<span>        </span>
<span>        return {</span>
<span>            'accuracy': accuracy,</span>
<span>            'precision_macro': precision_macro,</span>
<span>            'recall_macro': recall_macro,</span>
<span>            'f1_macro': f1_macro,</span>
<span>            'f1_weighted': f1_weighted,</span>
<span>            'roc_auc': roc_auc,</span>
<span>            'precision_per_class': precision_per_class.tolist(),</span>
<span>            'recall_per_class': recall_per_class.tolist(),</span>
<span>            'f1_per_class': f1_per_class.tolist(),</span>
<span>            'n_samples': len(y_true),</span>
<span>            'n_correct': int(accuracy * len(y_true))</span>
<span>        }</span>
<span>    </span>
<span>    def _print_metrics(self, metrics):</span>
<span>        """Pretty print metrics."""</span>
<span>        </span>
<span>        print("\n📈 Performance Metrics:")</span>
<span>        print(f"   Accuracy:  {metrics['accuracy']:.4f} ({metrics['n_correct']}/{metrics['n_samples']})")</span>
<span>        print(f"   Precision: {metrics['precision_macro']:.4f}")</span>
<span>        print(f"   Recall:    {metrics['recall_macro']:.4f}")</span>
<span>        print(f"   F1 Score:  {metrics['f1_macro']:.4f}")</span>
<span>        print(f"   ROC-AUC:   {metrics['roc_auc']:.4f}")</span>
<span>        </span>
<span>        print("\n📊 Per-Class F1 Scores:")</span>
<span>        class_names = ['Safe', 'Low', 'Medium', 'High', 'Extreme']</span>
<span>        for i, (name, f1) in enumerate(zip(class_names, metrics['f1_per_class'])):</span>
<span>            emoji = "✅" if f1 &gt;= 0.70 else "⚠️" if f1 &gt;= 0.50 else "❌"</span>
<span>            print(f"   {emoji} {name:10s}: {f1:.4f}")</span>
<span>    </span>
<span>    def _plot_confusion_matrix(self, cm, output_dir):</span>
<span>        """Plot and save confusion matrix."""</span>
<span>        </span>
<span>        fig, ax = plt.subplots(figsize=(10, 8))</span>
<span>        </span>
<span>        sns.heatmap(</span>
<span>            cm,</span>
<span>            annot=True,</span>
<span>            fmt='d',</span>
<span>            cmap='Blues',</span>
<span>            xticklabels=['Safe', 'Low', 'Medium', 'High', 'Extreme'],</span>
<span>            yticklabels=['Safe', 'Low', 'Medium', 'High', 'Extreme'],</span>
<span>            ax=ax</span>
<span>        )</span>
<span>        </span>
<span>        ax.set_xlabel('Predicted')</span>
<span>        ax.set_ylabel('Actual')</span>
<span>        ax.set_title('Confusion Matrix')</span>
<span>        </span>
<span>        plt.tight_layout()</span>
<span>        plt.savefig(f"{output_dir}/confusion_matrix.png", dpi=150)</span>
<span>        plt.close()</span>
<span>        </span>
<span>        print(f"   ✓ Saved confusion matrix to {output_dir}/confusion_matrix.png")</span>
<span>    </span>
<span>    def _plot_feature_importance(self, output_dir):</span>
<span>        """Plot feature importance."""</span>
<span>        </span>
<span>        if hasattr(self.model, 'feature_importances_') and self.feature_names:</span>
<span>            importances = self.model.feature_importances_</span>
<span>            </span>
<span>            # Sort by importance</span>
<span>            indices = np.argsort(importances)[::-1]</span>
<span>            </span>
<span>            fig, ax = plt.subplots(figsize=(10, 6))</span>
<span>            </span>
<span>            ax.barh(range(len(importances)), importances[indices])</span>
<span>            ax.set_yticks(range(len(importances)))</span>
<span>            ax.set_yticklabels([self.feature_names[i] for i in indices])</span>
<span>            ax.set_xlabel('Feature Importance')</span>
<span>            ax.set_title('XGBoost Feature Importance')</span>
<span>            ax.invert_yaxis()</span>
<span>            </span>
<span>            plt.tight_layout()</span>
<span>            plt.savefig(f"{output_dir}/feature_importance.png", dpi=150)</span>
<span>            plt.close()</span>
<span>            </span>
<span>            print(f"   ✓ Saved feature importance to {output_dir}/feature_importance.png")</span>
<span>    </span>
<span>    def _plot_roc_curves(self, y_true, y_proba, output_dir):</span>
<span>        """Plot ROC curves for each class."""</span>
<span>        </span>
<span>        from sklearn.preprocessing import label_binarize</span>
<span>        </span>
<span>        # Binarize labels for ROC</span>
<span>        y_true_bin = label_binarize(y_true, classes=[0, 1, 2, 3, 4])</span>
<span>        </span>
<span>        fig, ax = plt.subplots(figsize=(10, 8))</span>
<span>        </span>
<span>        class_names = ['Safe', 'Low Risk', 'Medium Risk', 'High Risk', 'Extreme Risk']</span>
<span>        colors = ['green', 'yellowgreen', 'orange', 'orangered', 'darkred']</span>
<span>        </span>
<span>        for i in range(5):</span>
<span>            fpr, tpr, _ = roc_curve(y_true_bin[:, i], y_proba[:, i])</span>
<span>            auc = roc_auc_score(y_true_bin[:, i], y_proba[:, i])</span>
<span>            ax.plot(fpr, tpr, color=colors[i], lw=2, label=f'{class_names[i]} (AUC = {auc:.3f})')</span>
<span>        </span>
<span>        ax.plot([0, 1], [0, 1], 'k--', lw=1)</span>
<span>        ax.set_xlim([0.0, 1.0])</span>
<span>        ax.set_ylim([0.0, 1.05])</span>
<span>        ax.set_xlabel('False Positive Rate')</span>
<span>        ax.set_ylabel('True Positive Rate')</span>
<span>        ax.set_title('ROC Curves by Risk Class')</span>
<span>        ax.legend(loc='lower right')</span>
<span>        </span>
<span>        plt.tight_layout()</span>
<span>        plt.savefig(f"{output_dir}/roc_curves.png", dpi=150)</span>
<span>        plt.close()</span>
<span>        </span>
<span>        print(f"   ✓ Saved ROC curves to {output_dir}/roc_curves.png")</span>
<span>    </span>
<span>    def _analyze_per_class_performance(self, y_true, y_pred, output_dir):</span>
<span>        """Analyze where the model makes mistakes."""</span>
<span>        </span>
<span>        cm = confusion_matrix(y_true, y_pred)</span>
<span>        </span>
<span>        # Find most common misclassifications</span>
<span>        misclassifications = []</span>
<span>        for i in range(5):</span>
<span>            for j in range(5):</span>
<span>                if i != j and cm[i, j] &gt; 0:</span>
<span>                    misclassifications.append({</span>
<span>                        'actual': i,</span>
<span>                        'predicted': j,</span>
<span>                        'count': cm[i, j]</span>
<span>                    })</span>
<span>        </span>
<span>        misclassifications.sort(key=lambda x: x['count'], reverse=True)</span>
<span>        </span>
<span>        class_names = ['Safe', 'Low Risk', 'Medium Risk', 'High Risk', 'Extreme Risk']</span>
<span>        </span>
<span>        print("\n🔍 Most Common Misclassifications:")</span>
<span>        for m in misclassifications[:5]:</span>
<span>            print(f"   {class_names[m['actual']]} → {class_names[m['predicted']]}: {m['count']} cases")</span>
<span>        </span>
<span>        # Save to file</span>
<span>        with open(f"{output_dir}/misclassifications.json", 'w') as f:</span>
<span>            json.dump(misclassifications, f, indent=2)</span>
<span>    </span>
<span>    def _check_thresholds(self, metrics):</span>
<span>        """Check if model meets production thresholds."""</span>
<span>        </span>
<span>        thresholds = {</span>
<span>            'accuracy': 0.80,</span>
<span>            'f1_macro': 0.75,</span>
<span>            'roc_auc': 0.85</span>
<span>        }</span>
<span>        </span>
<span>        passed = True</span>
<span>        print("\n🎯 Production Threshold Check:")</span>
<span>        </span>
<span>        for metric, threshold in thresholds.items():</span>
<span>            value = metrics[metric]</span>
<span>            status = "✅ PASS" if value &gt;= threshold else "❌ FAIL"</span>
<span>            print(f"   {metric:12s}: {value:.4f} (need ≥{threshold}) {status}")</span>
<span>            if value &lt; threshold:</span>
<span>                passed = False</span>
<span>        </span>
<span>        # Check per-class F1</span>
<span>        min_f1 = min(metrics['f1_per_class'])</span>
<span>        if min_f1 &lt; 0.50:</span>
<span>            print(f"   per_class_f1: min={min_f1:.4f} ❌ FAIL (one class too low)")</span>
<span>            passed = False</span>
<span>        else:</span>
<span>            print(f"   per_class_f1: min={min_f1:.4f} ✅ PASS")</span>
<span>        </span>
<span>        return passed</span>
<span>    </span>
<span>    def _save_metrics(self, metrics, output_dir):</span>
<span>        """Save metrics to JSON file."""</span>
<span>        </span>
<span>        # Make serializable</span>
<span>        serializable_metrics = {}</span>
<span>        for key, value in metrics.items():</span>
<span>            if isinstance(value, np.ndarray):</span>
<span>                serializable_metrics[key] = value.tolist()</span>
<span>            elif isinstance(value, np.float32) or isinstance(value, np.float64):</span>
<span>                serializable_metrics[key] = float(value)</span>
<span>            elif isinstance(value, np.int64):</span>
<span>                serializable_metrics[key] = int(value)</span>
<span>            else:</span>
<span>                serializable_metrics[key] = value</span>
<span>        </span>
<span>        serializable_metrics['timestamp'] = datetime.now().isoformat()</span>
<span>        </span>
<span>        with open(f"{output_dir}/metrics.json", 'w') as f:</span>
<span>            json.dump(serializable_metrics, f, indent=2)</span>
<span>        </span>
<span>        print(f"   ✓ Saved metrics to {output_dir}/metrics.json")</span>
<span></span>
<span></span>
<span># Command-line interface</span>
<span>def main():</span>
<span>    import argparse</span>
<span>    </span>
<span>    parser = argparse.ArgumentParser(description='Evaluate trained model')</span>
<span>    parser.add_argument('--model', type=str, default='models/production/risk_model.pkl',</span>
<span>                        help='Path to model file')</span>
<span>    parser.add_argument('--test-data', type=str, default='data/test/test_features.parquet',</span>
<span>                        help='Path to test features')</span>
<span>    parser.add_argument('--test-labels', type=str, default='data/test/test_labels.parquet',</span>
<span>                        help='Path to test labels')</span>
<span>    parser.add_argument('--output', type=str, default='reports',</span>
<span>                        help='Output directory for reports')</span>
<span>    </span>
<span>    args = parser.parse_args()</span>
<span>    </span>
<span>    # Load test data</span>
<span>    X_test = pd.read_parquet(args.test_data)</span>
<span>    y_test = pd.read_parquet(args.test_labels).squeeze()</span>
<span>    </span>
<span>    # Evaluate</span>
<span>    evaluator = ModelEvaluator(args.model)</span>
<span>    results = evaluator.evaluate(X_test, y_test, args.output)</span>
<span>    </span>
<span>    # Summary</span>
<span>    print("\n" + "=" * 60)</span>
<span>    if results['passes']:</span>
<span>        print("✅ MODEL PASSES PRODUCTION THRESHOLDS")</span>
<span>        print("   Ready for deployment!")</span>
<span>    else:</span>
<span>        print("❌ MODEL DOES NOT PASS PRODUCTION THRESHOLDS")</span>
<span>        print("   Needs improvement before deployment")</span>
<span>    print("=" * 60)</span>
<span></span>
<span>if __name__ == "__main__":</span>
<span>    main()</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><hr style="background: none 0% 0% / auto repeat scroll padding-box border-box rgba(0, 0, 0, 0.1); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; height: 1px; margin: 32px 0px; display: block; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><h2 style="font: 700 22px / 32px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Part 3: Running Evaluation</span></h2><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">3.1 Basic Evaluation</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Run full evaluation</span></span>
<span>python scripts/run_evaluation.py</span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># With custom paths</span></span>
<span>python scripts/run_evaluation.py <span class="token punctuation" style="color: rgb(56, 58, 66);">\</span></span>
<span>    <span class="token parameter variable" style="color: rgb(64, 120, 242);">--model</span> models/staging/experiment_v2.pkl <span class="token punctuation" style="color: rgb(56, 58, 66);">\</span></span>
<span>    --test-data data/validation/test_features.parquet <span class="token punctuation" style="color: rgb(56, 58, 66);">\</span></span>
<span>    <span class="token parameter variable" style="color: rgb(64, 120, 242);">--output</span> reports/experiment_v2</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">3.2 Expected Output</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">text</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span>============================================================</span>
<span>MODEL EVALUATION</span>
<span>============================================================</span>
<span>✅ Loaded model from models/production/risk_model.pkl</span>
<span></span>
<span>📈 Performance Metrics:</span>
<span>   Accuracy:  0.8347 (1252/1500)</span>
<span>   Precision: 0.8234</span>
<span>   Recall:    0.8012</span>
<span>   F1 Score:  0.8124</span>
<span>   ROC-AUC:   0.9189</span>
<span></span>
<span>📊 Per-Class F1 Scores:</span>
<span>   ✅ Safe      : 0.8623</span>
<span>   ✅ Low       : 0.8345</span>
<span>   ✅ Medium    : 0.8012</span>
<span>   ✅ High      : 0.7734</span>
<span>   ✅ Extreme   : 0.8045</span>
<span></span>
<span>📊 Classification Report:</span>
<span>              precision    recall  f1-score   support</span>
<span>        Safe       0.88      0.85      0.86        90</span>
<span>     Low Risk       0.84      0.82      0.83        75</span>
<span>   Medium Risk       0.81      0.79      0.80        60</span>
<span>    High Risk       0.79      0.76      0.77        45</span>
<span>     Extreme       0.82      0.79      0.80        30</span>
<span></span>
<span>    accuracy                           0.83       300</span>
<span>   macro avg       0.83      0.80      0.81       300</span>
<span>weighted avg       0.83      0.83      0.83       300</span>
<span></span>
<span>   ✓ Saved confusion matrix to reports/confusion_matrix.png</span>
<span>   ✓ Saved feature importance to reports/feature_importance.png</span>
<span>   ✓ Saved ROC curves to reports/roc_curves.png</span>
<span></span>
<span>🔍 Most Common Misclassifications:</span>
<span>   Medium Risk → Low Risk: 28 cases</span>
<span>   Low Risk → Safe: 24 cases</span>
<span>   High Risk → Medium Risk: 22 cases</span>
<span>   Safe → Low Risk: 18 cases</span>
<span>   Extreme → High Risk: 13 cases</span>
<span></span>
<span>🎯 Production Threshold Check:</span>
<span>   accuracy    : 0.8347 (need ≥0.80) ✅ PASS</span>
<span>   f1_macro    : 0.8124 (need ≥0.75) ✅ PASS</span>
<span>   roc_auc     : 0.9189 (need ≥0.85) ✅ PASS</span>
<span>   per_class_f1: min=0.7734 ✅ PASS</span>
<span></span>
<span>============================================================</span>
<span>✅ MODEL PASSES PRODUCTION THRESHOLDS</span>
<span>   Ready for deployment!</span>
<span>============================================================</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><hr style="background: none 0% 0% / auto repeat scroll padding-box border-box rgba(0, 0, 0, 0.1); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; height: 1px; margin: 32px 0px; display: block; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><h2 style="font: 700 22px / 32px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Part 4: Validation Notebook</span></h2><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Create<span> </span></span><code style="box-sizing: border-box; font-style: normal; font-variant: normal; font-weight: 400; font-stretch: 100%; line-height: 22px; font-optical-sizing: auto; font-size-adjust: none; font-kerning: auto; font-feature-settings: normal; font-variation-settings: normal; font-language-override: normal; font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; background-color: rgb(235, 238, 242); border-radius: 6px; align-items: center; padding: 0px 5px; display: inline-flex; font-size: 0.875em !important;">notebooks/04_model_evaluation.ipynb</code><span class="">:</span></p><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">python</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Cell 1: Setup</span></span>
<span><span class="token keyword" style="color: rgb(166, 38, 164);">import</span> pandas <span class="token keyword" style="color: rgb(166, 38, 164);">as</span> pd</span>
<span><span class="token keyword" style="color: rgb(166, 38, 164);">import</span> numpy <span class="token keyword" style="color: rgb(166, 38, 164);">as</span> np</span>
<span><span class="token keyword" style="color: rgb(166, 38, 164);">import</span> matplotlib<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>pyplot <span class="token keyword" style="color: rgb(166, 38, 164);">as</span> plt</span>
<span><span class="token keyword" style="color: rgb(166, 38, 164);">import</span> seaborn <span class="token keyword" style="color: rgb(166, 38, 164);">as</span> sns</span>
<span><span class="token keyword" style="color: rgb(166, 38, 164);">from</span> sklearn<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>metrics <span class="token keyword" style="color: rgb(166, 38, 164);">import</span> confusion_matrix<span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> classification_report</span>
<span><span class="token keyword" style="color: rgb(166, 38, 164);">import</span> joblib</span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Cell 2: Load model and test data</span></span>
<span>model <span class="token operator" style="color: rgb(64, 120, 242);">=</span> joblib<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>load<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">'../models/production/risk_model.pkl'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>X_test <span class="token operator" style="color: rgb(64, 120, 242);">=</span> pd<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>read_parquet<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">'../data/test/test_features.parquet'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>y_test <span class="token operator" style="color: rgb(64, 120, 242);">=</span> pd<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>read_parquet<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">'../data/test/test_labels.parquet'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>squeeze<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Cell 3: Make predictions</span></span>
<span>y_pred <span class="token operator" style="color: rgb(64, 120, 242);">=</span> model<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>predict<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>X_test<span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>y_proba <span class="token operator" style="color: rgb(64, 120, 242);">=</span> model<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>predict_proba<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>X_test<span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Cell 4: Visualize predictions vs actual</span></span>
<span>fig<span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> axes <span class="token operator" style="color: rgb(64, 120, 242);">=</span> plt<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>subplots<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token number" style="color: rgb(183, 107, 1);">1</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> <span class="token number" style="color: rgb(183, 107, 1);">2</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> figsize<span class="token operator" style="color: rgb(64, 120, 242);">=</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token number" style="color: rgb(183, 107, 1);">14</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> <span class="token number" style="color: rgb(183, 107, 1);">5</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Distribution of actual vs predicted</span></span>
<span>actual_counts <span class="token operator" style="color: rgb(64, 120, 242);">=</span> y_test<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>value_counts<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>sort_index<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>pred_counts <span class="token operator" style="color: rgb(64, 120, 242);">=</span> pd<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>Series<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>y_pred<span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>value_counts<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>sort_index<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">0</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>bar<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>actual_counts<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>index <span class="token operator" style="color: rgb(64, 120, 242);">-</span> <span class="token number" style="color: rgb(183, 107, 1);">0.2</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> actual_counts<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>values<span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> width<span class="token operator" style="color: rgb(64, 120, 242);">=</span><span class="token number" style="color: rgb(183, 107, 1);">0.4</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> label<span class="token operator" style="color: rgb(64, 120, 242);">=</span><span class="token string" style="color: rgb(80, 161, 79);">'Actual'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">0</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>bar<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>pred_counts<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>index <span class="token operator" style="color: rgb(64, 120, 242);">+</span> <span class="token number" style="color: rgb(183, 107, 1);">0.2</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> pred_counts<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>values<span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> width<span class="token operator" style="color: rgb(64, 120, 242);">=</span><span class="token number" style="color: rgb(183, 107, 1);">0.4</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> label<span class="token operator" style="color: rgb(64, 120, 242);">=</span><span class="token string" style="color: rgb(80, 161, 79);">'Predicted'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">0</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>set_xlabel<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">'Risk Level'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">0</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>set_ylabel<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">'Count'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">0</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>set_title<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">'Distribution: Actual vs Predicted'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">0</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>legend<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">0</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>set_xticks<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">0</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span><span class="token number" style="color: rgb(183, 107, 1);">1</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span><span class="token number" style="color: rgb(183, 107, 1);">2</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span><span class="token number" style="color: rgb(183, 107, 1);">3</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span><span class="token number" style="color: rgb(183, 107, 1);">4</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Confidence histogram</span></span>
<span>confidences <span class="token operator" style="color: rgb(64, 120, 242);">=</span> np<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span><span class="token builtin" style="color: rgb(80, 161, 79);">max</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>y_proba<span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> axis<span class="token operator" style="color: rgb(64, 120, 242);">=</span><span class="token number" style="color: rgb(183, 107, 1);">1</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">1</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>hist<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>confidences<span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> bins<span class="token operator" style="color: rgb(64, 120, 242);">=</span><span class="token number" style="color: rgb(183, 107, 1);">20</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> edgecolor<span class="token operator" style="color: rgb(64, 120, 242);">=</span><span class="token string" style="color: rgb(80, 161, 79);">'black'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">1</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>set_xlabel<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">'Confidence'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">1</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>set_ylabel<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">'Count'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>axes<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span><span class="token number" style="color: rgb(183, 107, 1);">1</span><span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>set_title<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">'Prediction Confidence Distribution'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span></span>
<span>plt<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>tight_layout<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span>plt<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>show<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Cell 5: Error analysis</span></span>
<span>errors <span class="token operator" style="color: rgb(64, 120, 242);">=</span> y_test <span class="token operator" style="color: rgb(64, 120, 242);">!=</span> y_pred</span>
<span>error_df <span class="token operator" style="color: rgb(64, 120, 242);">=</span> pd<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>DataFrame<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span></span>
<span>    <span class="token string" style="color: rgb(80, 161, 79);">'actual'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span> y_test<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span>errors<span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span></span>
<span>    <span class="token string" style="color: rgb(80, 161, 79);">'predicted'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span> y_pred<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span>errors<span class="token punctuation" style="color: rgb(56, 58, 66);">]</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span></span>
<span>    <span class="token string" style="color: rgb(80, 161, 79);">'confidence'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span> confidences<span class="token punctuation" style="color: rgb(56, 58, 66);">[</span>errors<span class="token punctuation" style="color: rgb(56, 58, 66);">]</span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">}</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span></span>
<span><span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string-interpolation"><span class="token string" style="color: rgb(80, 161, 79);">f"Total errors: </span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span>errors<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span><span class="token builtin" style="color: rgb(80, 161, 79);">sum</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);"> / </span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span><span class="token builtin" style="color: rgb(80, 161, 79);">len</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>y_test<span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);"> (</span><span class="token interpolation"><span class="token punctuation" style="color: rgb(56, 58, 66);">{</span>errors<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span><span class="token builtin" style="color: rgb(80, 161, 79);">sum</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token operator" style="color: rgb(64, 120, 242);">/</span><span class="token builtin" style="color: rgb(80, 161, 79);">len</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>y_test<span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token operator" style="color: rgb(64, 120, 242);">*</span><span class="token number" style="color: rgb(183, 107, 1);">100</span><span class="token punctuation" style="color: rgb(56, 58, 66);">:</span><span class="token format-spec">.1f</span><span class="token punctuation" style="color: rgb(56, 58, 66);">}</span></span><span class="token string" style="color: rgb(80, 161, 79);">%)"</span></span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span><span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token string" style="color: rgb(80, 161, 79);">"\nLowest confidence predictions (most uncertain):"</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span>
<span><span class="token keyword" style="color: rgb(166, 38, 164);">print</span><span class="token punctuation" style="color: rgb(56, 58, 66);">(</span>error_df<span class="token punctuation" style="color: rgb(56, 58, 66);">.</span>nsmallest<span class="token punctuation" style="color: rgb(56, 58, 66);">(</span><span class="token number" style="color: rgb(183, 107, 1);">10</span><span class="token punctuation" style="color: rgb(56, 58, 66);">,</span> <span class="token string" style="color: rgb(80, 161, 79);">'confidence'</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span><span class="token punctuation" style="color: rgb(56, 58, 66);">)</span></span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><hr style="background: none 0% 0% / auto repeat scroll padding-box border-box rgba(0, 0, 0, 0.1); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; height: 1px; margin: 32px 0px; display: block; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><h2 style="font: 700 22px / 32px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Quick Reference</span></h2><div class="ds-scroll-area ds-scroll-area--show-on-focus-within ds-scroll-area--enabled _1210dd7 c03cafe9" style="--dsl-scroll-area-gutters-disappear-delay: 1s; z-index: 0; position: relative; overflow: auto; scrollbar-width: none; --padding-left: calc(( 1280px - (840px - 2 * 44px) ) / 2 + (840px - 2 * 44px - 100%)); --padding-right: 54px; width: calc(100% + 210px); padding-left: calc(-100% + 1016px); padding-right: 54px; margin-left: calc(100% - 1016px); color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="ds-scroll-area__gutters" style="--dsl-scroll-area-scrollbar-bg: #e5e5e5; --dsl-scroll-area-scrollbar-hover: #d4d4d4; --dsl-scroll-area-horizontal-gutter-padding: 2px 0; --dsl-scroll-area-vertical-gutter-padding: 0 2px; pointer-events: none; z-index: 1000; transition: opacity 0.1s ease-out 1s; opacity: 1 !important; display: block; --container-height: 230px; position: sticky; top: 0px; left: 0px; right: 0px; width: 962px; height: 0px;"><div class="ds-scroll-area__horizontal-gutter" style="position: absolute; padding: 2px 0px; left: 0px; right: 0px; display: block; top: 216px; height: 10px;"></div><div class="ds-scroll-area__vertical-gutter" style="position: absolute; padding: 0px 2px; right: 0px; top: 8px; bottom: -222px; width: 10px;"></div></div>
Metric | Target | Current | Status
-- | -- | -- | --
Accuracy | >0.80 | 0.83 | ✅
F1 Score | >0.75 | 0.81 | ✅
ROC-AUC | >0.85 | 0.92 | ✅
Per-class F1 (min) | >0.50 | 0.77 | ✅

</div><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong style="font-weight: 600;"><span class="">Model Status:</span></strong><span class=""><span> </span>✅ PRODUCTION READY</span></p><hr style="background: none 0% 0% / auto repeat scroll padding-box border-box rgba(0, 0, 0, 0.1); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; height: 1px; margin: 32px 0px; display: block; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><em><span class="">Last updated: June 2026</span></em></p><!--EndFragment-->
</body>
</html>