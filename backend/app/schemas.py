from pydantic import BaseModel, HttpUrl, Field

class MonitorCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    url: HttpUrl

class MonitorUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=200)
    url: HttpUrl | None = None

class MonitorOut(BaseModel):
    id: int
    name: str
    url: str

    class Config:
        from_attributes = True