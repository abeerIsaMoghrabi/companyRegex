import re
from Department import Department


class DepartmentRegex(object):
    """
    this class used to pares dep file and create department list
    """
    def __init__(self,text):
        self.dep_arr = [-1]*100
        self.pattern = '(\S+ ?\S*)\s+(\d+)\s+(\S+ ?\S*)'
        self.text = text

    def build_dep_list(self):
        for line in self.text:
            self.dep_line_parse(line)

    def dep_line_parse(self, line):
        """
        this function parse dep file line to create Department object
        :param line: line in dep file
        """
        rx = re.compile(self.pattern)
        groups = rx.search(line)
        new_dep = Department()
        new_dep.set_manager_id(groups.group(1))
        new_dep.set_department_id(groups.group(2))
        new_dep.set_department_name(groups.group(3))
        self.dep_arr[int(new_dep.get_department_id())] = new_dep

    def create_dep_list(self, emp_list):
        self. build_dep_list()
        for emp in emp_list:

            self.dep_arr[int(emp.get_department_id())].employees.append(emp)

    def get_my_key(self, emp):
        """
        :param emp: Employee object
        """
        return emp.get_name()

    def print_dep_arr(self):
        """
        this function print employee info in sorted way
        """
        for dep in self.dep_arr:
            if dep != -1:
                print dep.get_department_name(), " ", dep.get_department_id(), " ", dep.get_manager_id()
                dep.employees.sort(key=self.get_my_key)
                print 'employee'

                for emp in dep.employees:
                    print emp.get_name(), " ", emp.get_phone_number(), " ", emp.get_emp_number(), " ", emp.get_birth_day(), " ", emp.get_birth_day(), " ", emp.get_position()