## Destiny friends
Small collection of scripts to see who you have most raided with in Destiny 2.

# How to use?
All the scripts can be ran as their own by running the files they are in

Running the ```ìnteractive_start.py``` gives you a simpler experience of using the scripts

# Before you run the script

Create a Bungie application in https://www.bungie.net/en/Application

Make sure you make the Oauth Client Type as Confidential.

Once you have created the application fill ```.env.example``` and rename it as ```.env```

# How it works?

The scripts fetch all the raids you have done, so it takes a while.

The default behaviour is to save it as a file, so if you have raided a lot, the file might take quite a lot of space.
With over 300 recorded raid activities, the file size is 26.5MB. This is saved so that future analysis can be done faster.

# In the future
There can always be more analysis on the data.

This app can be extended to dungeons (and in theory to crucible and more).

One could learn to use either the wrapper or bungie api properly instead of taking the best of both worlds