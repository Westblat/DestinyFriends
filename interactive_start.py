import asyncio
from pathlib import Path
from gather_data import gather_raid_data
from analyze import analyze


async def interactive_start():
    bungie_id = input("What is your bungie id?\n")
    file_location = Path.cwd() / f"{bungie_id}_raid.json"
    delete_file = input("Do you want to delete the associated file? (y/n)\n")
    try:
        if Path(file_location).is_file():
            update = input("File already found, do you want to update or analyze existing file? (update / analyze)\n")
            if update == "update":
                await gather_raid_data(bungie_id, True)
        else:
            await gather_raid_data(bungie_id)
        analyze(f"{bungie_id}.json")
    except:
        print("Something went wrong :(")
    if delete_file == 'y' or delete_file == 'yes':
        Path.unlink(file_location)


asyncio.run(interactive_start())