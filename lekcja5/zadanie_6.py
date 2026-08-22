model_name = "XGBoost"
accuracy = 0.8934
training_time = 45.67

report = f"""Model: {model_name}
    Accuracy: {accuracy * 100:.2f}%
    Training time: {training_time:.2f}s"""

print(report)