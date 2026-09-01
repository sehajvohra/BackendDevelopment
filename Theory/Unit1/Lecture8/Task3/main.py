from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"now": now},
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)