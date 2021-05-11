# Program to count upper and lower case characters without using inbuilt functions

def count_upper_lower_characters(str_1):
    """
    Function to count upper and lower case characters without using inbuilt functions
    :param str_1: String
    :return: None
    """
    # Flags for
    char_count_uppercase = 0
    char_count_lowercase = 0

    for i in range(len(str_1)):

        # For lowercase characters
        if 97 <= ord(str_1[i]) <= 122:
            char_count_lowercase += 1

        # For uppercase characters
        elif 65 <= ord(str_1[i]) <= 90:
            char_count_uppercase += 1

    print(f'Lower case characters: {char_count_lowercase} \nUpper case characters: {char_count_uppercase}')


# Driver Code
string_1 = 'HeLLo WorLD Upper'

# Function call
count_upper_lower_characters(string_1)
