import asyncio


async def start_strongman(*args):
    name, power = args
    print(f'Силач {name} начал соревнование')
    for i in range(5):
        await asyncio.sleep(1./power)
        print(f'Силач {name} поднял шар номер {i+1}.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    strongmen = [('Вася Пупкин', 20), ('Ося Пупкинд', 15), ('Ганс Пупкен', 10)]
    tasks = []
    for sm_ in strongmen:
        tasks.append(asyncio.create_task(start_strongman(*sm_)))
    for t_ in tasks:
        await t_

if __name__ == '__main__':
    asyncio.run(start_tournament())