



filtered_wordsPath = '/home/x8/Desktop/python/show-me-the-code/0012/filtered_words.txt'
words = open(filtered_wordsPath).read().split()

user_input = input("Please Input an sentence:")

for word in words:
    user_input = user_input.replace(word,'*'*len(word))

print(user_input)
