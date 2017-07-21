import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re

script = "transcription.txt"

def stripStopwordsPunctuation(transcription):
	transcription = transcription.replace('\u2019', '').replace('\u2026', '')
	lines = transcription.split('\n')
	processed_lines = []
	for sentence in lines:
		sentence = sentence.lower()
		tokenizer = RegexpTokenizer(r'\w+')
		tokens = tokenizer.tokenize(sentence)
		filtered_words = [w for w in tokens if (not w in stopwords.words('english') and not w in ['operator', 'anderson'])]
		processed_lines.append(" ".join(filtered_words))
	return "\n".join(processed_lines)

def stripPeople(transcription):
	transcription = transcription.replace('\u2019', '').replace('\u2026', '')
	lines = transcription.split('\n')
	processed_lines = []
	for sentence in lines:
		tokens = sentence.split()
		filtered_words = [w for w in tokens if not w in ['Operator:', 'Anderson:', 'Im']]
		processed_lines.append(" ".join(filtered_words))
	return "\n".join(processed_lines)

def stripCallerText(transcription):
	transcription = transcription.replace('\u2019', '').replace('\u2026', '')
	transcript_lines = transcription.split('\n')
	caller_lines = [line.split(": ")[1] for line in transcript_lines if "Operator: " not in line]
	return "\n".join(caller_lines)

def stripOperatorText(transcription):
	transcription = transcription.replace('\u2019', '').replace('\u2026', '')
	transcript_lines = transcription.split('\n')
	operator_lines = [line.split(": ")[1] for line in transcript_lines if "Operator: " in line]
	return "\n".join(operator_lines)