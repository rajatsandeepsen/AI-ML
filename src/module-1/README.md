# Module 1: AI/ML Fundamentals

## Introduction to AI, ML, and DL

### Artificial Intelligence vs Machine Learning vs Deep Learning

**Artificial Intelligence (AI)** is the broad field of computer science focused on creating intelligent systems that can perform tasks requiring human-like intelligence. This includes reasoning, problem-solving, perception, and language understanding.

**Machine Learning (ML)** is a subset of AI that enables systems to learn from data and improve their performance without being explicitly programmed. Instead of following hardcoded rules, ML algorithms identify patterns and make predictions based on examples.

**Deep Learning (DL)** is a specialized subset of machine learning that uses artificial neural networks with multiple layers (hence "deep") to learn hierarchical representations of data. DL excels at processing unstructured data like images, audio, and text.

```
AI (Broad)
 └── Machine Learning
      └── Deep Learning
```

---

## Types of Machine Learning

Machine learning problems are typically categorized into three main paradigms:

### Supervised Learning

**Supervised learning** trains on labeled data—where both input features and correct output (target) are provided. The algorithm learns to map inputs to outputs by minimizing prediction errors.

**Common Tasks:**
- **Classification**: Predicting discrete categories (e.g., spam detection, image classification)
- **Regression**: Predicting continuous values (e.g., house price prediction, stock price forecasting)

**Examples:**
- Email spam classification (spam / not spam)
- Predicting house prices based on features
- Medical diagnosis from patient data

**Advantages:** Clear performance metrics, faster convergence with sufficient labeled data
**Disadvantages:** Requires expensive labeled data collection

---

### Unsupervised Learning

**Unsupervised learning** works with unlabeled data, discovering hidden patterns, structures, or relationships without predefined target outputs. The algorithm must find meaning in the data independently.

**Common Tasks:**
- **Clustering**: Grouping similar data points together (e.g., customer segmentation)
- **Dimensionality Reduction**: Compressing data while preserving important information
- **Anomaly Detection**: Identifying unusual or outlier patterns

**Examples:**
- Customer segmentation for targeted marketing
- Gene sequencing and biological data analysis
- Detecting fraudulent transactions in financial data

**Advantages:** Requires no labeled data, discovers novel patterns humans might miss
**Disadvantages:** Harder to evaluate, may find spurious patterns

---

### Reinforcement Learning

**Reinforcement Learning (RL)** trains an agent to make sequences of decisions by rewarding desired behaviors and penalizing undesired ones. The agent learns through trial-and-error interaction with an environment.

**Key Concepts:**
- **Agent**: The decision-maker
- **Environment**: The system the agent interacts with
- **Reward**: Feedback signal indicating action quality
- **Policy**: Strategy mapping observations to actions

**Examples:**
- Game AI (chess, Go, video games)
- Robotic control and navigation
- Autonomous vehicle decision-making
- Resource optimization

**Advantages:** Learns optimal strategies through interaction, handles sequential decision problems
**Disadvantages:** Computationally expensive, requires careful reward design

---
