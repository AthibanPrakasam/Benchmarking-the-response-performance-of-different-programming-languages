from fastapi import FastAPI, HTTPException
from services.service_registry import SERVICES, register_service
from utils.benchmark import benchmark_services, benchmark_single, benchmark_services_with_payload
from pydantic import BaseModel
from typing import Dict, Any, Optional

app = FastAPI()

@app.get("/")
def root():
    return {"message": "LangSpeed Coordinator API"}

@app.get("/languages")
def get_languages():
    return {"languages": list(SERVICES.keys())}

@app.get("/benchmark")
def run_benchmark(rounds: Optional[int] = 5):
    return {"results": benchmark_services(SERVICES, rounds)}

@app.get("/benchmark/{language}")
def run_single(language: str, rounds: Optional[int] = 5):
    if language not in SERVICES:
        raise HTTPException(status_code=404, detail="Language not registered")
    return benchmark_single(language, SERVICES[language], rounds)

'''@app.post("/services")
def add_service(data: dict):
    lang = data.get("language")
    url = data.get("url")
    if not lang or not url:
        raise HTTPException(status_code=400, detail="Language and URL required")
    register_service(lang, url)
    return {"message": f"{lang} service registered successfully."}
'''
class DynamicPayload(BaseModel):
    payload: Dict[str, Any]
    rounds: Optional[int] = 5

@app.post("/benchmark-payload", summary="Send custom JSON payload to all services")
def benchmark_payload(request: DynamicPayload):
    return {
        "results": benchmark_services_with_payload(SERVICES, request.payload, request.rounds)
    }
