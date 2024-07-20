import streamlit as st

if 'words' not in st.session_state:
    st.session_state.words = []

st.title("Leximate - Your Language Learning Companion")

new_word = st.text_input("Enter a word you want to learn")

# Button to add the word to the list
if st.button("Add Word"):
    if new_word:
        st.session_state.words.append(new_word)
        st.success(f"'{new_word}' has been added to your list.")
        new_word = ""  # Clear the input box
    else:
        st.error("Please enter a word.")

if st.session_state.words:
    st.subheader("Words you are learning:")
    for word in st.session_state.words:
        st.write(f"- {word}")

if st.button("Clear List"):
    st.session_state.words = []
    st.success("The list has been cleared.")