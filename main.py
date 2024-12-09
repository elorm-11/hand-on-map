numbers1 = [1,2,3,13,14,15,16,17,18]
numbers2 = [4,5,6,7,8,9,10,11,12]
result = map(lambda x,y: x + y, numbers1, numbers2)
print(list(result))

nums = [1,2,3,4,5]
def sq(n):
    return n*n 
square = list(map(sq, nums))
print("square of number in list")
print(square)