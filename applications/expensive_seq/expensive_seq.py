# Your code here
 
store = {} #Create a place to store some data

def expensive_seq(x, y, z):
    if x <= 0: #From Readme
        return y + z 
    if (x, y, z) not in store and x > 0: #Some logic
        store[(x, y, z)] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y + 2, z*2) + expensive_seq(x-3, y+3, z*3) # Calculate and store the information

    return store[(x, y, z)] # Return the information from the store


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
