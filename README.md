# High-Performance Asynchronous Network Verification Engine

An enterprise-grade, non-blocking network architecture script built to handle concurrent network requests, latency measurements, and HTTP status verification.

## Features
- **Concurrency Throttling:** Utilizes asyncio.Semaphore to manage connection pools safely.
- **Non-blocking I/O:** Powered by aiohttp for maximum request throughput.
- **Cross-Platform Compatibility:** Features automated event loop policy adaptation for Windows systems.
- **Real-Time Latency Metrics:** Calculates precise execution latency in milliseconds.

## Tech Stack
- **Language:** Python 3.8+
- **Async Framework:** Asyncio & Aiohttp

## Quick Start
1. Install dependencies:
   pip install aiohttp

2. Run the engine:
   python engine.py
