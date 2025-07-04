from fastapi.middleware.cors import CORSMiddleware
from app.middleware import RateLimitMiddleware
from fastapi import FastAPI
from app.api import routes_fleet, routes_vehicle

app = FastAPI(title="SmartFleetX API")

app.include_router(routes_fleet.router, prefix="/fleet", tags=["Fleet"])
app.include_router(routes_vehicle.router, prefix="/vehicle", tags=["Vehicle"])

app.add_middleware(RateLimitMiddleware)
from app.api import routes_auth
app.include_router(routes_auth.router, tags=["Auth"])
