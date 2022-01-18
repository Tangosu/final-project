# Project Prototype
https://github.com/Tangosu/final-project
## What it does
Using a short video of the game to detect the moving arrows in the bottom right of the screen and counts them. Only need to run the main.py.

## Current Progress
- Able to detect moving objects within a small area i.e. bottom right of the screen
- Able to identify the number of unique moving objects, although not correctly. The total number of moving object should have been 31, but only 29 are counted.
- Enters the mid point of the contour in an array

##Future direction
- Fix the counter. May not actually need the counter as it was used as a visual aid. The actual detection of the arrow was correctly identified.
- Use the mid point to represent the arrows. 
- Create different patterns using coordinates 
- Loop through the unique_obj array and check if any of the coordinates matches the pattern coordinates in order.
- Count the amount of times different patterns appears.
- Apply weighting to different patterns
- Test on different videos