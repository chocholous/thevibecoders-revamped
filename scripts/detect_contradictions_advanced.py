#!/usr/bin/env python3
"""
Advanced AI-powered contradiction and duplicate detector
Enhanced with NLP capabilities for better semantic analysis
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import List, Tuple, Dict, Set
from collections import Counter, defaultdict
import math
import hashlib

# Try to import advanced NLP libraries
try:
    import nltk
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer
    NLTK_AVAILABLE = True

    # Download required NLTK data
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)
except ImportError:
    NLTK_AVAILABLE = False
    print("⚠️  NLTK not installed. Using basic tokenization. Install with: pip install nltk")

class AdvancedSemanticAnalyzer:
    """Advanced semantic analyzer with NLP enhancements"""

    def __init__(self):
        self.documents = []
        self.file_paths = []
        self.vocabulary = set()
        self.idf_scores = {}
        self.contradictions_found = []
        self.duplicates_found = []

        # NLP components
        if NLTK_AVAILABLE:
            self.stop_words = set(stopwords.words('english'))
            self.stemmer = PorterStemmer()
        else:
            # Basic stop words if NLTK not available
            self.stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on',
                               'at', 'to', 'for', 'of', 'with', 'by', 'from', 'as'}
            self.stemmer = None

        # Semantic patterns for contradiction detection
        self.negation_patterns = [
            (r'\bmust\b', r'\bmust not\b'),
            (r'\bshould\b', r'\bshould not\b'),
            (r'\balways\b', r'\bnever\b'),
            (r'\brequired\b', r'\boptional\b'),
            (r'\bwill\b', r"\bwon't\b"),
            (r'\bdoes\b', r"\bdoesn't\b"),
            (r'\bis\b', r"\bisn't\b"),
            (r'\benable', r'\bdisable'),
            (r'\ballow', r'\bdeny|\bprevent'),
            (r'\bsync', r'\basync'),
            (r'\bclient', r'\bserver'),
            (r'\bpublic\b', r'\bprivate\b'),
        ]

        # Technical terminology standardization rules
        self.term_standardization = {
            'authentication': ['auth', 'authn'],
            'authorization': ['authz'],
            'configuration': ['config', 'cfg'],
            'application': ['app'],
            'repository': ['repo'],
            'directory': ['dir', 'folder'],
            'identifier': ['id'],
            'environment': ['env'],
            'development': ['dev'],
            'production': ['prod'],
            'component': ['comp'],
            'element': ['elem'],
            'property': ['prop'],
            'attribute': ['attr'],
            'function': ['func', 'fn'],
            'documentation': ['docs', 'doc']
        }

    def _tokenize(self, text: str) -> List[str]:
        """Advanced tokenization with NLP"""
        if NLTK_AVAILABLE:
            # Use NLTK tokenization
            tokens = word_tokenize(text.lower())
            # Remove stop words and apply stemming
            tokens = [self.stemmer.stem(t) for t in tokens
                     if t.isalnum() and t not in self.stop_words]
        else:
            # Basic tokenization
            text = re.sub(r'[^\w\s]', ' ', text.lower())
            tokens = [t for t in text.split() if t and t not in self.stop_words]

        return tokens

    def _extract_sentences(self, text: str) -> List[str]:
        """Extract sentences from text"""
        if NLTK_AVAILABLE:
            return sent_tokenize(text)
        else:
            # Basic sentence splitting
            sentences = re.split(r'[.!?]+', text)
            return [s.strip() for s in sentences if s.strip()]

    def load_markdown_files(self, repo_path: str):
        """Load all markdown files with enhanced parsing"""
        for root, dirs, files in os.walk(repo_path):
            # Skip hidden and system directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']

            for file in files:
                if file.endswith('.md'):
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            content = f.read()

                            # Enhanced chunking: by sections and paragraphs
                            sections = self._extract_sections(content)

                            for section in sections:
                                if len(section.strip()) > 50:
                                    self.documents.append(section)
                                    self.file_paths.append(path)

                                    # Build vocabulary with tokenization
                                    tokens = self._tokenize(section)
                                    self.vocabulary.update(tokens)
                    except Exception as e:
                        print(f"Error reading {path}: {e}")

        # Calculate IDF scores
        self._calculate_idf()

    def _extract_sections(self, markdown_content: str) -> List[str]:
        """Extract logical sections from markdown"""
        sections = []

        # Split by headers
        header_pattern = r'^#+\s+.+$'
        lines = markdown_content.split('\n')

        current_section = []
        for line in lines:
            if re.match(header_pattern, line) and current_section:
                # New section starting
                sections.append('\n'.join(current_section))
                current_section = [line]
            else:
                current_section.append(line)

        if current_section:
            sections.append('\n'.join(current_section))

        # Also split by double newlines for paragraphs
        for section in sections[:]:
            if len(section) > 1000:  # Large sections
                paragraphs = section.split('\n\n')
                sections.remove(section)
                sections.extend(p for p in paragraphs if len(p.strip()) > 50)

        return sections

    def _calculate_idf(self):
        """Calculate IDF scores for all tokens"""
        total_docs = len(self.documents)
        if total_docs == 0:
            return

        word_doc_count = Counter()

        for doc in self.documents:
            unique_tokens = set(self._tokenize(doc))
            for token in unique_tokens:
                word_doc_count[token] += 1

        for word, count in word_doc_count.items():
            self.idf_scores[word] = math.log(total_docs / (count + 1))

    def _get_tfidf_vector(self, text: str) -> Dict[str, float]:
        """Convert text to TF-IDF vector with advanced tokenization"""
        tokens = self._tokenize(text)
        tf = Counter(tokens)

        if not tf:
            return {}

        # Normalize TF
        max_freq = max(tf.values())
        tfidf = {}

        for token, freq in tf.items():
            normalized_tf = freq / max_freq
            idf = self.idf_scores.get(token, 0)
            tfidf[token] = normalized_tf * idf

        return tfidf

    def _cosine_similarity(self, vec1: Dict, vec2: Dict) -> float:
        """Calculate cosine similarity between vectors"""
        all_tokens = set(vec1.keys()) | set(vec2.keys())

        dot_product = sum(vec1.get(t, 0) * vec2.get(t, 0) for t in all_tokens)
        mag1 = math.sqrt(sum(v**2 for v in vec1.values()))
        mag2 = math.sqrt(sum(v**2 for v in vec2.values()))

        if mag1 == 0 or mag2 == 0:
            return 0

        return dot_product / (mag1 * mag2)

    def detect_semantic_contradictions(self) -> List[Dict]:
        """Advanced contradiction detection using semantic patterns"""
        contradictions = []

        for i in range(len(self.documents)):
            doc1_sentences = self._extract_sentences(self.documents[i])

            for j in range(i + 1, len(self.documents)):
                doc2_sentences = self._extract_sentences(self.documents[j])

                # Compare sentences for contradictions
                for sent1 in doc1_sentences:
                    for sent2 in doc2_sentences:
                        if self._are_contradictory(sent1, sent2):
                            contradictions.append({
                                'file1': self.file_paths[i],
                                'text1': sent1[:200],
                                'file2': self.file_paths[j],
                                'text2': sent2[:200],
                                'type': 'semantic_opposition'
                            })

        return contradictions

    def _are_contradictory(self, sent1: str, sent2: str) -> bool:
        """Check if two sentences are contradictory"""
        sent1_lower = sent1.lower()
        sent2_lower = sent2.lower()

        # Check for negation patterns
        for positive_pattern, negative_pattern in self.negation_patterns:
            if (re.search(positive_pattern, sent1_lower) and re.search(negative_pattern, sent2_lower)) or \
               (re.search(negative_pattern, sent1_lower) and re.search(positive_pattern, sent2_lower)):
                return True

        # Check for conflicting values
        number_pattern = r'\d+(\.\d+)?'
        nums1 = re.findall(number_pattern, sent1)
        nums2 = re.findall(number_pattern, sent2)

        if nums1 and nums2 and nums1 != nums2:
            # Check if talking about same thing
            tokens1 = set(self._tokenize(sent1))
            tokens2 = set(self._tokenize(sent2))
            overlap = len(tokens1 & tokens2) / min(len(tokens1), len(tokens2))
            if overlap > 0.5:  # High token overlap but different numbers
                return True

        return False

    def find_duplicates_and_contradictions(self, similarity_threshold=0.75):
        """Find duplicates and contradictions with improved accuracy"""
        results = {
            'duplicates': [],
            'contradictions': [],
            'semantic_contradictions': []
        }

        # Convert documents to TF-IDF vectors
        vectors = [self._get_tfidf_vector(doc) for doc in self.documents]

        # Find duplicates and contradictions
        for i in range(len(self.documents)):
            for j in range(i + 1, len(self.documents)):
                if not vectors[i] or not vectors[j]:
                    continue

                similarity = self._cosine_similarity(vectors[i], vectors[j])

                # Skip if same file
                if self.file_paths[i] == self.file_paths[j]:
                    continue

                if similarity > similarity_threshold:
                    # High similarity = likely duplicate
                    results['duplicates'].append({
                        'similarity': round(similarity, 3),
                        'file1': self.file_paths[i],
                        'text1': self.documents[i][:300] + '...',
                        'file2': self.file_paths[j],
                        'text2': self.documents[j][:300] + '...'
                    })
                elif 0.3 < similarity < 0.7:
                    # Moderate similarity - check for contradictions
                    if self._are_contradictory(self.documents[i], self.documents[j]):
                        results['contradictions'].append({
                            'similarity': round(similarity, 3),
                            'file1': self.file_paths[i],
                            'text1': self.documents[i][:300] + '...',
                            'file2': self.file_paths[j],
                            'text2': self.documents[j][:300] + '...'
                        })

        # Advanced semantic contradiction detection
        results['semantic_contradictions'] = self.detect_semantic_contradictions()

        return results

    def find_terminology_issues(self) -> Dict:
        """Find and suggest fixes for terminology inconsistencies"""
        issues = {
            'inconsistencies': [],
            'suggested_fixes': {}
        }

        # Analyze usage of each term group
        for standard_term, variations in self.term_standardization.items():
            all_terms = [standard_term] + variations
            term_usage = defaultdict(set)
            term_counts = defaultdict(int)

            for doc, path in zip(self.documents, self.file_paths):
                doc_lower = doc.lower()
                for term in all_terms:
                    # Use word boundaries for accurate matching
                    pattern = r'\b' + re.escape(term) + r'\b'
                    if re.search(pattern, doc_lower):
                        term_usage[term].add(path)
                        term_counts[term] += len(re.findall(pattern, doc_lower))

            # If multiple variations are used, it's an inconsistency
            used_terms = [term for term, files in term_usage.items() if files]
            if len(used_terms) > 1:
                issues['inconsistencies'].append({
                    'standard_term': standard_term,
                    'variations_found': used_terms,
                    'usage': {term: {
                        'files': list(term_usage[term]),
                        'count': term_counts[term]
                    } for term in used_terms}
                })

                # Suggest the most common term or the standard term
                most_common = max(used_terms, key=lambda t: term_counts[t])
                issues['suggested_fixes'][standard_term] = {
                    'replace_all': used_terms,
                    'with': standard_term if term_counts[standard_term] > 0 else most_common,
                    'files_affected': list(set().union(*[term_usage[t] for t in used_terms]))
                }

        return issues

    def generate_fix_script(self, fixes: Dict) -> str:
        """Generate a Python script to fix terminology inconsistencies"""
        script = """#!/usr/bin/env python3
# Auto-generated script to fix terminology inconsistencies

import os
import re

def fix_terminology(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for old_term, new_term in replacements:
        # Case-insensitive replacement preserving original case
        pattern = r'\\b' + re.escape(old_term) + r'\\b'
        content = re.sub(pattern, new_term, content, flags=re.IGNORECASE)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Terminology fixes
replacements = {
"""
        for standard, fix_info in fixes.items():
            terms_to_replace = [t for t in fix_info['replace_all'] if t != fix_info['with']]
            if terms_to_replace:
                script += f"    '{standard}': [\n"
                for term in terms_to_replace:
                    script += f"        ('{term}', '{fix_info['with']}'),\n"
                script += "    ],\n"

        script += """
}

# Apply fixes
files_to_fix = [
"""
        all_files = set()
        for fix_info in fixes.values():
            all_files.update(fix_info['files_affected'])

        for file_path in sorted(all_files):
            script += f"    '{file_path}',\n"

        script += """
]

fixed_count = 0
for file_path in files_to_fix:
    all_replacements = []
    for term_group in replacements.values():
        all_replacements.extend(term_group)

    if fix_terminology(file_path, all_replacements):
        print(f"✓ Fixed: {file_path}")
        fixed_count += 1

print(f"\\n✅ Fixed {fixed_count} files")
"""
        return script


def main():
    """Main entry point"""
    repo_path = '/Users/chocho/projects/thevibecoders-revamped'

    print("🤖 Advanced AI-Powered Documentation Analyzer")
    print("=" * 60)

    analyzer = AdvancedSemanticAnalyzer()

    print(f"📂 Loading documents from: {repo_path}")
    analyzer.load_markdown_files(repo_path)

    if not analyzer.documents:
        print("❌ No markdown files found!")
        return 1

    print(f"📊 Loaded {len(analyzer.documents)} text chunks from {len(set(analyzer.file_paths))} files")
    print(f"📚 Vocabulary size: {len(analyzer.vocabulary)} unique tokens")
    print(f"🔧 NLP Features: {'Enabled' if NLTK_AVAILABLE else 'Basic mode (install nltk for better results)'}")
    print()

    # Find duplicates and contradictions
    print("🔍 Analyzing for duplicates and contradictions...")
    results = analyzer.find_duplicates_and_contradictions()

    # Display results
    if results['duplicates']:
        print(f"\n📑 Found {len(results['duplicates'])} potential duplicates:")
        for i, dup in enumerate(results['duplicates'][:5], 1):
            print(f"\n  {i}. Similarity: {dup['similarity']*100:.1f}%")
            print(f"     File 1: {Path(dup['file1']).name}")
            print(f"     File 2: {Path(dup['file2']).name}")
    else:
        print("\n✅ No significant duplicates found")

    if results['contradictions'] or results['semantic_contradictions']:
        total_contradictions = len(results['contradictions']) + len(results['semantic_contradictions'])
        print(f"\n⚠️  Found {total_contradictions} potential contradictions:")

        all_contradictions = results['contradictions'] + results['semantic_contradictions']
        for i, cont in enumerate(all_contradictions[:5], 1):
            print(f"\n  {i}. Type: {cont.get('type', 'pattern-based')}")
            print(f"     File 1: {Path(cont['file1']).name}: {cont['text1'][:100]}...")
            print(f"     File 2: {Path(cont['file2']).name}: {cont['text2'][:100]}...")
    else:
        print("\n✅ No contradictions detected")

    # Check terminology
    print("\n🔤 Analyzing terminology consistency...")
    terminology_issues = analyzer.find_terminology_issues()

    if terminology_issues['inconsistencies']:
        print(f"\n📝 Found {len(terminology_issues['inconsistencies'])} terminology inconsistencies:")
        for issue in terminology_issues['inconsistencies']:
            print(f"\n  • Standard: '{issue['standard_term']}'")
            print(f"    Variations found: {', '.join(issue['variations_found'])}")
            for term, info in issue['usage'].items():
                print(f"    - '{term}': {info['count']} occurrences in {len(info['files'])} files")

        # Generate fix script
        if terminology_issues['suggested_fixes']:
            fix_script = analyzer.generate_fix_script(terminology_issues['suggested_fixes'])
            fix_script_path = os.path.join(repo_path, 'scripts', 'fix_terminology.py')
            with open(fix_script_path, 'w') as f:
                f.write(fix_script)
            print(f"\n💡 Fix script generated: {fix_script_path}")
            print("   Run it with: python scripts/fix_terminology.py")
    else:
        print("\n✅ Terminology is consistent")

    # Save detailed results
    output_file = os.path.join(repo_path, 'contradiction_analysis.json')
    with open(output_file, 'w') as f:
        json.dump({
            'duplicates': results['duplicates'],
            'contradictions': results['contradictions'],
            'semantic_contradictions': results['semantic_contradictions'],
            'terminology_issues': terminology_issues,
            'statistics': {
                'total_documents': len(analyzer.documents),
                'unique_files': len(set(analyzer.file_paths)),
                'vocabulary_size': len(analyzer.vocabulary),
                'nlp_enabled': NLTK_AVAILABLE
            }
        }, f, indent=2)

    print(f"\n💾 Detailed results saved to: {output_file}")
    print("\n✨ Analysis complete!")

    return 0

if __name__ == "__main__":
    sys.exit(main())