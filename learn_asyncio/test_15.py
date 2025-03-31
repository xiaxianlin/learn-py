import asyncio
from asyncio import Queue
from random import sample, randint
from typing import List


class Product:
    """
    商品
    """

    def __init__(self, name: str, checkout_time: float):
        self.name = name  # 商品名称
        self.checkout_time = checkout_time  # 结算需要的时间


class Customer:
    """
    客户
    """

    def __init__(self, customer_id, products: List[Product]):
        self.customer_id = customer_id  # 客户的 id
        self.products = products  # 客户购买的商品


async def checkout_customer(queue: Queue, cashier_id: int):
    # 检查队列中是否有客户
    while not queue.empty():
        customer: Customer = await queue.get()
        print(f"收银员 {cashier_id} 开始对客户 {customer.customer_id} 的商品进行结算")
        for product in customer.products:
            print(
                f"收银员 {cashier_id} 正在结算客户 {customer.customer_id} 的商品: {product.name}"
            )
            await asyncio.sleep(product.checkout_time)
        print(f"收银员 {cashier_id} 已完成对客户 {customer.customer_id} 商品的结算")
        queue.task_done()  # 这行代码后续解释


async def main():
    customer_queue = Queue()
    all_products = [
        Product("苹果", 2),
        Product("香蕉", 0.5),
        Product("草莓", 1),
        Product("蓝莓", 0.2),
    ]
    # 创建 4 个客户，并用随机产品进行填充。
    for i in range(1, 5):
        products = sample(all_products, randint(1, 4))
        await customer_queue.put(Customer(i, products))
    # 创建三个收银员，从队列中取出客户，进行服务
    cashiers = [
        asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(1, 4)
    ]
    await asyncio.gather(customer_queue.join(), *cashiers)


asyncio.run(main())
