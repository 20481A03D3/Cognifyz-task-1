
def is_palindrome(input_str):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_str = ''.join(input_str.split()).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Example usage:
word_to_check = "madam"
result = is_palindrome(word_to_check)

if result:
    print(f"{word_to_check} is a palindrome.")
else:
    print(f"{word_to_check} is not a palindrome.")
