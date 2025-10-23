# Count the number of set bits (1s) in an integer
# Given an integer n, return how many bits are set to 1 in its binary representation.

# Examples:

# Input: n = 5   # binary 101
# Output: 2

# Input: n = 15  # binary 1111
# Output: 4

# Hint: Keep checking the least significant bit using (n & 1), then shift right by one (n >>= 1) until n becomes zero.

# (Bonus: You can also use n = n & (n-1) trick to remove one bit at a time.)

def setOfBits(n):
    print(n)

    k=0
    while (n > 0):
     if (n & 1):
         k+=1
     n>>=1
    return k

setOfBits(5)

#counter
# if n & 1
