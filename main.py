import textwrap

"""
This module provides utility functions for string manipulation and formatting.
It demonstrates how well-documented code with clear examples can improve
readability and ease of use, reflecting the principles of good technical documentation.

Each function includes a comprehensive docstring explaining its purpose, arguments,
return values, and practical usage examples. The main execution block further
illustrates how to use these functions with clear output.
"""

def reverse_string(text: str) -> str:
    """
    Reverses the order of characters in a given string.

    This function takes a string as input and returns a new string with
    the characters in reverse order. It's a basic string manipulation utility.

    Args:
        text (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Examples:
        >>> reverse_string("hello")
        "olleh"
        >>> reverse_string("Python")
        "nohtyP"
        >>> reverse_string("")
        ""
    """
    # Core logic for reversing a string
    return text[::-1]

def count_vowels(text: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u, case-insensitive) in a string.

    This function iterates through the input string, converts each character
    to lowercase, and checks if it's one of the five standard English vowels.

    Args:
        text (str): The input string to count vowels from.

    Returns:
        int: The total count of vowels found in the string.

    Examples:
        >>> count_vowels("Hello World")
        3
        >>> count_vowels("Python Programming")
        5
        >>> count_vowels("AEIOUaeiou")
        10
        >>> count_vowels("rhythm")
        0
    """
    vowels = "aeiou"
    count = 0
    # Iterate through each character and check if it's a vowel
    for char in text.lower(): # Convert to lowercase for case-insensitivity
        if char in vowels:
            count += 1
    return count

def format_currency(amount: float, currency_symbol: str = "$") -> str:
    """
    Formats a numeric amount as a currency string.

    This function takes a float representing an amount and an optional
    currency symbol, then formats it to two decimal places. It's useful
    for displaying monetary values consistently.

    Args:
        amount (float): The numeric value to format.
        currency_symbol (str, optional): The symbol to prepend to the amount.
                                         Defaults to "$".

    Returns:
        str: The formatted currency string (e.g., "$123.45").

    Examples:
        >>> format_currency(123.456)
        "$123.46"
        >>> format_currency(99.9)
        "$99.90"
        >>> format_currency(1000, "€")
        "€1000.00"
        >>> format_currency(0.0)
        "$0.00"
    """
    # Format the amount to two decimal places and prepend the symbol
    return f"{currency_symbol}{amount:.2f}"

if __name__ == "__main__":
    print("--- Demonstrating String Utility Functions ---")

    print("\n# 1. Reversing a String")
    # Example 1: Basic string reversal, illustrating clear input/output
    original_str_1 = "Dokümantasyon"
    reversed_str_1 = reverse_string(original_str_1)
    print(f"Original: '{original_str_1}' -> Reversed: '{reversed_str_1}'")

    # Example 2: Reversing a sentence, showing different use cases
    original_str_2 = "Teknik Belgeler"
    reversed_str_2 = reverse_string(original_str_2)
    print(f"Original: '{original_str_2}' -> Reversed: '{reversed_str_2}'")

    print("\n# 2. Counting Vowels")
    # Example 1: Counting vowels in a simple word
    text_1 = "Merhaba Dünya"
    vowel_count_1 = count_vowels(text_1)
    print(f"Text: '{text_1}' -> Vowel Count: {vowel_count_1}") # Clear demonstration of function usage

    # Example 2: Case-insensitivity check, highlighting a function feature
    text_2 = "PYtHoN"
    vowel_count_2 = count_vowels(text_2)
    print(f"Text: '{text_2}' -> Vowel Count: {vowel_count_2}")

    print("\n# 3. Formatting Currency")
    # Example 1: Default currency symbol, showing how optional arguments work
    price_1 = 1234.567
    formatted_price_1 = format_currency(price_1)
    print(f"Price: {price_1} -> Formatted: {formatted_price_1}")

    # Example 2: Custom currency symbol, demonstrating flexibility
    price_2 = 99.9
    formatted_price_2 = format_currency(price_2, "₺") # Turkish Lira symbol
    print(f"Price: {price_2} -> Formatted: {formatted_price_2}")

    # Example 3: Zero amount, testing edge cases
    price_3 = 0.0
    formatted_price_3 = format_currency(price_3, "€")
    print(f"Price: {price_3} -> Formatted: {formatted_price_3}")

    print("\n--- End of Demonstration ---")
    print("Review the code to see how docstrings and examples improve clarity and ease of use.")
