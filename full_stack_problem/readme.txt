In the data folder, you will find a file jds.jl. This file contains around 96000 job descriptions obtained from multiple sources. Given this data, write an API that that does the following:

1. Write a function that returns the common n-grams in which a given word or phrase occurs - the number of words to consider for the n-gram should be a parameter, as should the minimum count threshold below which n-grams are not returned.
2. Build a web-app on top of this that utilizes the function and draws a word cloud of most common n-grams.

