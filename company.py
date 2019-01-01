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
        self.fill_dep_arr()

    def read_from_file(self, filename):
        """

        :param filename: the name of file we want to read
        :return: file content
        """
        st = ""
        emp_file = open(filename, "r")
        for line in emp_file:
            st = st+line
        return st

    def fill_dep_arr(self):
        """
        this function call function in DepartmentRegex class
        """
        self.dep_regex.create_dep_list(self.emp_regex.create_emp_list())

    def menu(self):
        while True:
            print(self.menu_item)
            option = input("Enter number of option you want:")

            if option == 1:
                self.emp_regex.general_search()

            elif option == 2:
                self.dep_regex.print_dep_arr()

            elif option == 3:
                self.emp_regex.search_using_id()

            elif option == 4:
                self.emp_regex.count_emp_birth_in_m()

            elif option == 5:
                self.emp_regex.search_for_position()


c = Company()
c.menu()

