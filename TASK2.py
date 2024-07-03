import streamlit as st
import math

board = ['-'] * 9
AI = 'O'
YOU = 'X'

def print_board(board):
    for i in range(0, 9, 3):
        st.write(board[i] + '|' + board[i + 1] + '|' + board[i + 2])
    st.write('')

def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full(board):
    return all(cell != '-' for cell in board)

def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, AI):
        return 1
    elif check_winner(board, YOU):
        return -1
    elif is_board_full(board):
        return 0
    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = AI
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = '-'
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = YOU
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = '-'
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board):
    best_move = -1
    best_eval = -math.inf
    for i in range(9):
        if board[i] == '-':
            board[i] = AI
            eval = minimax_alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = '-'
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

if 'board' not in st.session_state:
    st.session_state.board = ['-'] * 9

st.title("Tic Tac Toe with AI")

if st.button("Reset Game"):
    st.session_state.board = ['-'] * 9

print_board(st.session_state.board)

move = st.selectbox("Select your choice (0-8):", list(range(9)))

if st.button("Make Move"):
    if st.session_state.board[move] == '-':
        st.session_state.board[move] = YOU
        if check_winner(st.session_state.board, YOU):
            print_board(st.session_state.board)
            st.write("You win!")
        elif is_board_full(st.session_state.board):
            print_board(st.session_state.board)
            st.write("It's a draw!")
        else:
            ai_move = find_best_move(st.session_state.board)
            st.session_state.board[ai_move] = AI
            if check_winner(st.session_state.board, AI):
                print_board(st.session_state.board)
                st.write("AI wins!")
            elif is_board_full(st.session_state.board):
                print_board(st.session_state.board)
                st.write("It's a draw!")
    else:
        st.write("Cell already filled. Try again.")

print_board(st.session_state.board)
