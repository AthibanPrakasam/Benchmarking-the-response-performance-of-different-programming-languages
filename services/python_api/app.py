from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()



@app.post("/process")
async def process(request: Request):
    try:
        await request.json()  # simulate processing
        return {
            "language": "python",
            "message": "Processed successfully"
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/process")
def health_check():
    return {
        "language": "python",
        "message": "GET /process is alive"
    }