import asyncio
import os
import json
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


async def gather_raid_data(bungie_id):
    # create a user obj using a known bungie id
    user = DestinyUser(membership_id=int(bungie_id), membership_type=BungieMembershipType.TIGER_STEAM)
    # iterate thought the raids that user has played
    with open(f"{bungie_id}_raid.json", "w") as outfile:
        response_list = []
        print("Started fetching data, this may take a while")
        async for activity in user.yield_activity_history(mode=DestinyActivityModeType.RAID):

            # Running a raw request through the wrapper for saving purposes
            report = await client.http.get_post_game_carnage_report(activity.activity_details.instance_id)
            response_list.append(report)

        print("Data collected")
        outfile.write(json.dumps(response_list, indent=4))
        print("File written")

if __name__ == "__main__":
    asyncio.run(gather_raid_data(4611686018467273361))  # Put your own bungie_id here
