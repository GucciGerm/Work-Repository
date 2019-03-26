__author__ = 'Zunyan'

import re
from nltk import stem
from nltk import ngrams
from collections import Counter


class DataProcessor():
    
    

    def __init__(self):
        pass
        
    """    
        Process source:jds.jl.
        The strings are processed by removing punctuations and lowercasing.
        Save the processed strings in a file named "processed_jds". One line represents one processed sentence.
    """
    def process_file(self, source_filepath):
        processed_filepath = 'processed_jds'
        WORD = re.compile(r'\w+\+*')
        porter = stem.porter.PorterStemmer()
        with open(source_filepath, 'r') as source_file:
            with open(processed_filepath, 'w') as processed_file:
                for block in source_file:
                    # identify the end of a sentence (period+blank), remove redundant information, job_description, Responsibilities
                    block = re.sub('\\.\s+|job_description|\\nResponsibilities\\n', '\\n', block)
                    strings = block.split('\\n')
                    for s in strings:
                        if s:
                            tokens = WORD.findall(s.lower())  #lowercase
                            tokens = [porter.stem(token) for token in tokens] #stemming
                            processed_file.write(' '.join(tokens)+'\n')
 
    """                       
    #extract n-grams from the processed file
    def extract_n_grams(self, filepath, n):
        ngram_file_path = 'ngram_file'
        with open(filepath, 'r') as inputfile:
            with open(ngram_file_path, 'w') as outputfile:
                for line in inputfile:
                    tokens = line.split()
                    if len(tokens)>=n:
                        n_grams = ngrams(tokens, n)
                        for n_gram in n_grams:
                            print n_gram
                            outputfile.write(' '.join(n_gram))
                            outputfile.write('\n')
    
    #extract n-grams from the processed file
    def extract_n_grams1(self, filepath, n):
        ngram_file_path = 'ngram_file2'
        ngram_dict = {}
        with open(filepath, 'r') as inputfile:
            for line in inputfile:
                tokens = line.split()
                if len(tokens)>=n:
                    n_grams = ngrams(tokens, n)
                    for n_gram in n_grams:
                        ngram_dict[n_gram] = ngram_dict.get(n_gram, 0) + 1
                        
        return ngram_dict
                            
    """


if __name__ == '__main__':
    test = DataProcessor()
    test.process_file("jds.jl")
    #test.extract_n_grams("processed_jds", 4)
