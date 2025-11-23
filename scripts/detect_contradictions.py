#!/usr/bin/env python3
"""
AI-powered contradiction and duplicate detector for The Vibe Coders repo
Uses embeddings to find semantic similarities and potential conflicts
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Tuple, Dict
import hashlib

# Simple embedding using TF-IDF (no external dependencies needed)
from collections import Counter
import math

class SimpleSemanticAnalyzer:
    """Lightweight semantic analyzer using TF-IDF"""

    def __init__(self):
        self.documents = []
        self.file_paths = []
        self.vocabulary = set()
        self.idf_scores = {}

    def load_markdown_files(self, repo_path: str):
        """Load all markdown files from the repository"""
        for root, dirs, files in os.walk(repo_path):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            for file in files:
                if file.endswith('.md'):
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            # Split into meaningful chunks (paragraphs)
                            chunks = [c.strip() for c in content.split('\n\n') if len(c.strip()) > 50]
                            for chunk in chunks:
                                self.documents.append(chunk.lower())
                                self.file_paths.append(path)
                                # Build vocabulary
                                words = chunk.lower().split()
                                self.vocabulary.update(words)
                    except Exception as e:
                        print(f"Error reading {path}: {e}")

        # Calculate IDF scores
        self._calculate_idf()

    def _calculate_idf(self):
        """Calculate IDF scores for all words"""
        total_docs = len(self.documents)
        word_doc_count = Counter()

        for doc in self.documents:
            unique_words = set(doc.split())
            for word in unique_words:
                word_doc_count[word] += 1

        for word, count in word_doc_count.items():
            self.idf_scores[word] = math.log(total_docs / count)

    def _get_tfidf_vector(self, text: str) -> Dict[str, float]:
        """Convert text to TF-IDF vector"""
        words = text.lower().split()
        tf = Counter(words)

        # Normalize TF
        max_freq = max(tf.values()) if tf else 1
        tfidf = {}

        for word, freq in tf.items():
            normalized_tf = freq / max_freq
            idf = self.idf_scores.get(word, 0)
            tfidf[word] = normalized_tf * idf

        return tfidf

    def _cosine_similarity(self, vec1: Dict, vec2: Dict) -> float:
        """Calculate cosine similarity between two vectors"""
        # Get all unique words
        all_words = set(vec1.keys()) | set(vec2.keys())

        # Calculate dot product and magnitudes
        dot_product = sum(vec1.get(w, 0) * vec2.get(w, 0) for w in all_words)
        mag1 = math.sqrt(sum(v**2 for v in vec1.values()))
        mag2 = math.sqrt(sum(v**2 for v in vec2.values()))

        if mag1 == 0 or mag2 == 0:
            return 0

        return dot_product / (mag1 * mag2)

    def find_duplicates_and_contradictions(self, similarity_threshold=0.7):
        """Find potential duplicates and contradictions"""
        results = {
            'duplicates': [],
            'potential_contradictions': []
        }

        # Convert all documents to TF-IDF vectors
        vectors = [self._get_tfidf_vector(doc) for doc in self.documents]

        # Compare all document pairs
        for i in range(len(self.documents)):
            for j in range(i + 1, len(self.documents)):
                similarity = self._cosine_similarity(vectors[i], vectors[j])

                if similarity > similarity_threshold:
                    # Check if they're from different files
                    if self.file_paths[i] != self.file_paths[j]:
                        # Potential duplicate
                        results['duplicates'].append({
                            'similarity': round(similarity, 3),
                            'file1': self.file_paths[i],
                            'text1': self.documents[i][:200] + '...',
                            'file2': self.file_paths[j],
                            'text2': self.documents[j][:200] + '...'
                        })

                # Check for contradictions (moderate similarity + negation patterns)
                elif 0.4 < similarity < 0.7:
                    if self._contains_contradiction_patterns(
                        self.documents[i], self.documents[j]
                    ):
                        results['potential_contradictions'].append({
                            'similarity': round(similarity, 3),
                            'file1': self.file_paths[i],
                            'text1': self.documents[i][:200] + '...',
                            'file2': self.file_paths[j],
                            'text2': self.documents[j][:200] + '...'
                        })

        return results

    def _contains_contradiction_patterns(self, text1: str, text2: str) -> bool:
        """Simple heuristic to detect potential contradictions"""
        contradiction_indicators = [
            ('must', 'must not'),
            ('should', 'should not'),
            ('always', 'never'),
            ('required', 'optional'),
            ('yes', 'no'),
            ('true', 'false'),
            ('will', "won't"),
            ('does', "doesn't"),
            ('is', "isn't"),
            ('are', "aren't")
        ]

        for positive, negative in contradiction_indicators:
            if (positive in text1 and negative in text2) or \
               (negative in text1 and positive in text2):
                return True

        return False

    def find_terminology_inconsistencies(self):
        """Find potential terminology inconsistencies"""
        # Common technical term variations
        term_variations = [
            ['component', 'widget', 'element'],
            ['function', 'method', 'procedure'],
            ['property', 'attribute', 'field'],
            ['directory', 'folder'],
            ['repository', 'repo'],
            ['configuration', 'config', 'settings'],
            ['authentication', 'auth'],
            ['authorization', 'authz'],
            ['identifier', 'id'],
            ['application', 'app']
        ]

        inconsistencies = []

        for variations in term_variations:
            files_using_terms = {term: set() for term in variations}

            for doc, path in zip(self.documents, self.file_paths):
                for term in variations:
                    if term in doc:
                        files_using_terms[term].add(path)

            # Check if multiple variations are used
            used_variations = [(term, files) for term, files in files_using_terms.items() if files]
            if len(used_variations) > 1:
                inconsistencies.append({
                    'terms': [term for term, _ in used_variations],
                    'usage': {term: list(files) for term, files in used_variations}
                })

        return inconsistencies

def main():
    """Main entry point"""
    repo_path = '/Users/chocho/projects/thevibecoders-revamped'

    print("🤖 AI-Powered Documentation Analyzer")
    print("=" * 50)

    analyzer = SimpleSemanticAnalyzer()

    print(f"📂 Loading documents from: {repo_path}")
    analyzer.load_markdown_files(repo_path)

    print(f"📊 Loaded {len(analyzer.documents)} text chunks from {len(set(analyzer.file_paths))} files")
    print(f"📚 Vocabulary size: {len(analyzer.vocabulary)} unique words")
    print()

    print("🔍 Analyzing for duplicates and contradictions...")
    results = analyzer.find_duplicates_and_contradictions()

    # Display duplicates
    if results['duplicates']:
        print(f"\n📑 Found {len(results['duplicates'])} potential duplicates:")
        for i, dup in enumerate(results['duplicates'][:5], 1):  # Show top 5
            print(f"\n  {i}. Similarity: {dup['similarity']*100:.1f}%")
            print(f"     File 1: {dup['file1']}")
            print(f"     File 2: {dup['file2']}")
            print(f"     Preview: {dup['text1'][:100]}...")
    else:
        print("\n✅ No significant duplicates found")

    # Display contradictions
    if results['potential_contradictions']:
        print(f"\n⚠️  Found {len(results['potential_contradictions'])} potential contradictions:")
        for i, cont in enumerate(results['potential_contradictions'][:5], 1):
            print(f"\n  {i}. Files: {cont['file1']} vs {cont['file2']}")
            print(f"     Similarity: {cont['similarity']*100:.1f}%")
    else:
        print("\n✅ No potential contradictions detected")

    # Check terminology inconsistencies
    print("\n🔤 Checking for terminology inconsistencies...")
    inconsistencies = analyzer.find_terminology_inconsistencies()

    if inconsistencies:
        print(f"\n📝 Found {len(inconsistencies)} terminology inconsistencies:")
        for inc in inconsistencies:
            print(f"\n  • Mixed usage of: {', '.join(inc['terms'])}")
            for term, files in inc['usage'].items():
                print(f"    - '{term}' used in: {', '.join([Path(f).name for f in files])}")
    else:
        print("\n✅ Terminology is consistent")

    # Save detailed results
    output_file = os.path.join(repo_path, 'contradiction_analysis.json')
    with open(output_file, 'w') as f:
        json.dump({
            'duplicates': results['duplicates'],
            'contradictions': results['potential_contradictions'],
            'terminology_inconsistencies': inconsistencies,
            'statistics': {
                'total_documents': len(analyzer.documents),
                'unique_files': len(set(analyzer.file_paths)),
                'vocabulary_size': len(analyzer.vocabulary)
            }
        }, f, indent=2)

    print(f"\n💾 Detailed results saved to: {output_file}")

if __name__ == "__main__":
    main()