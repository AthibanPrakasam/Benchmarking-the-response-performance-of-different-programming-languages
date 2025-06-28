SERVICES = {
    "python": "http://localhost:8001/process",
    "go": "http://localhost:8002/process",
    "node": "http://localhost:8003/process",
    "java": "http://localhost:8004/process",
}

def register_service(language, url):
    SERVICES[language] = url
