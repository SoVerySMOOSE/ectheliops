from fastapi import FastAPI

app = FastAPI(title="EctheliOps")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"service": "EctheliOps", "message": "Hello"}