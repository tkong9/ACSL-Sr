def limit_repeats(input_string, max_length):
    result = []  # List to store the modified characters
    count = 1  # Counter for consecutive characters

    # Iterate through the string starting from the second character
    for i in range(1, len(input_string)):
        # If current character is the same as the previous one
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            count = 1  # Reset the counter if different character

        # If count is within the max length, append the character to result
        if count <= max_length:
            result.append(input_string[i])
        else:
            # Skip the character if count exceeds max_length
            continue

    # Return the first character of input string concatenated with result list
    return input_string[0] + ''.join(result)

# Test case
input_string = "EEEEEEOOORRBKP"
max_length = 4
output = limit_repeats(input_string, max_length)
print(output)  # Output: "MMMGGMMMXXABDMZ"