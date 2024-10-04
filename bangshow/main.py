#!/usr/bin/python
import argparse
from bangshow.getpics import get_pics
from bangshow.getpics import output_path as pics_path
from bangshow.namedic import CHAR_TO_ID, BAND_TO_ID
import pkg_resources
import subprocess
import os

CHAFA = "chafa"
SLIDES_PLAYER_SC = pkg_resources.resource_filename('bangshow', "slidesplayer")


def get_id(name):
    # Get the ID for the specified band or character
    band_id = None
    char_id = None
    if name in CHAR_TO_ID:
        char_id = CHAR_TO_ID[name]
    elif name in BAND_TO_ID:
        band_id = BAND_TO_ID[name]
    return (band_id, char_id)

def update_images(name):
    # Logic to update images for the specified band or character
    print(f"Updating images for {name}...")
    band_id, char_id = get_id(name)
    get_pics(band_id, char_id)

def display_images(name, delay):
    # Logic to display images for the specified band or character
    print(f"Displaying images for {name}...")
    band_id, char_id = get_id(name)
    char_ids = []
    if char_id:
        char_ids.append(char_id)
    elif band_id:
        char_ids = list(range(band_id*5-4, band_id*5+1))
    
    for char_id in char_ids:
        args = [SLIDES_PLAYER_SC, f"{pics_path}/res{str(char_id).zfill(3)}*/*.png", str(delay)]
        try:
            subprocess.run(args)
        except KeyboardInterrupt:
            print("\nDisplay stopped.")
            exit(0)

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Bang Dream Images Display Tool")

    # Add optional parameters
    parser.add_argument('-u', action='store_true', help='Update images')
    parser.add_argument('-s', action='store_true', help='Display images')
    parser.add_argument('-d', type=float, default=1, help='Specify delay (in seconds) between image displays')
    parser.add_argument('-l', action='store_true', help='Loop playback of images')

    # Allow multiple names to be passed (nargs='+')
    parser.add_argument('name', nargs='+', help='Band or character name(s)')

    # Parse the command-line arguments
    args = parser.parse_args()


    if args.u:
        for name in args.name:
            update_images(name)
    else:
        args.s = True
    if args.s:
        while True:
            for name in args.name:
                display_images(name, args.d)
            if not args.l:
                break

