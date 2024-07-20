# Fast Api Entry point
from fastapi import FastAPI
from src.business_layer import process_word

app = FastAPI()



@app.post("/receive")
def receive_word()
    
    output = process_word(word)

    return output
    