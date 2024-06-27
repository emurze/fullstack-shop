from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from container import container
from pizzas.api import pizzas_router

config = container.config()
app = FastAPI(title=config.app_title)
app.include_router(pizzas_router)

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
