book_list = ['mathematics', 'science', 'chemics', 'english']

print('show all books')

for book in book_list:
    print(book)

print('show all books with len')
for i in range(0, len(book_list)):
    print(book_list[i])

book_list = [12, 'science', 10, 'english']

print('\nshow new book list')

for book in book_list:
    print(book)

book_list = ['mathematics', 'science', 'chemics', 'english']
book_list.append('sociology')

print('\nshow new book list')
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nclear list')
book_list.clear()
print(book_list)

book_list = ['mathematics', 'science', 'chemics', 'english']
print('\nchange first element')
book_list[0] = 'physics'
for i in range(0, len(book_list)):
    print(book_list[i])

print('\npick second element')
new_book = book_list.pop(1)
for i in range(0, len(book_list)):
    print(book_list[i])
print(f'second element = {new_book}')

print('\npop -1')
book_list = ['mathematics', 'science', 'chemics', 'english', 'economy']
book_list.pop(-1)
for i in range(0, len(book_list)):
    print(book_list[i])

print('\ndeleting list using list comprehension')
book_list = ['mathematics', 'science', 'chemics', 'english', 'economy']
del book_list[1]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\ndeleting list using list comprehension with start and end')
book_list = ['mathematics', 'science', 'chemics', 'english', 'economy']
del book_list[0:4]  #start:end
for i in range(0, len(book_list)):
    print(book_list[i])

print('\ndeleting list using list comprehension with start, end and step')
book_list = ['mathematics', 'science', 'chemics', 'english', 'economy']
del book_list[0:5:2]  #start:end:step
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nmaking new list using comprehension')
book_list = ['mathematics', 'science', 'chemics', 'english', 'economy']
new_book_list = book_list[:]
del book_list
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print('\nmaking new list using comprehension')
book_list = ['mathematics', 'science', 'chemics', 'english', 'economy']
new_book_list = book_list[:]
del book_list
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print('\nmaking new list using comprehension: odd only')
book_list = ['mathematics', 'science', 'chemics', 'english', 'economy']
new_book_list = book_list[0::2]
del book_list
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print('\nmaking new list using comprehension: even only')
book_list = ['mathematics', 'science', 'chemics', 'english', 'economy']
new_book_list = book_list[1::2]
del book_list
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print('\nmaking new list using comprehension: odd only without last book')
book_list = ['mathematics', 'science', 'chemics', 'english', 'economy']
new_book_list = book_list[0:-1:2]
del book_list
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

