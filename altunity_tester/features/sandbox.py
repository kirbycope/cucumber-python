#$  python altunity_tester/features/sandbox.py -d "C:\\Users\\kirby\\cucumber-python\\altunity_tester\\features"

import argparse
import asyncio
import datetime
import pathlib
import os


phone1 = "Samsung_Galaxy_S8_POC104"
phone2 = "Samsung_Galaxy_S8_POC144"
phone3 = "Samsung_Galaxy_S8_POC182"
phone4 = "Samsung_Galaxy_S8_POC112"


async def run_behave(args):    
    proc = await asyncio.create_subprocess_exec("behave", *args.split())
    await proc.communicate()


async def main():
    # Print start time
    print("Start Time: " + str(datetime.datetime.now()))
    # Get context
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Get opts
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory')
    args = parser.parse_args()
    # Set the working directory
    directory_provided = os.path.isdir(args.directory) if args.directory != None else False
    directory = args.directory if directory_provided else current_directory
    # Create a list of test runs
    features = []
    for path in pathlib.Path(directory).rglob('*.feature'):
        args = "altunity_tester/features --junit --quiet --include=" + path.name + ""
        features.append(run_behave(args))
    # Run `behave` so that all .features run at the same time
    await asyncio.gather(*features)
    # ToDo: Handle results
    print("Done!")
    # Print end time
    print("End Time: " + str(datetime.datetime.now()))

# This is the entry point if this file is executed rather than imported
if __name__ == '__main__':
    asyncio.run(main())
