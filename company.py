from EmployeeRegex import EmployeeRegex
from DepartmentRegex import DepartmentRegex

class Company:

    def __init__(self):
        self.menu_item = "1-Search and return name and emp_number\n" + \
                         "2-sort employee\n" + \
                         "3- Fetch any entry depending on emp_number\n" + \
                         "4-Count number of employees that have been born in some month M\n" + \
                          "5-Give employees name and number for the following query\n"

        self.emp_regex = EmployeeRegex(self.read_from_file('data'))
        self.dep_regex = DepartmentRegex(self.read_from_file('dep'))
        self.dep_array = []
        self.fill_dep_arr()
        pass

    def read_from_file(self, filename):
        arr = []
        emp_file = open(filename, "r")
        for line in emp_file:
            arr.append(line)
        return arr

    def fill_dep_arr(self):
        self.dep_array = self.dep_regex.create_dep_list(self.emp_regex.create_emp_list())

    def menu(self):
        while True:
            print(self.menu_item)
            option = input("Enter number of option you want:")

            if option == 1:
                self.emp_regex.general_search()

            elif option == 2:
                self.print_dep_arr()

            elif option == 3:
                self.emp_regex.search_using_id()

            elif option == 4:
                self.emp_regex.count_emp_birth_in_m()

            elif option == 5:
                self.emp_regex.search_for_position()

    def print_dep_arr(self):
        for dep in self.dep_array:
            if dep != -1:
                print dep.get_department_name(), " ", dep.get_department_id(), " ", dep.get_manager_id()
                print 'employee'
                for emp in dep.employees:
                    print emp.get_name(), " ", emp.get_emp_number()



c = Company()
c.menu()

