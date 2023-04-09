from fastapi import FastAPI

app = FastAPI()  # インスタンスを作成


@app.get("/")  # @：デコレータ
async def root():
    return {"message": "Hello World"}
