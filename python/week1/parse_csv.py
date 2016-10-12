import csv

with open ('/Users/alfredgarcia/codingdojo/web_fundamentals/python/week1/us-500.csv', 'rU') as f:
    reader = csv.reader(f)
    keys = reader.next()
    for data in reader:
        print "{} {}".format(data[0], data[1])
        for idx in range(len(keys)):
            print "{} {}".format(keys[idx], data[idx])
        print "\n _ _ _ _ _ _ _ _ _ _"
