from fastapi import FastAPI

app = FastAPI()


@app.get("/")

def read_root():
    return { "Message": "This is cool" }



# @app.post("/login")

# def 