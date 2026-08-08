from Emp import Emp

class Hr(Emp):

    def __init__(self, emp_id, name, sal, com):
        super().__init__(emp_id, name, sal)
        self.com = com

    def cal_sal(self):
        return self.sal + self.com

    def __str__(self):
     return f"id:{self.emp_id}\tname:{self.name}\tfinal_sal:{self.cal_sal()}"

    def __repr__(self):
        return self.__str__()