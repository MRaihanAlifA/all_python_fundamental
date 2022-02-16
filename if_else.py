print('mom tell her son to buy milk, if they have eggs, buy 6 eggs')
print('son go to store')
milk_count = 0
egg_count = 2
print(f'there are {milk_count} milk and {egg_count} egg')
if milk_count > 0:
    if egg_count > 5:
        print('son buying 1 milk and 6 eggs and go home')
    else:
        print('son buying 1 milk and go home')
else:
    print('store doesnt sell milk then son go to home and tell her mother')
