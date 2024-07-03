TASK 1 - CHATBOT WITH RULE-BASED RESPONSES

Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or pattern matching techniques to identify user queries and provide appropriate responses. This task will let us understand about your knowledge of natural language processing and conversation flow.
Explanation:
1.Pattern Matching:

Patterns are defined using regular expressions (patterns dictionary) to match against user input.
Each key in the dictionary is a regular expression pattern, and the corresponding value is the chatbot's response.
re.search Function:

2.re.search(pattern, string) is used to search for the pattern in the user's lowercase input string (user_input_lower).
If a match is found, the corresponding response from the patterns dictionary is returned.

3.Interactive Loop:

The script welcomes the user and starts an interactive loop where it continuously accepts user input.
It checks if the user wants to exit (exit command) and ends the conversation if so.
Otherwise, it passes the user input to chatbot_response, retrieves the response, and prints it.

4.Default Response:

If no patterns match the user input, a default response is returned indicating that the chatbot didn't understand the input.
