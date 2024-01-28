# utils.py
import re
import nltk
import os

nltk.download("punkt")

def clean_and_tokenize(text):
    if text is None:
        return []  # Return an empty list for None input

    # Remove extra whitespaces and perform various cleaning tasks
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\b(?:http|ftp)s?://\S+', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()

    # Tokenize the cleaned text
    return nltk.word_tokenize(text)

def format_documents(documents):
    numbered_docs = "\n".join([f"{i+1}. {os.path.basename(doc.metadata['source'])}: {doc.page_content}" for i, doc in enumerate(documents)])
    return numbered_docs

def format_user_question(question):
    if question is None:
        return None
    # Remove extra whitespaces and strip leading/trailing spaces
    question = re.sub(r'\s+', ' ', question).strip()
    return question
