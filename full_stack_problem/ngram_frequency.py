import glob

# read files from 'temp_result' folder and combine the data in "ngram_frequency" file.
with open('ngram_frequency', 'w') as result_file:
        for onefile in glob.glob('temp_result/*'):
            print str(onefile)
            with open(onefile, 'r') as input_file:
                for line in input_file:
                    result_file.write(line)
