from collections import Counter
from sys import argv
import re, csv
script, filename = argv

csvfile = "wordfreq.csv"

words = re.findall(r'\w+', open(filename).read().lower())
wordfreq = Counter(words).most_common()

print wordfreq

writer = csv.writer(open(csvfile, 'w'))

for word, count in wordfreq:
	print "%s, %s" % (word, count)
	writer.writerow([word, count])