# AI & NLP Exam Project – ESG and Risk Classification

## Overview

This repository contains the final exam project for the course **Artificial Intelligence and Machine Learning (KAN-CINTO4003U)** at Copenhagen Business School, Fall 2025. The project explores the application of Natural Language Processing (NLP) techniques—including Bag of Words (BoW), BERT, and large language models (LLMs)—to classify and extract information from corporate ESG reports and 10-K filings.

## Objective

The primary objective of the project is to assess the effectiveness of different NLP approaches in identifying ESG-related content and evaluating corporate risk exposure. We compare traditional and modern NLP techniques across multiple datasets to analyze their performance in classification and information extraction tasks.

## Data Sources

- **ESG Reports**: Manually downloaded from official company websites.
- **10-K Filings**: Retrieved via the SEC API at [https://sec-api.io](https://sec-api.io).

## Methodology

We implemented and compared the following methods:

- **BoW + Logistic Regression**: A classic baseline approach using term frequency vectors.
- **BERT-based Classification**: Fine-tuning pretrained transformer models for ESG/risk labeling.
- **LLM Zero-Shot / Few-Shot**: Using decoder-only large language models (e.g., GPT-4, WatsonX) to extract and classify text without explicit fine-tuning.

## Structure
📂 data/ # Contains raw and preprocessed ESG and 10-K data
📂 notebooks/ # Jupyter notebooks for exploration and model evaluation
📂 models/ # Saved model checkpoints and configurations
📄 requirements.txt # List of Python dependencies
📄 main.py # Entry point for running classification tasks
📄 report.pdf # Final exam report (PDF version)


## Results

The results showed that LLMs outperformed traditional methods in capturing nuanced ESG-related content and context-dependent risk indicators, particularly in unstructured report sections. However, BERT models provided a competitive balance of performance and efficiency in structured classification tasks.

## Installation

bash
git clone https://github.com/[your-username]/esg-risk-nlp.git
cd esg-risk-nlp
pip install -r requirements.txt

Reproducibility
All scripts are provided with clear instructions and can be run end-to-end to reproduce the results presented in the report. Make sure you have the correct API keys if you intend to re-fetch data.

License
This project is for academic purposes only and is released under the MIT License.
