# AStarTesting

## Description
Just playing around with A star using python.

## Current Features
- Can read in a map text file (see map layout)
- Vertical and horizontal movement
- unpassable walls

## Features to add / work on
- Diagonal movement
- Different terrain costs
- Optimized data structures for the open / closed lists

## Map Layout
- First line is 2 numbers separated by a space: the width and height
- The next height lines are characters representing the map with the following key:
    * 'S' for start
    * 'F' for finish/goal
    * 'W' for wall
    * '1' for walkable space (eventually will be the cost to move to the space, but thats not implemented yet)
