import re


class Employee(object):

    def __init__(self):
        self.menu_item = "1-name \n" + \
                    "2-phone_number \n" + \
                    "3-emp_number\n" + \
                    "4-birth_day\n" + \
                    "5-phone_number \n" + \
                    "6-emp_number\n" + \
                    "7-birth_day\n"

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
        arr = self.token_arr

        arr[code] = '(?:' + value + ')'

        all_token = '('+arr[0]+')'
        for item in arr[1:]:
            all_token = all_token + self.token['spaces'] + '('+item+')'
        return all_token

    def general_search(self):
        print "enter value you want search"
        print(self.menu_item)

        option = input("Enter number of option you want:")
        value = raw_input("Plz txt:")

        self.search(option-1, [1, 3], value)

    def search_using_id(self):
        print "enter the field you want"
        print(self.menu_item)

        option = input("Enter number of option you want:")
        value = raw_input("id value:")

        self.search(2, [option], value)

    def search(self, code, group_num, value):

        rx = re.compile(r'' + self.create_pattern(value, code))

        emp_file = open('data', "r")

        for line in emp_file:
            grp = rx.search(line)

            if grp != None:
                print_group = ""
                for num in group_num:
                    print_group = print_group + "  " + grp.group(num)
                print print_group


e = Employee()
e.search_using_id()
