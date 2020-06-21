"""
The user will be able to create a TODO and assign a description, due date, and priority. Optionally, the user can assign a classroom and a class to the
TODO if it is related to academic activities. o TODOs can be classified as: Personal, Academic, Work, or Leisure. o The three possible priorities are: Urgent, Intermediate, and Optional. o TODOs should be removed when the user indicates that it was
completed.
Additionally, the app should include a tracker of the classes that the
student is taking at a college or high school.
Each class has a class code, a professor, a start time, end time, and
classroom assigned.


"""
class Subject:
    def __init__(self,class_code,professor,start_time,end_time,class_room_assigned):
        self.class_code = class_code
        self.professor = professor
        self.start_time = start_time
        self.end_time = end_time
        self.class_room_assigned = class_room_assigned

class Student_TODO:

    def __init__(self,description,due_date,priority):
        self._description = description
        self._due_date = due_date
        self._priority = priority


    def assign_description(self,new_description):
        if new_description == 'Personal':
            self._description=new_description
        elif new_description == 'Academic':
            self._description = 'Academic'
            self.subject=Subject()
        elif new_description == 'Work':
            self._description = 'Work'
        else:
            self._description = 'Leisure'

    def assign_priority(self,new_priority):
        if new_priority == 'Urgent':
            self._priority = new_priority
        elif new_priority == 'Intermediate':
            self._priority = new_priority
        elif new_priority == 'Optional':
            self._priority = new_priority

    def to_removed(self):
        del self._priority
        del self._description
        del self._due_date