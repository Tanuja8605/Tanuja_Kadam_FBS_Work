from Emp import Emp

class Trainer(Emp):

    def __init__(self, emp_id, name, sal, bonus):
        super().__init__(emp_id, name, sal)
        self.bonus = bonus

    def cal_sal(self):
        return self.sal + self.bonus
        

    def __str__(self):
        return f"id:{self.emp_id}\tname:{self.name}\tfinal_sal:{self.cal_sal()}"

    def __repr__(self):
        return self.__str__()