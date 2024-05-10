import asyncio

from gather_data import gather_raid_data


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(gather_raid_data(4611686018467273361))


if __name__ == "__main__":
    main()
