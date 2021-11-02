import pandas as pd
import json
from sqlite3 import connect

#Instinctive solution is to use a recursive sql cte pattern on a normalised parent child table
#Initial oberservations without the use of sql would mean: 
# 1. Mapping of users to roles via iteration O(n) - via array or dict iteration
# 2. Mapping of role subordinates via nested recursive function loop O(n^2) - via e.g. python set() operations / itertools list chaining
    
#Solution below opts to perform this in memory. Considerations for writing to disk can include:  
#...looking to use the 'pool' package for multi-threaded processing as well specifying an appropriate chunksize 
# ...for larger datasets to optimise write speeds to db on disk

class org_subordinates(object):
    def __init__(self): 
        pass
    
    #setter for roles
    def setRoles(self, roles):
        self.roles = roles
    
    #setter for users
    def setUsers(self, users):
        self.users = users
    
    #getter for subordinates
    def getSubOrdinates(self, user_id): 
        if self.roles:
            df_roles = pd.DataFrame(self.roles)
        else: 
            print("role data for employee organisational structure required - please load and try again")
            return None

        if self.users:
            df_users = pd.DataFrame(self.users)
        else:
            print("user data for employee information missing - please load and try again")
            return None
        
        try: 
            df_org = pd.merge(df_users,df_roles, how='outer', left_on='Role', right_on='Id')
            df_org_renamed = df_org.rename(columns={'Id_x':'Id', 'Name_x':'Name','Name_y':'role_name', 'Parent':'parent_role_id'})
            df_org_renamed.drop(columns='Id_y',inplace=True)
            #instantiate sqlite db with cursor connection in memory (NOT disk)
            conn = connect(':memory:') #sqlite3.connect()
            df_org_renamed.to_sql(name='org_hierarchy', con=conn, if_exists='replace',index=False)
            #recursive query - sql statement string - recursive on O(n log n) from whence
            qry = (
                f"""
                    with cte_emp_org_path as (
                        select Id, Name, Role, 0 as level, "" as parent_role_id, "" as level_up_manager_name
                        from org_hierarchy org_temp
                        where parent_role_id = {user_id} -- originally starting from 0. Building out entire org view from level 0 not required
                        union all
                        select org_anchor.Id, org_anchor.Name, org_anchor.Role, level + 1, org_recursive.parent_role_id, org_recursive.Name 
                        from org_hierarchy org_anchor
                        inner join cte_emp_org_path org_recursive ON org_recursive.Role = org_anchor.parent_role_id
                    )
                    select * from cte_emp_org_path
                    order by id 
                """)
            #sql execution for relevant level
            org_hierarchy = pd.read_sql_query(qry,conn)
            conn.close()
            #return result in json format for selected org level
            # result = org_hierarchy.query(f"""level == {user_id}""") #opted to put inline filter in sql query rather than build out entire org hierarchy to save on recursive cte
            return(json.loads(org_hierarchy[['Id','Name','Role']].to_json(orient='records')))
        except: 
            print("error - check input json format and key indexes")