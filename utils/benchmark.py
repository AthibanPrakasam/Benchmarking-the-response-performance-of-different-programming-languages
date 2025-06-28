import httpx
import time
import asyncio

# ---------- ASYNC GET ----------
async def benchmark_single_async(language, url, client):
    try:
        start = time.time()
        response = await client.get(url, timeout=10)
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

async def benchmark_services(service_dict):
    async with httpx.AsyncClient() as client:
        tasks = [benchmark_single_async(lang, url, client) for lang, url in service_dict.items()]
        results = await asyncio.gather(*tasks)
    return {r["language"]: r for r in results}

# ---------- SYNC GET (SINGLE) ----------
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

# ---------- ASYNC POST (WITH PAYLOAD) ----------
async def benchmark_post_single(lang, url, payload, client):
    try:
        start = time.time()
        response = await client.post(url, json=payload, timeout=10)
        end = time.time()
        return {
            lang: {
                "status_code": response.status_code,
                "response_time_ms": round((end - start) * 1000, 2),
                "response": response.json() if response.status_code == 200 else None
            }
        }
    except Exception as e:
        return {
            lang: {
                "error": str(e)
            }
        }

async def benchmark_services_with_payload(services: dict, payload: dict):
    async with httpx.AsyncClient() as client:
        tasks = [benchmark_post_single(lang, url, payload, client) for lang, url in services.items()]
        responses = await asyncio.gather(*tasks)
    result = {}
    for r in responses:
        result.update(r)
    return result
