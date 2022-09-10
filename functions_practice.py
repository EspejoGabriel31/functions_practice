def hello():
    print('Hello User!')

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(li):
    first = True
    if len(li) == 0:
        print('My lunchbox is empty!')
    else:
        for x in li:
            if(first):
                first = False
                print('First I eat ', x)
            else:
                print('Next I eat ', x)

hello()

print(pack('m','r','i'))

eat_lunch(['apple','pear', 'grape'])