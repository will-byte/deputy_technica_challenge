from orgHierarchy import org_subordinates

######## Deputy Sample Inputs ########
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

######## Deputy Expected Outputs ########
test_getSubOrdinates_3 = [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 5, "Name": "Steve Trainer","Role": 5}]

test_getSubOrdinates_1 = [{"Id": 2,"Name": "Emily Employee","Role": 4}
                            ,{"Id": 3,"Name": "Sam Supervisor","Role": 3}
                                ,{"Id": 4,"Name": "Mary Manager","Role": 2}
                                     ,{"Id": 5, "Name": "Steve Trainer","Role": 5}]

######## Tests ########
if __name__ == '__main__':
    calc = org_subordinates()
    calc.setRoles(roles)
    calc.setUsers(users)
    
    if calc.getSubOrdinates(3) == test_getSubOrdinates_3: 
        print("Test 1: Passed")
    else: 
        print("Test 1: Failed")
    
    if calc.getSubOrdinates(1) == test_getSubOrdinates_1: 
        print("Test 2: Passed")
    else: 
        print("Test 2: Failed")