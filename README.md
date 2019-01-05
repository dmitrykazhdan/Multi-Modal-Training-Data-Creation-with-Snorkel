# Multi Modal Training Data Creation with Snorkel

This project explores ways in which Snorkel may be combined with non-textual datasets and unsupervised clustering approaches.

# Report

The original report can be found in TBC


# Relevant Resources

The Snorkel repository can be found here: https://github.com/HazyResearch/snorkel

The relevant model files and dataset can be found here: https://github.com/husseinmouzannar/multimodal-deep-learning-for-disaster-response

The image-clustering repository can be found here: https://github.com/elcorto/imagecluster

Note: The latter two APIs will not work directly out-of-the-box, and have to be manually adjusted (e.g. by setting appropriate filepaths, parameter values etc.).


# Files

partition_data.py - contains code that partitions the multi-modal dataset, creating the appropriate directory structure and extracting training, testing and validation sample subsets.

snorkelLabelGeneration.ipynb - Notebook, outlining how Snorkel may be used to generate data labels using both text and image modalities. Note that this notebook has to be run from the Snorkel environment (see https://github.com/HazyResearch/snorkel#quick-start) for more info.

execute_models.py - trains all of the relevant models one after the other in a sequential fashion.

generate_performance_metrics.py - contains code for processing the confusion matrices and computing the Precision, Recall and F1-Score.

# Workflow

The anticipated sequence of steps is as follows:
  1) Download and setup the multi-modal models and dataset
  2) Pre-process the dataset using 'partition_data.py'
  3) Generate labels using 'snorkelLabelGeneration.ipynb' and image-clustering
  4) Train and test the models on the generated dataset using 'execute_models.py'
  5) Investigate performance using 'generate_performance_metrics.py'
