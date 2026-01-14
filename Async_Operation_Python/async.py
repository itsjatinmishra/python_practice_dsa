import asyncio

async def fetch_data(delay):
    print(f'Starting {delay} seconds delay')
    await asyncio.sleep(delay)
    print(f'Finished {delay} seconds delay')
    return f'Task is done'

async def main():
    print("Start of main coroutine ...")

    # task01 = fetch_data(2)
    # task02 = fetch_data(2)

    task01 = asyncio.create_task(fetch_data(2))
    task02 = asyncio.create_task(fetch_data(4))

    result01 = await task01
    print(f'Recevied result : {result01}')
    result02 = await task02
    print(f'Recevied result : {result02}')

    print('End of main coroutine ...')
# main()
# print(main)
asyncio.run(main())