
import asyncio

async def a_task_1():
    """Some task that takes time."""
    for i in range(5):
        print(f"Task is running... {i}")
        await asyncio.sleep(1)  # Simulate a time-consuming task
    return "Task completed"


async def a_task_2():
    """Another task that takes time."""
    for i in range(3):
        print(f"Another task is running... {i}")
        await asyncio.sleep(1)  # Simulate a time-consuming task
    return "Another task completed"


def sequential_execution():
    """Run tasks sequentially."""
    result1 = asyncio.run(a_task_1())
    print(result1)
    result2 = asyncio.run(a_task_2())
    print(result2)
    
async def parallel_execution():
    """Run tasks in parallel."""
    results = await asyncio.gather(a_task_1(), a_task_2())
    return results
    
if __name__ == "__main__":
    print("Running tasks sequentially:")
    sequential_execution()
    
    print("\nRunning tasks in parallel:")
    results = asyncio.run(parallel_execution())
    for result in results:
        print(result)
