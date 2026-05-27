#!/usr/bin/env python3
import argparse
import sys
import json
VERSION = "1.0.0"

def extractive_summarize(text, num_sentences=3):
    sentences = text.split('. ')
    if len(sentences) <= num_sentences:
        return text
    step = len(sentences) // num_sentences
    summary = '. '.join(sentences[i] for i in range(0, len(sentences), step)[:num_sentences])
    return summary + '.' if not summary.endswith('.') else summary

def main():
    parser = argparse.ArgumentParser(description='Quick Summarize - Intelligent text summarization')
    parser.add_argument('input', nargs='?', help='Input text or file path')
    parser.add_argument('-f', '--file', help='Read from file')
    parser.add_argument('-n', '--num', type=int, default=3, help='Number of sentences')
    parser.add_argument('--json', action='store_true', help='JSON output')
    args = parser.parse_args()
    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.input:
        text = args.input
    else:
        text = sys.stdin.read()
    if not text.strip():
        parser.error("No input text provided")
    summary = extractive_summarize(text, args.num)
    if args.json:
        print(json.dumps({"summary": summary, "length": len(summary)}))
    else:
        print(summary)
if __name__ == '__main__':
    main()
