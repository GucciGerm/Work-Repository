
"""
    Calculates the frequency of n-grams from "processed_jds" file
    
    Result is saved in a file named "ngram_frequency"

"""


from pyspark import SparkConf, SparkContext

from operator import add
import sys
import glob

## Constants
APP_NAME = "ngram_frequency"

    

def main(sc,file_name, threshold, n_for_ngram):
    temp_result = 'temp_result'
    
    # extract n-grams and count the frequency
    textRDD = sc.textFile(file_name)
    ngrams = textRDD.flatMap(lambda line: zip(*[line.split()[i:] for i in range(n_for_ngram)]))
    ngramCounts = ngrams.map(lambda ngram: (ngram, 1)).reduceByKey(lambda v1,v2:v1 +v2)
    
    # filter out the n-grams with frequency larger than the threshold
    filtered = ngramCounts.filter(lambda pair:pair[1] >= threshold)
    
    #save the result in the temp_result folder
    filtered.saveAsTextFile(temp_result)
    
    # read files in the temp_result folder and collect the data in "ngram_frequency" file.
    with open('ngram_frequency', 'w') as result_file:
        for one_file in glob.glob('result/*'):
            print str(one_file)
            with open(one_file, 'r') as input_file:
                for line in input_file:
                    result_file.write(line)
            

if __name__ == "__main__":

    # create Spark context with Spark configuration
    conf = SparkConf().setAppName(APP_NAME)
    conf = conf.setMaster("local[*]")
    sc   = SparkContext(conf=conf)
    
    #~/spark-2.0.1-bin-hadoop2.7/bin/spark-submit /home/zunyan/Python/iDatalabs/final/ngram_counter.py processed_jds 20 4
    
    # filename: the processed file to extract n-grams
    filename = sys.argv[1]
    # threshold: the threshold of minimum frequency of n-grams
    threshold = int(sys.argv[2])
    #n_for_ngram: the number n for n-gram
    n_for_ngram = int(sys.argv[3])
    
    # get n-grams with frequency
    main(sc, filename, threshold, n_for_ngram)
    
    
