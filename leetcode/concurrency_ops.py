import asyncio

async def main_async():
    print("Welcom to your async process testing")
    task = asyncio.create_task( foo('second'))
    print("finished with async task")
    

async def foo(data):
    print(f"{data} asynchronously running process")
    await asyncio.sleep(1)
    

def bar():
    print("This process is running synchronously")
    
asyncio.run(main_async())
bar()
bar()