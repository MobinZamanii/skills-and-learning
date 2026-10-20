# Deep Learning with Python

A structured, practical, and continuously evolving learning repository covering Deep Learning with Python — from mathematical foundations and neural networks to modern frameworks, advanced architectures, and real-world applications.

The goal of this repository is to build a strong understanding of Deep Learning through **clear explanations, mathematical intuition, commented code, visualizations, hands-on exercises, and practical projects**.

This repository is designed for self-study, teaching, experimentation, and demonstrating practical machine learning skills.

---

## Objectives

- Understand the mathematical foundations behind Deep Learning.
- Build neural networks from scratch using NumPy.
- Learn PyTorch, Keras, and TensorFlow through practical examples.
- Understand tensors, automatic differentiation, loss functions, and optimization.
- Implement, train, evaluate, and improve neural networks.
- Explore modern Deep Learning architectures and techniques.
- Apply Deep Learning to real-world datasets and projects.
- Develop reusable code and a strong practical portfolio.

## Learning Path

The repository follows a progressive learning structure. Each stage builds on concepts introduced in earlier stages.

### 1. Foundations of Deep Learning

Build the mathematical and conceptual knowledge needed to understand neural networks.

Topics include:

- Introduction to Deep Learning
- Mathematical foundations
- Linear algebra and matrix operations
- Derivatives and the chain rule
- Activation functions
- Loss functions
- Gradient descent and optimization
- Neural networks from scratch
- Forward propagation and backpropagation

**Goal:** Understand how neural networks work before relying on high-level frameworks.

### 2. PyTorch

Start with PyTorch to develop a practical understanding of tensor computation, automatic differentiation, and neural network training.

Topics include:

- PyTorch fundamentals
- Tensors, shapes, dimensions, and data types
- Tensor creation and manipulation
- CPU and GPU computation
- Automatic differentiation with `autograd`
- Datasets and `DataLoader`
- Building models with `torch.nn`
- Loss functions and optimizers
- Training and evaluation loops
- Model saving and loading
- Training visualization and debugging
- Custom datasets and reusable training workflows

**Goal:** Develop the ability to implement and train neural networks with a flexible, low-level workflow.

### 3. Keras

Move to Keras to learn a more concise and high-level approach to building Deep Learning models.

Topics include:

- Keras fundamentals
- Sequential and Functional APIs
- Layers and model construction
- Compilation and training
- Loss functions and metrics
- Optimizers and callbacks
- Validation and overfitting
- Model evaluation and prediction
- Saving and loading models
- Comparing Keras workflows with PyTorch

**Goal:** Build neural networks efficiently while understanding the training process and model design.

### 4. TensorFlow

Explore TensorFlow to understand its computational tools and broader ecosystem for Deep Learning.

Topics include:

- TensorFlow fundamentals
- Tensor operations
- Variables and automatic differentiation
- `tf.GradientTape`
- Data pipelines with `tf.data`
- Model training and evaluation
- GPU acceleration
- Model serialization and deployment basics
- TensorFlow and Keras integration
- Comparing TensorFlow and PyTorch

**Goal:** Understand TensorFlow workflows and become comfortable working across major Deep Learning frameworks.

### 5. Core Neural Network Architectures

Apply the concepts and tools learned in the previous stages to important neural network architectures.

Topics include:

- Artificial Neural Networks (ANNs)
- Multilayer Perceptrons (MLPs)
- Convolutional Neural Networks (CNNs)
- Recurrent Neural Networks (RNNs)
- Long Short-Term Memory (LSTM)
- Gated Recurrent Units (GRU)
- Autoencoders
- Attention mechanisms
- Transformers

**Goal:** Understand the purpose, architecture, strengths, and limitations of different neural network models.

### 6. Training, Optimization, and Evaluation

Learn how to improve model performance and make reliable evaluations.

Topics include:

- Learning rates and learning-rate schedules
- SGD, Momentum, RMSprop, and Adam
- Weight initialization
- Batch normalization and regularization
- Dropout and weight decay
- Overfitting and underfitting
- Training, validation, and test splits
- Classification and regression metrics
- Confusion matrices
- Precision, recall, and F1 score
- ROC curves and ROC-AUC
- Hyperparameter tuning
- Reproducibility and experiment tracking

**Goal:** Train models more effectively and evaluate their performance appropriately.

### 7. Computer Vision and Image Deep Learning

Explore Deep Learning techniques for image analysis and visual recognition.

Topics include:

- Image preprocessing and augmentation
- CNN architectures
- Transfer learning
- Fine-tuning pretrained models
- Image classification
- Object detection
- Image segmentation
- Vision Transformers
- Model interpretation and visualization

**Goal:** Develop practical computer vision skills using real datasets.

### 8. Natural Language Processing and Transformers

Study neural networks for text, language, and sequence-based data.

Topics include:

- Text preprocessing and tokenization
- Word embeddings
- Sequence modeling
- Attention mechanisms
- Transformer architecture
- Encoder and decoder models
- Transfer learning for NLP
- Text classification
- Introduction to pretrained language models

**Goal:** Understand modern approaches to language modeling and text-based Deep Learning.

### 9. Advanced Topics

Expand into modern architectures and techniques as the repository grows.

Potential topics include:

- Generative Adversarial Networks (GANs)
- Variational Autoencoders (VAEs)
- Diffusion models
- Self-supervised learning
- Contrastive learning
- Representation learning
- Distributed training
- Model compression and quantization
- Efficient inference
- Model deployment

**Goal:** Explore advanced concepts and understand how they are used in modern Deep Learning systems.

### 10. Practical Projects

Use the concepts from previous sections to build complete, reproducible projects.

Potential project areas include:

- Binary and multiclass classification
- Regression
- Image classification
- Image segmentation
- Time-series forecasting
- Text classification
- Transfer learning
- Biomedical image analysis
- Deep Learning for biological data

Each project should include a problem definition, dataset description, preprocessing, model implementation, training, evaluation, visualizations, and conclusions.

---
## Learning Philosophy

The repository emphasizes understanding over memorization.

Each notebook aims to include, where appropriate:

- **Conceptual explanations** — what a method does and why it matters.
- **Mathematical foundations** — equations and intuition behind algorithms.
- **Commented code** — readable implementations with meaningful explanations.
- **Practical examples** — runnable code using NumPy, PyTorch, Keras, or TensorFlow.
- **Visualizations** — plots that help explain model behavior.
- **Evaluation** — appropriate metrics and interpretation of results.
- **Exercises** — opportunities to practice and extend the material.
- **Quick reference** — key functions, concepts, and common mistakes.

The goal is not simply to make models work, but to understand how they work, how to evaluate them, and when to use them.

---

## Technologies

The repository focuses on Python and the following tools:

- Python
- Jupyter Notebook
- NumPy
- Matplotlib
- scikit-learn
- PyTorch
- Keras
- TensorFlow

Additional libraries may be introduced when needed for specific topics or projects.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MobinZamanii/skills-and-learning.git
cd skills-and-learning
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install the basic dependencies

```bash
python -m pip install --upgrade pip
pip install numpy matplotlib scikit-learn jupyter
```

Install PyTorch, TensorFlow, and other framework-specific dependencies according to the notebook you want to run. For PyTorch, choose the appropriate installation command for your operating system and hardware from the official installation guide.

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Start with Notebook 01 and continue through the learning path. Some notebooks may be explored independently once their prerequisites are understood.

---
##  Contributions and Feedback

Suggestions, corrections, and improvements are welcome.

If you find an issue or have an idea for a useful example, feel free to open an issue or propose a contribution.

## License

A license can be added to define how the code and educational materials may be reused and distributed.

---

**Learn the mathematics. Understand the models. Write the code. Build practical skills.**

