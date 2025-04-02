# Recommendation System

## Description

This is a recommendation system that recommends users based on their skills.

## Usage
1. import the requirement
```bash
pip install -r requirements.txt
```
2. run the server
```bash
python main.py
```

## API

```bash
http://localhost:5000/recommend?user_id=1&top_n=3
```

## Data

The data is in the `data.csv` file.

## Theory

$[[TF-IDF (Term Frequency-Inverse Document Frequency)]]$ is a statistical measure used to evaluate the importance of a word in a document. It is often used in information retrieval and text mining to rank documents based on their relevance to a query.

$[[Cosine Similarity]]$ is a measure of similarity between two vectors of an inner product space that measures the cosine of the angle between them. It is used to measure how similar two documents are, regardless of their size.


## Docs 
Here are some docs that I found useful while working on this project:
1. [GFG tf-idf](https://www.geeksforgeeks.org/understanding-tf-idf-term-frequency-inverse-document-frequency/)
2. [medium](https://medium.com/@abhishekjainindore24/tf-idf-in-nlp-term-frequency-inverse-document-frequency-e05b65932f1d)
