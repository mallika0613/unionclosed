# unionclosedsets



```Installation```

​	`python setup.py install`

```Usage : ```

 `is_unionclosed(file) : returns boolean value if the sets in file are union closed`

````python
from unionclosedsets import unionclosed
# location of the file with sets as input to function
print(unionclosed.is_unionclosed(filelocation))

````

`Input file format`

-  Text file with each line respresenting a set
-  Make sure each element in the set is seperated by comma
- Empty line represents a null set
- Example file 

`````
1,2,3
1,2

3,4
1,3,4
`````



`create(set, filelocation) : create unionclosed sets from a given set of values and saves the data in the specified file location`

`````python
from unionclosedsets import unionclosed
unionclosed.create({1,2,3}, filelocation)
`````







