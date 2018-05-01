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
* Add another column with each school's average total SAT score

### Code
```python
def getScore(school, section):
	school = school.split(",")
	if section == "math":
		section = -2
	elif section == "reading":
		section = -3
	if school[section] == "s":
		return 0
	else:
	 	return int(school[section])

def getName(school):
	school = school.split(",")
	return ",".join(school[1:-4])
	# excludes the first element and last four elements

def genReport(section):
	data = open("sats.csv", "r")
	scores = []
	topschools = []
	schools = data.readlines()[1:] # getting rid of the labels
	for school in schools:
		scores.append(getScore(school,section))

	data.close()
	x = 0
	while x < 10:
		# finds, stores, and removes school with the max score
		maxIdx = scores.index(max(scores))
		topschools.append(getName(schools[maxIdx]))
		schools.pop(maxIdx)
		scores.pop(maxIdx)
		x += 1
	return topschools

print genReport("reading")
```
