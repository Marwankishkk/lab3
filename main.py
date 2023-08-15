import authandlogin as us
import projectsmang as proj
import re
import json

u10=us.User("nour","n@gmail.com","afsa","+201026990431")
u11=us.User("nadem","n@gmail.com","afsa","+201026990431")
print(u11.id)
print(u10.id)
p2=proj.Projects("sec","to help people","20000","2023-08-01", "2023-09-01",int(u11.id))
p1=proj.Projects("First","to help people","20000","2023-08-01", "2023-09-01",int(u10.id))
proj.Projects.view_projects()
print(p1.start_time)

p1.edit_project(int(u10.id))