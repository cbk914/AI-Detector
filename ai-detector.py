import os
import sys
import docx
import PyPDF2
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob
from colorama import Fore, Style
import argparse

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_pdf(file_path):
    text = ''
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

def read_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def analyze_text_basic(text):
    # Tokenize text into words and sentences
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Calculate basic metrics
    word_count = len(words)
    sentence_count = len(sentences)
    vocabulary = set(words)
    vocabulary_size = len(vocabulary)

    # Scoring (simplified for basic analysis)
    score = 0
    score += (word_count > 100) * 10  # Example: higher score for longer texts
    score += (sentence_count > 5) * 10  # Example: higher score for more sentences
    score += (vocabulary_size > 50) * 10  # Example: higher score for larger vocabulary

    # Convert score to probability
    probability = min(100, score)  # Cap the probability at 100%
    return probability

def analyze_text_advanced(text):
    # Tokenize and remove stopwords
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

    # Sentiment Analysis
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # Complexity Analysis (using POS tagging)
    pos_tags = nltk.pos_tag(words)
    num_nouns = sum(1 for word, tag in pos_tags if tag.startswith('NN'))
    noun_ratio = num_nouns / len(words) if words else 0

    # Coherence (based on sentence complexity)
    avg_sentence_length = sum(len(sent.split()) for sent in sentences) / len(sentences) if sentences else 0

    # Scoring
    score = 0
    score += (sentiment > 0.1 or sentiment < -0.1) * 30  # Arbitrary sentiment threshold
    score += (noun_ratio < 0.2) * 30  # Low noun ratio
    score += (avg_sentence_length < 10 or avg_sentence_length > 20) * 40  # Unusual sentence length

    # Convert score to probability
    probability = min(100, score)  # Cap the probability at 100%
    return probability

def determine_authorship(file_path, analysis_type='basic'):
    if not os.path.exists(file_path):
        return Fore.RED + "File not found" + Style.RESET_ALL

    _, file_extension = os.path.splitext(file_path)

    try:
        if file_extension == '.txt':
            text = read_txt(file_path)
        elif file_extension == '.pdf':
            text = read_pdf(file_path)
        elif file_extension == '.docx':
            text = read_docx(file_path)
        else:
            return Fore.RED + "Unsupported file format" + Style.RESET_ALL

        if analysis_type == 'basic':
            probability = analyze_text_basic(text)
        elif analysis_type == 'advanced':
            probability = analyze_text_advanced(text)
        else:
            return Fore.RED + "Invalid analysis type" + Style.RESET_ALL

        return f"{Fore.BLUE}{probability}%{Style.RESET_ALL} chance of being written by a bot"

    except Exception as e:
        return Fore.RED + f"Error processing file: {e}" + Style.RESET_ALL

# Example usage
file_path = 'example.txt'  # Replace with your file path
result = determine_authorship(file_path)
print(f"The analysis of '{file_path}' indicates a {result}")

def main():
    parser = argparse.ArgumentParser(
        description="AI Text Detector - Determines if a text file was written by a human or a bot."
    )

    parser.add_argument('-f', '--file', type=str, help='Path to the file to be analyzed')
    parser.add_argument('-t', '--type', type=str, choices=['basic', 'advanced'], default='basic',
                        help='Type of analysis: "basic" or "advanced"')

    # Check if no arguments were provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if not args.file:
        print(Fore.RED + "No file path provided" + Style.RESET_ALL)
        sys.exit(1)

    result = determine_authorship(args.file, args.type)
    print(f"The analysis of '{args.file}' indicates: {result}")

if __name__ == "__main__":
    main()
