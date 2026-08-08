from abc import ABC,abstractmethod
class Emp(ABC):
  def __init__(self,emp_id,name,sal):
    self.emp_id = emp_id
    self.name = name
    self.sal = sal
  @abstractmethod
  def cal_sal():
    pass
  def __str__(self):
    return f"id :{self.emp_id}\tname: {self.name}\tsalary: {self.sal}"
  def __repr__(self):
    return super().__str__()
  


