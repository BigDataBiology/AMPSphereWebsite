from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src import models
from src.database import engine
from src.router import amp_router, family_router, default_router
import os


os.environ['worker_class'] = 'uvicorn.workers.UvicornH11Worker'
models.Base.metadata.create_all(bind=engine)


with open('description.md', 'r') as f:
    description = f.read()


app = FastAPI(
    title="AMPSphereBackend",
    # description=description,
    version="0.1.0",
    contact={
        "name": "Hui Chong",
        "url": "adebc.github.io",
        "email": "huichong.me@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://github.com/BigDataBiology/AMPSphereWebsite/blob/main/LICENSE",
    },
    docs_url='/',
    redoc_url='/redoc',
    openapi_url='/openapi.json'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


for router in [amp_router, family_router, default_router]:
    app.include_router(router=router)
