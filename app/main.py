from fastapi import FastAPI
from fastapi import Response
import json

app = FastAPI()

data = {
  "status_code": 200,
  "detail": "ok",
  "result": "working"
}

@app.get('/')
def health_check():
    json_str = json.dumps(data, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')
#
# @app.get("/health_check")
# def hello():
#     return "health check"