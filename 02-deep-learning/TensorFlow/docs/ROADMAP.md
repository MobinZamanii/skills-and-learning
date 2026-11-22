# Course Roadmap

The course is organized into four parts and twelve notebooks. Each notebook is intended to be studied in sequence and includes a combination of theory, equations, implementation, visualization, evaluation, and exercises.

## Part I — Foundations of Deep Learning

### 01. Introduction to Deep Learning and Neural Networks
Artificial intelligence, machine learning, deep learning, artificial neurons, weights and biases, activation functions, feedforward architecture, forward propagation, and a first TensorFlow/Keras model.

### 02. Mathematical Foundations of Neural Networks
Scalars, vectors, matrices, tensors, linear algebra, matrix multiplication, affine transformations, derivatives, partial derivatives, gradients, chain rule, loss functions, gradient descent, numerical gradient checking, and NumPy backpropagation.

### 03. TensorFlow, Keras and Data Pipelines
Tensor creation and manipulation, tensor shapes, broadcasting, automatic differentiation, `tf.GradientTape`, eager execution, `tf.function`, Keras Sequential/Functional/subclassing APIs, `tf.data`, preprocessing, splitting, batching, and prefetching.

## Part II — Neural Networks and Model Training

### 04. Artificial Neural Networks and Regression
MLP architecture, dense layers, regression outputs, MSE/MAE/Huber loss, model compilation, training, evaluation, predictions, baseline comparisons, and residual analysis.

### 05. Neural Network Classification
Binary classification, logits and probabilities, sigmoid, binary cross-entropy, thresholds, confusion matrices, precision, recall, specificity, F1, ROC-AUC, precision-recall analysis, class imbalance, and calibration concepts.

### 06. Multiclass Classification and Model Evaluation
Binary/multiclass/multilabel distinctions, integer and one-hot encoding, softmax, categorical and sparse categorical cross-entropy, class weighting, confusion matrices, macro/micro/weighted metrics, multiclass ROC-AUC, average precision, and error analysis.

### 07. Optimization, Regularization and Custom Training
Backpropagation, batch strategies, SGD, momentum, RMSprop, Adam, AdamW, learning-rate schedules, initialization, gradient flow, L1/L2 penalties, dropout, batch normalization, early stopping, checkpointing, TensorBoard, gradient clipping, and custom training loops.

## Part III — Deep Learning Architectures

### 08. Convolutional Neural Networks
Image tensors, convolution/cross-correlation, kernels, filters, stride, padding, feature maps, pooling, flattening, global average pooling, CNN design, augmentation, training, and feature-map inspection.

### 09. Transfer Learning and Pretrained Models
ImageNet-pretrained backbones, MobileNetV2, ResNet, EfficientNet, architecture-specific preprocessing, frozen feature extraction, classification heads, unfreezing, fine-tuning, Batch Normalization considerations, and domain shift.

### 10. Sequential Deep Learning: RNN, LSTM, GRU and Transformers
Sequence data, time-series windows, chronological splitting, RNN hidden states, vanishing/exploding gradients, LSTM gates, GRU, bidirectional recurrence, attention, query/key/value, multi-head attention, positional encoding, Transformer encoders, and forecasting.

## Part IV — Advanced Applications and Interpretation

### 11. Autoencoders and Unsupervised Deep Learning
Encoder/decoder architectures, latent representations, bottlenecks, reconstruction losses, undercomplete and sparse autoencoders, denoising autoencoders, variational autoencoders, reparameterization, KL divergence, and reconstruction-based anomaly detection.

### 12. Capstone: Biological Image Classification and Explainable AI
Problem definition, exploratory analysis, specimen-level splits, preprocessing, CNN and transfer-learning comparison, model selection, internal and simulated external evaluation, ROC/PR analysis, calibration, error analysis, Grad-CAM, reproducibility, serialization, and model cards.

## Suggested study sequence

- Complete Part I before training larger models.
- Complete Part II before moving to computer vision architectures.
- Compare the CNN and transfer-learning workflows in Notebooks 08 and 09.
- Study sequential models and autoencoders before the capstone.
- Treat Notebook 12 as a synthesis exercise, not as evidence of clinical readiness.
