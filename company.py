
class Company:

    def __init__(self):
        self.menu_item = "1-Search and return name and emp_number\n" + \
                         "2- Fetch any entry depending on emp_number\n" + \
                         "3-Count number of employees that have been born in some month M\n" + \
                          "4-Give employees name and number for the following query\n"
        pass

    def menu(self):

        print(self.menu_item)
        option = input("Enter number of option you want:")

        if option == 1:
            print '1'

        elif option == 2:
            print '2'

        elif option == 3:
            print '3'

        elif option == 4:
            print '4'


c = Company()

c.menu()