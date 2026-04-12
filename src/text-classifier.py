"""The complete Problem Set 5. Building a text classifier using pure probability and dictionaries—no machine learning libraries allowed."""

import os
import math
from collections import defaultdict

class ScratchNaiveBayes:
    def __init__(self):
        self.vocab = set()
        self.word_counts = {'spam': defaultdict(int), 'ham': defaultdict(int)}
        self.class_counts = {'spam': 0, 'ham': 0}
        self.priors = {}

    def tokenize(self, text: str) -> list:
        """Converts text to lowercase and splits into words."""
        return ''.join([c.lower() if c.isalnum() or c.isspace() else ' ' for c in text]).split()

    def fit(self, X_train: list, y_train: list):
        """Calculates word frequencies and class priors based on training data."""
        total_docs = len(y_train)
        
        for text, label in zip(X_train, y_train):
            self.class_counts[label] += 1
            words = self.tokenize(text)
            
            for word in words:
                self.word_counts[label][word] += 1
                self.vocab.add(word)
                
        # Calculate prior probabilities P(Spam) and P(Ham)
        self.priors['spam'] = self.class_counts['spam'] / total_docs
        self.priors['ham'] = self.class_counts['ham'] / total_docs

    def predict(self, text: str) -> str:
        """Predicts the class of a new text using Bayes' Theorem with Laplace smoothing."""
        words = self.tokenize(text)
        scores = {'spam': math.log(self.priors['spam']), 'ham': math.log(self.priors['ham'])}
        
        vocab_size = len(self.vocab)
        
        for label in ['spam', 'ham']:
            total_words_in_class = sum(self.word_counts[label].values())
            
            for word in words:
                # Laplace (+1) Smoothing to handle words we haven't seen before
                word_count = self.word_counts[label].get(word, 0) + 1
                denominator = total_words_in_class + vocab_size
                
                # Using log probabilities to prevent floating point underflow
                scores[label] += math.log(word_count / denominator)
                
        return 'spam' if scores['spam'] > scores['ham'] else 'ham'

if __name__ == "__main__":
    # Mock training data
    train_emails = [
        "Win money now, free cash!",
        "Hey Bob, are we still on for lunch?",
        "Click here for a free prize",
        "Please review the attached project documentation."
    ]
    train_labels = ['spam', 'ham', 'spam', 'ham']
    
    # Initialize and train
    nb = ScratchNaiveBayes()
    nb.fit(train_emails, train_labels)
    
    # Test on unseen data
    test_email = "Get your free cash prize today by clicking here!"
    prediction = nb.predict(test_email)
    
    print(f"Email: '{test_email}'")
    print(f"Prediction: {prediction.upper()}")
