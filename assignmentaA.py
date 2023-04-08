def pairs(arr,sum):
    
    num_dict = {}
    Pairs = []

    for i in range(len(arr)):
        diff = sum - arr[i]
        if diff in num_dict:
            Pairs.append((diff, arr[i]))
        num_dict[arr[i]] = i
    return Pairs

arr = [1, 2, 3, 4, 5]
sum = 6
pairs = pairs(arr, sum)
print(pairs)
