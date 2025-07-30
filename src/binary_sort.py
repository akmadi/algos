# Binary search program 

def binary_search(list_test:list,item:int):
    low = 0
    high = len(list_test) - 1
    while low <= high:
        mid = low + high
        guess = list_test[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

if __name__ == "__main__":
    print(binary_search(sorted([6,1,3,2,5,4]),4))