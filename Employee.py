import re


class Employee(object):

    def __init__(self):
        self.name = ''
        self.phone_number = ''
        self.emp_number = -1
        self.birth_day = ''
        self.position = ''
        self.manager_id = -1
        self.department_id = -1

        self.token = {'name': '\S+ ?\S*',
                      'phone_number': '\d{10,10}',
                      'number': '\d+',
                      'birth_day': '[12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[0]',
                      'spaces': '\s+'
                      }
        self.token_arr = [self.token['name'],
                          self.token['phone_number'],
                          self.token['number'],
                          self.token['name'],
                          self.token['name'],
                          self.token['number'],
                          self.token['number']]

        pass

    def create_pattern(self, value, code):
        arr = self.token_arr;

        arr[code] = '(?:' + value + ')'

        all_token = '('+arr[0]+')'
        for item in arr[1:]:
            all_token = all_token + self.token['spaces'] + '('+item+')'
        return all_token

    def general_search(self):

        menu_item = "1-Search by name \n" + \
                    "2-Search by phone_number \n" + \
                    "3-Search by emp_number\n" + \
                    "4-Search by birth_day\n" + \
                    "5-Search by phone_number \n" + \
                    "6-Search by emp_number\n" + \
                    "7-Search by birth_day\n"
        print(menu_item)

        option = input("Enter number of option you want:")

        if option == 1:
            self.search(0)

        elif option == 2:
            self.search(1)

        elif option == 3:
            self.search(2)

        elif option == 4:
            self.search(3)

        elif option == 5:
            self.search(4)

        elif option == 6:
            self.search(5)

        elif option == 7:
            self.search(6)

    def search(self, code):

        name = raw_input("Plz txt:")

        rx = re.compile(r'' + self.create_pattern(name, code))

        emp_file = open('data', "r")

        for line in emp_file:
            grp = rx.search(line)

            if grp != None:

                print grp.group(1), grp.group(3)







e = Employee()
e.general_search()
