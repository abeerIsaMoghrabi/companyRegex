import re
from Department import Department


class DepartmentRegex(object):

    def __init__(self,text):
        self.dep_arr = [-1, -1, -1, -1]
        self.pattern = '(\S+ ?\S*)\s+(\d+)\s+(\S+ ?\S*)'
        self.text = text
        pass

    def build_dep_list(self):
        for line in self.text:
            self.dep_line_parse(line)

    def dep_line_parse(self, line):
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
            #print 'emp dep id:',emp.get_department_id()
            self.dep_arr[int(emp.get_department_id())].employees.append(emp)

        return self.dep_arr