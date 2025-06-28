import httpx
import time

def benchmark_services(service_dict):
    results = {}
    for lang, url in service_dict.items():
        results[lang] = benchmark_single(lang, url)
    return results

def benchmark_single(language, url):
    try:
        start = time.time()
        response = httpx.get(url, timeout=10)
        end = time.time()
        return {
            "language": language,
            "status_code": response.status_code,
            "response_time_ms": round((end - start) * 1000, 2),
        }
    except Exception as e:
        return {
            "language": language,
            "error": str(e),
        }
    
def benchmark_services_with_payload(services: dict, payload: dict):
    results = {}
    for lang, url in services.items():
        try:
            start = time.time()
            response = httpx.post(url, json=payload, timeout=10)
            end = time.time()

            results[lang] = {
                "status_code": response.status_code,
                "response_time_ms": round((end - start) * 1000, 2),
                "response": response.json() if response.status_code == 200 else None
            }
        except Exception as e:
            results[lang] = {
                "error": str(e)
            }
    return results
