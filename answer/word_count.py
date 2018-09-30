import string

def word_count(file_path):
    count = {}  # or dict()
    file = open(file_path)
    for line in file:
        for word in line.split():
            word = word.lower() # case insensitive
            word = word.strip(string.punctuation) # remove punctuation
            '''
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
            '''
            # with try-except pattern
            try:
                count[word] += 1
            except(KeyError):
                count[word] = 1
            '''
            # with get method
            count[word] = count.get(word, 0) + 1
            '''
    for word, num in count.items():
        print('{:12s}: {:>2d} {:s}'.format(word, num, 'time' if num == 1 else 'times'))

test_files = ['gettysburg.txt', 'shark.txt']
for file_name in test_files:
    print('=== Word count for {:s} ==='.format(file_name))
    word_count('../' + file_name)
