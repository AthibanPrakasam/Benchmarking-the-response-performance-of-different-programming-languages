SERVICES = {
    "python": "http://python_api:8001/process",
    "go": "http://go_api:8002/process",
    "node": "http://node_api:8003/process",
    "java": "http://java_api:8080/process"
}

def register_service(language, url):
    SERVICES[language] = url
