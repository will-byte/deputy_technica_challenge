# Deputy Technical Challenge

## Packages Required
This solution requires the `Pandas` library package. 
If you don’t already have this installed with your Python environment, run pip install in your terminal: 

```
$ pip install pandas
```

### Getting Started
1. Save the **OrgHierarchy.py** file in the same folder of your workspace
1. Import this into your script:
```
from orgHierarchy import org_subordinates
```
1. Instantiate the class object
```
example_organisation = org_subordinates()
```
1. Load organisational data as part of the deputy challenge (see appendices for Sample Inputs)
```
# load org unit roles and users
example_organisation.setRoles(roles)
example_organisation.setUsers(users)
```
1. Show a summary of subordinates using the method _getSubOrdeinates()_ for a given `User Id`
```
# Get subordinates under User Id: 1
example_organisation.getSubOrdinates(1)
```

### Tests against Deputy's Sample Inputs (see appendices)
1. Clone the repo to your workspace
```
$ git clone <github_path>
```
1. From the workspace in your terminal run: 
```
$ python tests.py
```

## Appendices
### i. Sample Input
```
roles = [ 
    {
        "Id": 1,
        "Name": "System Administrator",
        "Parent": 0
    }, 
    {
        "Id": 2,
        "Name": "Location Manager",
        "Parent": 1
    }, 
    {
        "Id": 3,
        "Name": "Supervisor",
        "Parent": 2
    }, 
    {
        "Id": 4,
        "Name": "Employee",
        "Parent": 3
    }, 
    {
        "Id": 5,
        "Name": "Trainer",
        "Parent": 3
    }]

users = [ 
    {
        "Id": 1,
        "Name": "Adam Admin",
        "Role": 1
    }, 
    {
        "Id": 2,
        "Name": "Emily Employee",
        "Role": 4
    }, 
    {
        "Id": 3,
        "Name": "Sam Supervisor",
        "Role": 3
    }, 
    {
        "Id": 4,
        "Name": "Mary Manager",
        "Role": 2
    }, 
    {
        "Id": 5,
        "Name": "Steve Trainer",
        "Role": 5
    }]
```
### ii. Expected outputs
```
getSubOrdinates(3) = [{"Id": 2,"Name": "Emily Employee","Role": 4}
                        ,{"Id": 5, "Name": "Steve Trainer","Role": 5}]

getSubOrdinates(1) = [{"Id": 2,"Name": "Emily Employee","Role": 4}
                            ,{"Id": 3,"Name": "Sam Supervisor","Role": 3}
                                ,{"Id": 4,"Name": "Mary Manager","Role": 2}
                                     ,{"Id": 5, "Name": "Steve Trainer","Role": 5}]
```
