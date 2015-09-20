from collections import Counter
from sys import argv
import re, csv

if len(argv) is 3:														# Gets optional limit
	script, filename, limit = argv
else:
	script, filename = argv
	limit = 1000000															# If not set, use 1M for word limit

raw = open(filename).read().lower()						# Open File
convo = re.sub('(?<=\n).*?(?=: ):', "", raw)	# Remove metadata (date, #'s etc)
words = re.findall(r'\w+', convo)							# Select words instead of letters
wordfreq = Counter(words).most_common()				# Count most common words

print 'Words detected: %s' % len(words)
print 'Writing to CSV...'

csvfile = "output.csv"
writer = csv.writer(open(csvfile, 'w'))
writer.writerow(['#', 'Word', 'Count'])

i=0
for word, count in wordfreq:
	i = i+1
	print "%d, %s, %s" % (i, count, word)
	writer.writerow([i, count, word])
	if i == int(limit):
		break

print 'Done! Word count for %s words saved to CSV!' % (i)