
book_count = 100

print('Mom tell me to read all the books')

book_read_count = 0

"""
for book_read_count in range (1 , book_count+1):
    print(f'{book_read_count} book is being read')
    book_read_count += 1
"""
while book_read_count < book_count:
    book_read_count += 1
    print(f'{book_read_count} book is being read')

print(' ')
print(f'{book_read_count}')
