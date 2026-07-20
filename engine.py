import asyncio
import platform
import time
import aiohttp

# Виправлення для Windows + Python 3.8
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

TEST_ENDPOINTS = [
    "https://httpbin.org/ip",
    "https://api.github.com",
    "https://httpbin.org/user-agent",
    "https://httpbin.org/status/200",
    "https://httpbin.org/delay/1",
]

class NetworkEngineArchitect:
    def __init__(self, concurrency_limit=3):
        self.concurrency_limit = concurrency_limit
        self.results = []

    async def check_endpoint(self, session, semaphore, url):
        async with semaphore:
            start_time = time.time()
            try:
                async with session.get(url, timeout=5) as response:
                    latency = round((time.time() - start_time) * 1000, 2)
                    status = response.status
                    if status == 200:
                        print(f"✅ [SUCCESS] {url} | Status: {status} | Latency: {latency}ms")
                        return {"url": url, "status": "ACTIVE", "latency_ms": latency}
                    else:
                        print(f"⚠️ [WARNING] {url} | Status: {status}")
                        return {"url": url, "status": f"HTTP_{status}", "latency_ms": latency}
            except Exception as e:
                print(f"❌ [FAILED] {url} | Error: {type(e).__name__}")
                return {"url": url, "status": "OFFLINE", "latency_ms": None}

    async def run(self):
        print("=== [System Launch] High-Performance Asynchronous Network Engine ===")
        print(f"[*] Checking {len(TEST_ENDPOINTS)} endpoints asynchronously...\n")
        
        semaphore = asyncio.Semaphore(self.concurrency_limit)

        async with aiohttp.ClientSession() as session:
            tasks = [self.check_endpoint(session, semaphore, url) for url in TEST_ENDPOINTS]
            self.results = await asyncio.gather(*tasks)

        active_count = sum(1 for r in self.results if r["status"] == "ACTIVE")
        print("\n=== [Execution Report] ===")
        print(f"[+] Total Checked: {len(self.results)}")
        print(f"[+] Active Endpoints: {active_count}")
        print("[+] Status: Architecture Pipeline Execution Completed Cleanly.")

if __name__ == "__main__":
    engine = NetworkEngineArchitect(concurrency_limit=3)
    asyncio.run(engine.run())