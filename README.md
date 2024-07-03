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

TASK 2 - TIC-TAC-TOE AI

Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable.This project will help us understand your game theory and basic search algorithms.

Example of Execution Flow:

1.The game starts by printing the empty board.

2.The user is prompted to make a move.

3.The user's move is validated and placed on the board.

4.The game checks if the user has won or if the board is full.

5.The AI calculates the best move using the minimax algorithm with alpha-beta pruning and makes its move.

6.The game checks if the AI has won or if the board is full.

7.Steps 2-6 are repeated until there is a winner or the game ends in a draw.

This approach ensures a robust and efficient Tic-Tac-Toe game with a competent AI opponent.

DEPLOYMENT:

## Installation


1.Clone the Repository
   ```sh
   git clone <your-repository-url>
   cd <your-repository-directory>
2.Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3.Install the required packages:

4.pip install streamlit

5.streamlit run programname.py

6.First create the app and connect to github repository in streamlit cloud and deploy the app.
