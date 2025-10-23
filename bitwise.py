# Check if a number is even or odd (using bitwise)
# Given an integer n, determine if it is even or odd using bitwise operations (no % or / allowed).

# Examples:

# Input: n = 5
# Output: "Odd"

# Input: n = 12
# Output: "Even"

# Hint: The least significant bit (LSB) tells you if a number is odd or even. If (n & 1) equals 1 → odd. If (n & 1) equals 0 → even.

# Python changes it to Binary by default

def bitWise(n):
    one = 1
    print(one)
    ourAnd = one & n
    print(ourAnd)
    if(ourAnd): print("Odd")
    else: print("Even")

bitWise(11)