# creates a table of colleges and the ap credit they take

you can load the csv(catted.csv) file into google sheets or microsoft excel

look at the code for additional functions that you can use in terminal python repl for easy searching

all data retrieved from collegeboard find credit database(https://apstudents.collegeboard.org/getting-credit-placement/search-policies/course)

in python terminal you can do: 

```python 
from processor import *
```
and use the built in functions to search by college or ap class

too lazy to document search functions hehe just look at `processor.py`

to add more college data go to the collegeboard credit database and download csv file of the table. then move the file to ./data and run `python processor.py` again to update `catted.csv`
