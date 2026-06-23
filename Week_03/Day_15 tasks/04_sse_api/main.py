from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse
import asyncio

app = FastAPI()


async def event_generator():
    count = 0
    while True:
        count +=1

        yield{
            "data": f"Counter: {count}"
        }

        await asyncio.sleep(1)


@app.get("/events")
async def stream_events():
    
    return EventSourceResponse(
        event_generator()
    )