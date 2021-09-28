#WRITE YOUR CODE IN THIS FILE
#define Function 
def close10(x,y):
    if abs(10-x)>= abs(10-y):
        return y

    elif abs(10-x)<= abs(10-y):
        return x

    else:
        return 0

print(close10(5, 12))  