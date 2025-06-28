
# 🚀 Benchmarking the Response Performance of Different Programming Languages

This project benchmarks the **response performance (speed and efficiency)** of different programming languages — **Python, Go, Node.js, and Java** — by comparing how fast each one processes API requests.

---

## 📌 Repository

GitHub: [AthibanPrakasam/Benchmarking-the-response-performance-of-different-programming-languages](https://github.com/AthibanPrakasam/Benchmarking-the-response-performance-of-different-programming-languages)

---

## 🧰 Tech Stack

- **Coordinator API:** FastAPI (Python)
- **Service APIs:**
  - Python (FastAPI)
  - Go (Gin)
  - Node.js (Express)
  - Java (Spring Boot)
- **Containerization:** Docker & Docker Compose

---

## 🛠 Setup Instructions

### 1. Clone the Repository


git clone https://github.com/AthibanPrakasam/Benchmarking-the-response-performance-of-different-programming-languages.git
cd Benchmarking-the-response-performance-of-different-programming-languages


### 2. Run the Project via Docker


docker compose up --build


> ✅ Ensure ports `8000` to `8004` are available.

---

## 🌐 API Endpoints (Coordinator API – `http://localhost:8000`)

### `GET /`

Returns a welcome message.

---

### `GET /languages`

Returns the list of registered programming languages.

---

### `GET /benchmark`

Runs a benchmarking test (GET request) against **all registered language services**, calculates their response time over multiple rounds, and returns the **average response time**.

#### Optional Query Parameter:

* `rounds`: Number of rounds to repeat the benchmark (default = 1)

Example:


GET /benchmark?rounds=5


---

### `GET /benchmark/{language}`

Runs the benchmark for a **single language** using a GET request.

Example:


GET /benchmark/python


---

### `POST /benchmark-payload`

Sends a **custom JSON payload** to all services via POST and benchmarks how fast each language processes the input.

#### Request Body Example:


{
  "payload": {
    "data": ["example", "test"]
  },
  "rounds": 3
}


---

### `POST /services`

Register a **new language and its API endpoint** dynamically.

#### Request Body Example:


{
  "language": "rust",
  "url": "http://localhost:8005/process"
}


---

## 📊 Sample Response (Payload Benchmark)


{
  "results": {
    "python": {
      "language": "python",
      "status_code": 200,
      "average_response_time_ms": 83.42
    },
    "go": {
      "language": "go",
      "status_code": 200,
      "average_response_time_ms": 43.17
    },
    "node": {
      "language": "node",
      "status_code": 200,
      "average_response_time_ms": 38.92
    },
    "java": {
      "language": "java",
      "status_code": 200,
      "average_response_time_ms": 77.15
    }
  }
}


---

## 📁 Folder Structure

.
├── coordinator_api/
│   ├── main.py
│   ├── benchmark.py
│   └── requirements.txt
├── services/
│   ├── python_api/
│   │   ├── main.py
│   │   └── Dockerfile
│   ├── go_api/
│   │   ├── main.go
│   │   └── Dockerfile
│   ├── node_api/
│   │   ├── index.js
│   │   └── Dockerfile
│   ├── java_service/
│       ├── JavaController.java
│       └── Dockerfile
├── docker-compose.yml
├── README.md


---

## 🚦 Benchmark Strategy

* Each language has a `/process` endpoint to simulate payload handling.
* The coordinator sends:

  * `GET` request for basic speed check.
  * `POST` request with a JSON payload to simulate processing load.
* Each response time is measured using Python’s `time.time()` with HTTP requests via `httpx`.

---

## 📈 Roadmap

* [x] Add benchmarking across Python, Go, Node.js, Java
* [x] Dockerize all services
* [x] Add custom payload support
* [x] Add average benchmarking over multiple rounds
* [ ] Add support for more languages (Rust, Ruby, PHP, etc.)
* [ ] Add a simple frontend for visualization

---

## 🙋 Author

**Athiban Prakasam**
GitHub: [@AthibanPrakasam](https://github.com/AthibanPrakasam)

---

## 📝 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)



---

Let me know if you'd like to add:
- **Badges** (GitHub workflow, Docker, FastAPI, etc.)
- **Screenshots** or CLI output
- **Contributors** or acknowledgments

You can now commit and push this file:

git add README.md
git commit -m "Add complete README with setup and API guide"
git push origin develop

