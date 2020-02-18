# Basics of ML

# Table of Contents
1. [Types of ML Problems](#types-of-ml-problems)
2. [Measuring Success and Visualization](#measuring-success)
    1. [How to measure success](#how-do-we-measure-the-success-of-our-ml-problems)
    2. [When to use them](#why-and-when-would-we-use-each)
    3. [visualization of success of models](#visualization)
    
## Types of ML problems
- Here we are usually looking at 2 types:
    - Supervised
        - Regression
        - Classification
    - Unsupervised
        - Clustering
        - Neural Networks
        - Principle Component Analysis

## Measuring success
### How do we measure the success of our ML problems?
There are 3 main ways to do this:

| Accuracy | Precision | Recall | F1 |
| --- | --- | --- | --- |
| (TP + TN)  | (TP) | (TP) | 2 * precision * recall |
| / | / | / | / |
| (TP + TN + FP + FN) |  (TP + FP) | (TP + FN) | precision + recall |

where:
- TP: True Positive
- FP: False Positive
- TN: True Negative
- FN: False Negative

### why and when would we use each?
- Accuracy: 
    - Quick and dirty, only interested in model predicting 
    as close to actual data as possible
- Precision:
    - Used when the cost of a false positive is high
    - Aim is to reduce number of false positives, since formula focuses
    on number of total positives as the denominator.
    - This means that the negatives are not as important 
    to the problem at hand
    - Such examples include classification of **spam**, which
    would be detrimental if it had high number of false positives 
    since the user could be losing important emails.
- Recall:
    - Used to reduce the number of false negatives
    - This means that the number of false positives are not as important
    - Examples include **Fraud detection** or **Sick patient detection**
    since a false negative would allow a fraud or sick patient through, 
    which would be more undesirable than falsely flagging out something
    as fraud or a wrongly classifying someone as sick.
- F1:
    - Used as a balance between precision and recall.
    - This metric punishes the extremes, such that large numbers
    of False Positives and/or False Negatives are penalized.
    - This would thus be ideal for datasets which have a large number of 
    True Negatives and would be a good metric for realistic
    datasets since it is expected that the ratio of positives and negatives
    in a real dataset would not be similar or ideal.
    
    
### Visualization:
- For a better visualization of the above,
we can use a confusion matrix

| Actual / Predicted | *Positive* | *Negative* |
| --- | --- | --- |
| *Positive* | True Positive | False Positive | 
| *Negative* | False Negative | True Negative |

This also works for multi-class classification problems 
since "Positive" and "Negative" can be treated as class labels
and be replaced with any arbitary label such as "dogs", "cats", etc.
