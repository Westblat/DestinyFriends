import asyncio
import datetime
import os
import json

from pytz import timezone
from bungio import Client
from bungio.models import BungieMembershipType, DestinyActivityModeType, DestinyUser
from dotenv import load_dotenv


load_dotenv()

# create the client obj with our bungie authentication
client = Client(
    bungie_client_id=os.getenv("BUNGIE_OAUTH_CLIENT_ID"),
    bungie_client_secret=os.getenv("BUNGIE_OAUTH_CLIENT_SECRET"),
    bungie_token=os.getenv("BUNGIE_API_KEY"),
)


async def gather_raid_data(bungie_id, update=False):
    raid_time = datetime.datetime(2017, 9, 6)
    # create a user obj using a known bungie id
    user = DestinyUser(membership_id=int(bungie_id), membership_type=BungieMembershipType.TIGER_STEAM)
    # iterate thought the raids that user has played
    response_list = []
    if update:
        # Update the file based on the time of the last raid
        f = open(f"{bungie_id}_raid.json")
        data = json.load(f)
        time = data[0].get("Response").get("period")
        # Add completely arbitary (tested) value, so that the previous raid is not added as a double
        raid_time = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=1, minutes=45)
        response_list = data

    with open(f"{bungie_id}_raid.json", "w") as outfile:
        new_data = []
        print("Started fetching data, this may take a while")
        async for activity in user.yield_activity_history(
                mode=DestinyActivityModeType.RAID,
                earliest_allowed_datetime=raid_time.replace(tzinfo=timezone("Europe/Helsinki"))
        ):
            # Running a raw request through the wrapper for saving purposes
            report = await client.http.get_post_game_carnage_report(activity.activity_details.instance_id)
            new_data.append(report)

        combined_list = new_data + response_list
        print("Data collected")
        outfile.write(json.dumps(combined_list, indent=4))
        print("File written")

if __name__ == "__main__":
    asyncio.run(gather_raid_data(4611686018467273361, True))  # Put your own bungie_id here
