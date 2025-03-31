import asyncio
from asyncio import Queue
from functools import partial
from random import randint
from fastapi import FastAPI, APIRouter
from fastapi.requests import Request
from fastapi.responses import Response
import uvicorn

router = APIRouter()


async def process_order_worker(worker_id: int, order_queue: Queue):
    # 从队列中获取订单，然后处理它
    while True:
        print(f"Worker {worker_id}, 等待订单")
        order = await order_queue.get()
        print(f"Worker {worker_id}, 开始处理订单")
        await asyncio.sleep(order)
        print(f"Worker {worker_id}, 订单处理完毕")
        order_queue.task_done()


@router.post("/order")
async def place_order(request: Request):
    order_queue: Queue = request.app.state.order_queue
    # 将订单放入队列，并立即响应用户，这里用一个 sleep 时长来模拟订单处理
    await order_queue.put(randint(1, 4))
    return Response("订单已被接收, 等待后台处理", media_type="text/plain")


async def create_order_queue(app: FastAPI):
    # 程序启动时执行的钩子函数
    print("创建队列和任务")
    # 创建一个最多容纳 10 个元素的队列，并创建 4 个 worker
    order_queue: Queue = asyncio.Queue(10)
    app.state.order_queue = order_queue
    # 程序启动之后会创建 4 个 worker，然后不断地从队列中取出订单，进行处理
    app.state.order_tasks = [
        asyncio.create_task(process_order_worker(i, order_queue)) for i in range(1, 5)
    ]


async def destroy_order_queue(app: FastAPI):
    # 程序结束时执行的钩子函数
    order_tasks = app.state.order_tasks
    # 等待所有繁忙的任务完成
    order_queue: Queue = app.state.order_queue
    print("等待尚未完成的任务执行完毕, 但只有 10 秒的机会")
    try:
        # 10 秒内未完成，那么程序直接结束，不再等待
        await asyncio.wait_for(order_queue.join(), timeout=10)
    except asyncio.TimeoutError:
        print("程序结束, 但还有任务尚未完成, 这里直接取消")
    finally:
        [task.cancel() for task in order_tasks]


app = FastAPI()
app.include_router(router)
app.router.on_startup.append(partial(create_order_queue, app))
app.router.on_shutdown.append(partial(destroy_order_queue, app))

if __name__ == "__main__":
    uvicorn.run(app, port=9999)
