from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Ye hai mera tabname</title>
        </head>
        <body>
            <h3 style="{color: "pink"}">Balle balle de shava shava piyo piyo te kava kava!</h1>
        </body>
    </html>
    """

@app.get("/hiakku")
async def root():
    return { "message": "Hi i am akku" }
