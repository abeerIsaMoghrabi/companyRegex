from EmployeeRegex import EmployeeRegex
from Department import Department
import re
class Company:

    def __init__(self):
        self.menu_item = "1-Search and return name and emp_number\n" + \
                         "2-sort employee\n" + \
                         "3- Fetch any entry depending on emp_number\n" + \
                         "4-Count number of employees that have been born in some month M\n" + \
                          "5-Give employees name and number for the following query\n"
        self.text =self.read_from_file('data')
        self.emp_regex = EmployeeRegex(self.text)
        self.dep_arr = [-1, -1, -1, -1]
        self.pattern = '(\S+ ?\S*)\s+(\d+)\s+(\S+ ?\S*)'
        pass

    def read_from_file(self, filename):
        arr = []
        emp_file = open(filename, "r")
        for line in emp_file:
            arr.append(line)
        return arr

    def build_dep_list(self):
        dep_lines = self.read_from_file('dep')
        for line in dep_lines:
            self.dep_line_parse(line)

    def dep_line_parse(self, line):
        rx = re.compile(self.pattern)
        groups = rx.search(line)
        new_dep = Department()
        new_dep.set_manager_id(groups.group(1))
        new_dep.set_department_id(groups.group(2))
        new_dep.set_department_name(groups.group(3))
        self.dep_arr[int(new_dep.get_department_id())] = new_dep

    def fill_dep_arr(self):
        emp_list = self.emp_regex.create_emp_list()
        self.build_dep_list()

        for emp in emp_list:
            #print 'emp dep id:',emp.get_department_id()
            self.dep_arr[int(emp.get_department_id())].employees.append(emp)



    def menu(self):
        while True:
            print(self.menu_item)
            option = input("Enter number of option you want:")

            if option == 1:
                self.emp_regex.general_search()

            elif option == 2:
                print '2'

            elif option == 3:
                self.emp_regex.search_using_id()

            elif option == 4:
                self.emp_regex.count_emp_birth_in_m()

            elif option == 5:
                print '5'


    def print_dep_arr(self):
        for dep in self.dep_arr:
            if dep != -1 :
                print dep.get_department_name(), " ", dep.get_department_id(), " ", dep.get_manager_id()
                print 'employee'
                for emp in dep.employees:
                    print emp.get_name(), " ", emp.get_emp_number()



c = Company()
c.fill_dep_arr()
c.print_dep_arr()