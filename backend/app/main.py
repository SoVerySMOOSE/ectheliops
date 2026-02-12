from fastapi import FastAPI

from .routes import router as monitors_router

app = FastAPI(title="EctheliOps")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"service": "EctheliOps", "message": "Hello"}

# routers get added AFTER app exists
app.include_router(monitors_router)