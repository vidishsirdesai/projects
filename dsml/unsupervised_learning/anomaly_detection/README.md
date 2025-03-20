# Introduction
Anomaly detection is the art of identifying data points that deviate significantly from the expected or "normal" behavior. These data points are often called,
- Anomalies: A general term for anything unexpected or out of ordinary.
- Outliers: Data points that fall far away from the majority of the data in a dataset.
- Novelties: Previously unseen data points that represent entirely new patterns.

### Anomaly v. novelty
Both are anomalies, but with a subtle difference. Novelties are entirely new and have not been observed before, like using Zoom during a pandemic. Outliers, on the other hand, deviate from the established norm, like a cricket match with a usually high scoring over.

### Real v. unreal anomalies
Novelties oftem have real world explanations, like economic factors influencing a new trend. Outliers, however can sometimes be caused by errors, like a data entry mistake or environmental factors.

### Why detect anomalies?
Imagine building a model to predict house prices. An outlier like Bill Gates' house might distort the model's understanding of typical house prices. This is where anomaly detection comes in. It helps identify and potentially remove outliers that could skew the results of data analysis or machine learning models.


# Impact of Anomaly Detection in Different Fields
Anomaly detection plays a vital role in various fields,
- Fraud detection: Identifying unusual transactions that might indicate fradulent activity.
- Network intrusion detection: Spotting suspicious network traffic that could be a security threat.
- Medical diagnosis: Detecting abnormal patterns in patient data that might indicate a health.

# Simple Techniques used for Anomaly Detection
- Box plot.
- Z-score.
- IQR analysis.
- Visualize and remove manually (plot the data using scatter plot, and filter the data).