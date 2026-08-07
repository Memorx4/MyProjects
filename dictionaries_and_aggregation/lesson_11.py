names = ["Alex", "Alex", "Charl", "Alex", "Max", "Charl", "Max", "Mari"]
word_count = {}
for word in names:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)