import streamlit as st

def guessing_game():
    secret_number = st.number_input("Enter a secret number:", min_value=1, max_value=100)
    guess = st.number_input("Guess the number:")

    if guess == secret_number:
        st.success("Congratulations! You guessed the number correctly.")
    elif guess > secret_number:
        st.error("Your guess is too high. Try again.")
    else:
        st.error("Your guess is too low. Try again.")

def main():
    st.title("Guessing Game")
    guessing_game()

if __name__ == "__main__":
    main()