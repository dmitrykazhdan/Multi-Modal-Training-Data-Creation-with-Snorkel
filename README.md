# Multi Modal Training Data Creation with Snorkel

This project explores ways in which Snorkel may be combined with non-textual datasets and unsupervised clustering approaches.


# Relevant Resources

The Snorkel repository can be found here: https://github.com/HazyResearch/snorkel

The relevant model files and dataset can be found here: https://github.com/husseinmouzannar/multimodal-deep-learning-for-disaster-response

The image-clustering repository can be found here: https://github.com/elcorto/imagecluster

The latter two APIs will not work directly out-of-the-box, and have to be manually adjusted (e.g. by setting appropriate filepaths, parameter values etc.).


# Files

partition_data.py - contains code that partitions the multi-modal dataset, creating the appropriate directory structure and extracting training, testing and validation sample subsets.

execute_models.py - trains all of the relevant models one after the other in a sequential fashion

generate_performance_metrics.py - contains code for processing the confusion matrices and computing the Precision, Recall and F1-Score
