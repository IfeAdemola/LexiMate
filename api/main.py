from typing import Union, Dict
from fastapi import FastAPI
from src.word_explorer import generate_explanations

app = FastAPI()

@app.get("/explain/{word}")
def explain_word(word: str) -> Dict[str, str]:
    explanation = generate_explanations(word)
    return {"word": word, "explanation": explanation}

@app.get("/")
def welcome():
    return "Welcome to the Word Explorer API!"