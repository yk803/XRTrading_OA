# XRTrading_OA
Python Development Challenge @ XRTrading

## How to download the code

Open the terminal of your computer, and run the following code:

```
git clone https://github.com/yk803/XRTrading_OA.git
```

If you are working with a MacBook or Linux-based machine, you should have python installed already. No additional packages need to be installed!

If you are working with Windows, we recommend to refer [this website](https://www.python.org/downloads/windows/) for python installations.

## How to use the code

With Python installed (any version $\ge$ 2.7 is good), make sure you have the input data files in the same directory of this repo, and run the following command in terminal:

```
python report.py -t TeamMap.csv -p ProductMaster.csv\
 -s Sales.csv --team-report TeamReport.csv --product-report ProductReport.csv
```

The input arguments are: team map that stores each team's name, product master that stores each product's information, sales that store every sales record, team-report where the report by team will be stored, and product-report where report by product will be stored.

You can change the name of the files in the command above accordingly. 

E.g. If your team map file is named `team_data.csv`, just change the command to

```
python report.py -t team_data.csv -p ProductMaster.csv\
 -s Sales.csv --team-report TeamReport.csv --product-report ProductReport.csv
```

## Other Notes

Since we are given an independent task with no dataset provided, it is easier to code and comprehend by defining multiple functions for different data files. When the dataset size gets very large, a better coding-style would be to write a class of method to read and process the data. Or, we can just use powerful data processing packages like `pandas`, or use SQL if speed is the priority.
