print('A B C | F')
for A in range(2):
    for B in range(2):
        for C in range(2):
            print(f'{A} {B} {C} | {int(not ( not ( not A or not B or not C) or A or not C ) or B)}')