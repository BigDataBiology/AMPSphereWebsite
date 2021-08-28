from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from router import browse_router, compute_router, search_router

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

app.include_router(
    router=browse_router
)
app.include_router(
    router=compute_router
)
app.include_router(
    router=search_router
)

