# Swap two numbers without using a temporary variable
# Given two integers a and b, swap their values using only bitwise operations.

# Examples:

# Input: a = 3, b = 5
# Output: a = 5, b = 3

# Input: a = 10, b = 25
# Output: a = 25, b = 10

# Hint: Use the XOR swap trick:
# XOR (^) has the neat property of flipping bits that differ and keeping bits that match.


def swap(a,b):
  #  print(a ^ (a ^ b), " ", b ^ (a ^ b))
 
 a = a ^ b  
 b = a ^ b
 a = a ^ b

 print(a, " ", b)

swap(3,5)