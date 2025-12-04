import asyncio
import random


async def produtor(fila):
    for i in range(5):
        await asyncio.sleep(random.uniform(0.1, 0.5))
        item = f"Item-{i+1}"
        await fila.put(item)
        print(f"[Produtor] Adicionou: {item}")
    await fila.put(None)
    print("--- Produtor finalizou o envio ---")


async def consumidor(fila):
    while True:
        item = await fila.get()
        if item is None:
            break
        print(f"[Consumidor] Processando: {item}...")
        await asyncio.sleep(1)
        print(f"[Consumidor] Finalizou: {item}")


async def main():
    fila = asyncio.Queue(maxsize=3)
    await asyncio.gather(produtor(fila), consumidor(fila))


asyncio.run(main())
