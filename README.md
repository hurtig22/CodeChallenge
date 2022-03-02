# CodeChallenge

## Summary

CodeChallenge was created to solve an assignment, described below.

## Usage

Run Python script from shell.

```bash
python main.py <mesh file> <number of view spots>
```

<mesh file> is a filename with given data in JSON-format.
<number of view spots> The Python script will stop after finding that number of view spots and will output found view spots in descending order based on values.

## Summary of challenge

The input should be presented in JSON format containing three different lists (for nodes, elements and values) in one file. See example file in mesh.json.

- nodes are presented with their ID and x, y coordinates
- elements are presented with their ID and 3 nodeIDs which make up each element. Each element is a triangle in plane.
- values on elements: each element is presented with a value

The challenge is to find local maxima in element values and output first N view spots from highest element value to lowest element value. If we find same values among neighbors, only one element should be reported.

## Approach:

### Visualization of data

I used a Jupyter notebook (handleData.ipynb) to visualize mesh and identified local maxima. It includes all the routines from the meshed package and can be run on its own.

### Package meshed

It contains all Python scripts to solve the code challenge.

At first neighbors of all elements are identified.
1. take one element
2. find nodes of this element
3. find all other elements which have at least one node in common = neighbors of this element
4. within values of all neighbors find the maximum value
5. compare maximum value of neighbors to element value under 1. If value of element in step 1 is larger than maximum value of all neighbors this is reported as a view spot.
6. if N view spots are collected algorithm will stop
7. N view sports are sorted descending
8. output N view spots
