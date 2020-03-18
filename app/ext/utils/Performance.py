from concurrent.futures import ThreadPoolExecutor
import asyncio


class Performance:
    """Performance Module
    - run_in_threadpool
    """
    def __init__(self, max_threads: int = 4):
        """
        ```
        Performance(max_threads: int)
        max_threads:
            Default 4
        ```
        """
        self.running_threads = 0 # Fixed value
        self.max_threads = max_threads

    async def run_in_threadpool(self, function):
        """run_in_threadpool Usage:
        ```
        ...
        async def main():
            data = await run_in_threadpool(lambda: function())
            return data
        ```
        """
        global running_threads

        while self.running_threads >= self.max_threads:
            await asyncio.sleep(1)

        with ThreadPoolExecutor(max_workers=1) as thread_pool:
            running_threads = self.running_threads + 1

            loop = asyncio.get_event_loop()
            result = loop.run_in_executor(thread_pool, function)
            try:
                result = await result
            except Exception as e:
                raise e
            finally:
                running_threads = running_threads - 1
                thread_pool.shutdown(wait=True)
            return result