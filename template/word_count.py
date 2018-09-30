import string

def word_count(file_path):
    count = {}  # or dict()
    file = open(file_path)
    #####################
    ## IMPLEMENT HERE! ##
    #####################

test_files = ['gettysburg.txt', 'shark.txt']
for file_name in test_files:
    print('=== Word count for {:s} ==='.format(file_name))
    word_count(file_name)
