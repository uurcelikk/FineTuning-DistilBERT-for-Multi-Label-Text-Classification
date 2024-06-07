# FineTuning-DistilBERT-for-Multi-Label-Text-Classification

This repository contains the code and resources for fine-tuning the DistilBERT model for multi-label text classification. The project involves using a dataset of quotes with multiple tags and fine-tuning a pre-trained DistilBERT model to classify these quotes into appropriate tags.

## Repository Structure

- `.gitattributes`: Initial configuration file.
- `Main.ipynb`: Jupyter Notebook containing the main workflow for data processing, model training, and evaluation.
- `README.md`: This file, providing an overview and instructions for the project.
- `scrape.py`: Script to scrape or preprocess the data.

## Dataset

The dataset used in this project consists of quotes with associated authors and tags. Here is a brief overview of the dataset structure:

| Quote                                                                 | Author         | Tags                                   |
|-----------------------------------------------------------------------|----------------|----------------------------------------|
| "The world as we have created it is a process of our thinking..."     | Albert Einstein| ['change', 'deep-thoughts', 'thinking']|
| "It is our choices, Harry, that show what we truly are..."            | J.K. Rowling   | ['abilities', 'choices']               |
| "There are only two ways to live your life. One is as though nothing is a miracle..." | Albert Einstein | ['inspirational', 'life']              |

## Data Preparation

1. **Loading the Data**: The dataset is loaded from a CSV file.
2. **Exploratory Data Analysis (EDA)**: Basic analysis is performed to understand the distribution of authors and tags.
3. **Text and Label Preprocessing**:
    - Quotes are tokenized using the DistilBERT tokenizer.
    - Tags are binarized using `MultiLabelBinarizer` to create a multi-label classification problem.

## Model Training

1. **Train-Test Split**: The dataset is split into training and validation sets.
2. **Model Initialization**:
    - The DistilBERT model is loaded with a classification head for multi-label classification.
3. **Custom Dataset Class**: A custom dataset class is implemented to handle the tokenization and formatting of inputs.
4. **Training Arguments**: Define the training parameters including batch size, number of epochs, and evaluation steps.
5. **Trainer**: The HuggingFace Trainer is used to handle the training loop, including evaluation metrics.

## Evaluation Metrics

- **ROC-AUC Score**
- **F1 Score**
- **Hamming Loss**

These metrics are computed using a custom function to handle multi-label classification outputs.

## Usage

### Requirements

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `torch`
- `transformers`
- `sklearn`

Install the required packages using pip:
```bash
pip install -U numpy pandas matplotlib seaborn torch transformers sklearn accelerate
