## Files
Each operating system comes with its own filesystem for creating and accessing files. Python achieves operating system independence by accessing files through a file handle.

## Writing
If the mode information is write - it'll overwrite the previous contents of the file.
```python
filehandle = open('colleges.txt', 'w')
for i in range(2):
  name = raw_input("Enter a college:")
  filehandle.write(name + '\n')
```
Instructs the operating system to create a file named `colleges.txt` and return a file handle to that file. the `w` argument indicates that the file is to be opened for writing.

## Reading
```python
filehandle = open('colleges.txt', 'r')
for line in filehandle:
    print line # have to remove the `\n`
```

## Appending
```python
filehandle = open('colleges.txt', 'a')
file.write('Duke\n')
file.write('UNC\n')
```

Important, a programmer should remember to close any files that is opened.
```python
filehandle.close()
```
