import re
from Department import Department


class ReadR(object):
    def __init__(self):
        self.dep_arr = []
        self.key_arr = []
        pass

    def add_dep(self, dep):
        new_dep = Department()
        new_dep.set_manager_id(dep['manager_id '])
        new_dep.set_department_id(dep['manager_id '])
        new_dep.set_department_name(dep['department_name'])
        return new_dep


    def parse_line(self, count, line):
        rx = re.compile(r'\S+ ?\S*')
        if count == 0:
            self.key_arr = rx.findall(line)

        else:
            array = rx.findall(line)
            dep = dict(zip(self.key_arr, array))
            self.dep_arr.append(self.add_dep(dep))


    def pares_file(self, filename):

        file = open(filename, "r")
        count = 0
        for line in file:
            if count == 0:
                self.parse_line(count, line)
                count = count+1

            else:
                self.parse_line(count, line)














r = ReadR()
r.pares_file('dep')
print(r.dep_arr[0].get_department_name())