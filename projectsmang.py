import authandlogin as us
import datetime
import json
class Projects:
    projects=[]
    def __init__(self,title,details,total_target,start_time,end_time,uid):
        self.title=title
        self.details=details
        self.total_target=total_target
        self.start_time = start_time
        self.end_time = end_time

        self.uid=uid
        self.save_project("projects.txt")

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        try:
            datetime.datetime.strptime(start_time, "%Y-%m-%d")
            self._start_time = start_time
        except ValueError:
            raise ValueError("Invalid start date format")

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        try:
            datetime.datetime.strptime(end_time, "%Y-%m-%d")
            self._end_time = end_time
        except ValueError:
            raise ValueError("Invalid end date format")

    def save_project(self,filename):
        project_data = {
            "title": self.title,
            "details": self.details,
            "total_target": self.total_target,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "uid": self.uid
        }
        self.projects.append(project_data)
#        projects = dict()
 #       projects["title"]=self.title
  #      projects["details"] = self.details
   #     projects["total_target"] = self.total_target
    #    projects["start_time"] = self.start_time
     #   projects["end_time"] = self.end_time
      #  projects["uid"] = self.uid
       # self.projects.append(str(projects))
        with open(filename, 'w') as file:
            for project in self.projects:
                json.dump(project, file)
                file.write("\n")
        #with open(filename,'w') as file:
         ##      file.write(str(item) + "\n")
    @classmethod
    def view_projects(cls):
        fhandle= open("projects.txt")
        for line in fhandle:
            print(line.rstrip())
    def edit_project(self,userid):
        new_projects = []
        with open("projects.txt", "r") as file:
            for line in file:
                project_data = json.loads(line)
                if project_data["uid"] == userid:
                    project_data["title"] = input("Enter new title: ")
                    project_data["details"] = input("Enter new details: ")
                new_projects.append(project_data)

        with open("projects.txt", "w") as file:
            for project_data in new_projects:
                json.dump(project_data, file)
                file.write("\n")

        self.projects = new_projects

      #  if self.uid==userid:
       #     self.title=input("enter new title ")
        #    self.details=input("change details ")
         ##  self.save_project("projects.txt")









