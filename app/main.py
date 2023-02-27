import uvicorn
from fastapi import FastAPI
from fastapi import Response
import json
from fastapi.middleware.cors import CORSMiddleware
#from dotenv import load_dotenv
#import os
from app.config import settings

#load_dotenv()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



data = {
  "status_code": 200,
  "detail": "ok",
  "result": "working"
}

@app.get('/')
def health_check():
    json_str = json.dumps(data, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')


if __name__ == "__main__":
    #uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))
    uvicorn.run(app, host=settings.HOST, port=int(settings.PORT))