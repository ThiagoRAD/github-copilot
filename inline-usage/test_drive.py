# Write a program that converts a Roman numeral to an integer
def roman_to_int(s: str) -> int:
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# Example usage
print(roman_to_int("IV"))  # Output: 4
# Example usage
print(roman_to_int("MCMXCIV"))  # Output: 1994

# Write a program that calculates the factorial of a number
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
      
      
      