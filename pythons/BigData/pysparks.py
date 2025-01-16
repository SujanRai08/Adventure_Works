# word count using pyspark 
from pyspark import SparkContext
sc = SparkContext('local','WordCount')

text_data = sc.textFile('data.txt')
# Count words
counts = text_data.flatMap(lambda line: line.split(" ")) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda a, b: a + b)

counts.saveAsTextFile('output')
print('word count completed')