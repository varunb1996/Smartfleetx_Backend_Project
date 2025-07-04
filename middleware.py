from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi import HTTPException
import time

rate_limit_storage = {}

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests=5, window=60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window = window

    async def dispatch(self, request: Request, call_next):
        ip = request.client.host
        now = time.time()
        request_log = rate_limit_storage.get(ip, [])
        request_log = [timestamp for timestamp in request_log if now - timestamp < self.window]
        if len(request_log) >= self.max_requests:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        request_log.append(now)
        rate_limit_storage[ip] = request_log
        return await call_next(request)
