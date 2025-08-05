# Script to match images between two folders based on their filenames
A very common task related task during our maintenance plan is to update images in bulk on a server, usually when we receive the images they are not following the folder structure that matches the server.

This script parses two folders, one with the original images and another with the new images, and matches them based on their filenames. It then generates a report of the matched images.

## Perequisites
In order to run the script you need `python3`. Steps:

1. Install [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
2. Install the latest version of Python using `pyenv install 3.12.0`

## How to use
Just run the script in your desired terminal with the two folders as arguments:   
`python3 match_images.py "../images_original" "../images_new"`