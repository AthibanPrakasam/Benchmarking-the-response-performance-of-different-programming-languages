import httpx
import time


def benchmark_services(service_dict, rounds=5):
    results = {}
    for lang, url in service_dict.items():
        results[lang] = benchmark_single(lang, url, rounds)
    return results


def benchmark_single(language, url, rounds=5):
    times = []
    for _ in range(rounds):
        try:
            start = time.time()
            response = httpx.get(url, timeout=10)
            end = time.time()
            times.append(round((end - start) * 1000, 2))
        except Exception:
            times.append(None)

    valid_times = [t for t in times if t is not None]
    if not valid_times:
        return {
            "language": language,
            "error": "All requests failed"
        }

    return {
        "language": language,
        "status_code": 200,
        "response_time_ms": {
            "min_ms": min(valid_times),
            "max_ms": max(valid_times),
            "avg_ms": round(sum(valid_times) / len(valid_times), 2),
            "all_times": valid_times
        }
    }


def benchmark_services_with_payload(services: dict, payload: dict, rounds=5):
    results = {}
    for lang, url in services.items():
        times = []
        final_response = None
        for _ in range(rounds):
            try:
                start = time.time()
                response = httpx.post(url, json=payload, timeout=10)
                end = time.time()
                times.append(round((end - start) * 1000, 2))
                if response.status_code == 200:
                    final_response = response.json()
            except Exception:
                times.append(None)

        valid_times = [t for t in times if t is not None]
        if not valid_times:
            results[lang] = {"error": "All requests failed"}
        else:
            results[lang] = {
                "status_code": 200,
                "response_time_ms": {
                    "min_ms": min(valid_times),
                    "max_ms": max(valid_times),
                    "avg_ms": round(sum(valid_times) / len(valid_times), 2),
                    "all_times": valid_times
                },
                "response": final_response
            }
    return results
