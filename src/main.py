from fastapi import FastAPI
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from apis.health_check_module import health_check_router
from apis.dropbox import drop_box_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_check_router)
app.include_router(drop_box_route)