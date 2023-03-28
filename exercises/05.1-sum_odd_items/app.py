arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_odds():
    sum_odd = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            print(arr[i])
            sum_odd += arr[i]
    print(sum_odd)

sum_odds()