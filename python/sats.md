## Processing Data from a CSV File

### CSV
* each row is delineated by a `\n`
* each column is marked by a comma

### Setup
1. Download the NYC 2012 SAT data [here](https://data.cityofnewyork.us/Education/2012-SAT-Results/f9bf-2cp4).
2. Export the data as a `.csv` file.
3. Convert the file into an array by using the `.readlines()` method.
4. Each row of the `.csv` file will be an element in the array produced by the `.readlines()` method.
5. Separate out the columns by calling the `.split()` on each element. This will produce another array.

### Activity
You can use the `.sort()` method.
* Find the 10 schools that had the highest Math scores
* Find the 10 schools that had the highest Writing scores
* Find the 10 schools that had the highest Reading scores
* Add another column with each school's average total SAT score
