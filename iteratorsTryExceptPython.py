lst = {3,6,4,9,8,7,5,1}

itr = iter(lst)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break
    