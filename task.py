class Task:
    def __init__(self, title, completed=False):
        self.title=title
        self.completed=completed
    
    #mark the task as completed
    def mark_completed(self): 
        self.completed=True

    #convert the task to a dictionary
    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }

    #create a task from a dictionary
    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["completed"])

