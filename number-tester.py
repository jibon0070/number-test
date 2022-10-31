import itertools as tool

chars = ['1', '5', '10']

len = int(input('note number: '))

counter = 1

for i in tool.product(chars, repeat=len):
    counter += 1
    sum = 0
    one = 0
    five = 0
    ten = 0
    for note in i:
        sum += int(note)
        if note == '1':
            one += 1
        elif note == '5':
            five += 1
        else:
            ten += 1
    if sum == 100 and one != 0 and five != 0 and ten != 0:
        print('try #'+str(counter)+', success')
        print('1 = ' + str(one))
        print('5 = ' + str(five))
        print('10 = ' + str(ten))
        break
    print('try #' + str(counter))

if one == 0 or five == 0 or ten == 0:
    print('no result found')