from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from stage import return_text

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": True, "message": "Hello!"}


@app.post("/main")
async def main(jsons: dict):
    return await return_text(pagetext=jsons["pagetext"])


@app.get("/favicon.ico")
async def favicon():
    return FileResponse("favicon.ico")


# if __name__ == "__main__":
#     uvicorn.run("app:app", host="127.0.0.1", port=8080, reload=True)