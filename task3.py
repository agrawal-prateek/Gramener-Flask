if __name__ == '__main__':
    L1, L2 = ['a', 'b', 'c'], ['b', 'd']
    print('Common Elements in L1 and L2 =', set(L1).intersection(L2))
    print('Present in L1 but not in L2 =', set(L1) - set(L2))
