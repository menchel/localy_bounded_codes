from itertools import product

def check_if_word_is_locally_bounded(n,word, l, delta):
    'iterate over all the windows'
    for i in range(n - l + 1):
        window = word[i:i+l]
        'check the current window'
        if sum(window) > l // 2 - delta:
            return False
    return True

def count_amount_of_n_l_delta_locally_bounded_codes(n, l, delta):
    vectors_counter = 0
    'iterate over all possible n sized vectors'
    for word in product([0, 1], repeat=n):
        if check_if_word_is_locally_bounded(n,word, l, delta):
            vectors_counter += 1
    return vectors_counter

if __name__ == '__main__':
    print("enter vector size n")
    n = int(input())
    print("enter window size")
    l = int(input())
    if l>n:
        print("invalid window size")
        exit()
    print("enter delta")
    delta = int(input())
    if l//2-delta < 0:
        print("invalid delta")
        exit()
    print("number of {n} sized vectors that are ({l},{delta}) bounded is {answer}".format(n=n, l=l, delta=delta,answer=count_amount_of_n_l_delta_locally_bounded_codes(n, l, delta)))

