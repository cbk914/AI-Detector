# AI-Detector

This Python script, "AI Text Detector," is designed to analyze text documents to determine the likelihood of them being written by a human or an AI (bot). It utilizes Natural Language Processing (NLP) techniques through the NLTK library and offers two modes of analysis: basic and advanced. The script supports analysis of text files (.txt), PDFs (.pdf), and Word documents (.docx).

NLTK Data Packages
The script automatically downloads the following NLTK data packages, essential for text analysis:

punkt: Used for sentence tokenization, dividing text into a list of sentences.

stopwords: Contains lists of common words (like "the", "is", "in") for various languages, which are usually filtered out in text analysis.

averaged_perceptron_tagger: Facilitates part-of-speech tagging, identifying words in a sentence as nouns, verbs, adjectives, etc.

# Installation Guide

+ Python Installation: Ensure Python (version 3.x) is installed on your system. Download it from the official Python website.

+ Library Installation: Install the required Python libraries using pip. Run the following command in your command line interface:

    pip install -r requirements.txt

Script Setup: Download or clone the script into your desired directory.

# Usage Guide

Run the script using Python from the command line, specifying the file for analysis and the type of analysis (basic or advanced) through command-line arguments.

    python3 ai-detector.py -f <path-to-your-text-file> -t <type-of-analysis>
    
    <path-to-your-text-file>: Replace this with the path to the text file you wish to analyze.
    <type-of-analysis>: Can be either basic or advanced. Defaults to basic if not specified.

# Disclaimer 

This script is intended for educational and informational purposes only. It provides a basic tool for text analysis, and while it strives for accuracy, results are not guaranteed. The script's effectiveness varies based on the text's nature and the parameters used for analysis. It should not replace professional judgment or more sophisticated text analysis methods. Results should be verified and interpreted with caution. The script is not responsible for any consequences resulting from its use.
