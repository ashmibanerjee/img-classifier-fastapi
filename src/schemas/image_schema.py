from pydantic import BaseModel


class Img(BaseModel):
    img_url: str
