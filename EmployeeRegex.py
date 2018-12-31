import re
from Employee import Employee

class EmployeeRegex(object):

    def __init__(self, text):
        self.menu_item = "1-name \n" + \
                    "2-phone_number \n" + \
                    "3-emp_number\n" + \
                    "4-birth_day\n" + \
                    "5-position \n" + \
                    "6-manager_id\n" + \
                    "7-department_id\n"

        self.token = {'name': '\S+ ?\S*',
                      'phone_number': '\d{10,10}',
                      'number': '\d+',
                      'birth_day': '([1-9] |1[0-9]| 2[0-9]|3[0-1])-([1-9] |1[0-2])',
                      'spaces': '\s+'
                      }
        self.token_arr = [self.token['name'],
                          self.token['phone_number'],
                          self.token['number'],
                          self.token['birth_day'],
                          self.token['name'],
                          self.token['number'],
                          self.token['number']]


        self.text = text

        pass

    def create_pattern(self, value, code):
        arr = self.token_arr[:]

        arr[code] = value

        all_token = '('+arr[0]+')'
        for item in arr[1:]:
            all_token = all_token + self.token['spaces'] + '('+item+')'
        del arr
        return all_token

    def general_search(self):
        print "enter value you want search"
        print(self.menu_item)

        option = input("Enter number of option you want:")
        value = raw_input("Plz txt:")
        value = '(?:' + value + ')'
        print self.search(option-1, [1, 3], value)

    def search_using_id(self):
        print "enter the field you want"
        print(self.menu_item)

        option = input("Enter number of option you want:")
        value = raw_input("id value:")
        value = '(?:' + value + ')'
        if option > 4:
            option = option+2
        print self.search(2, [option], value)

    def search(self, code, group_num, value):
        result_arr = []
        rx = re.compile(r'' + self.create_pattern(value, code))

        for line in self.text:
            grp = rx.search(line)

            if grp != None:
                print_group = ""
                for num in group_num:
                    print_group = print_group + "  " + grp.group(num)

                result_arr.append(print_group)
        return result_arr

    def count_emp_birth_in_m(self):
        month = raw_input("Plz enter the month:")
        date_reg = '([1-9] |1[0-9]| 2[0-9]|3[0-1])-'+month

        print self.search(3, [4], date_reg).__len__()

    def search_for_position(self):
        value = raw_input('Enter the postion you want:')
        op = input('Enter 1 for positive and 0 for negative:')

        if op == 0:
            value = '((?!' + value + ').)*'

        else:
            value = '(?:' + value + ')'

        print self.search(4, [1, 3], value)


    def create_emp_list(self):
        emp_list = []
        all_token = '(' + self.token_arr[0] + ')'
        for item in self.token_arr[1:]:
            all_token = all_token + self.token['spaces'] + '(' + item + ')'

        rx = re.compile(r'' + all_token)
        for line in self.text:
            grp = rx.search(line)

            if grp != None:
                new_emp = Employee()
                new_emp.set_name(grp.group(1))
                new_emp.set_phone_number(grp.group(2))
                new_emp.set_emp_number(grp.group(3))
                new_emp.set_birth_day(grp.group(4))
                new_emp.set_position(grp.group(7))
                new_emp.set_manager_id(grp.group(8))
                new_emp.set_department_id(grp.group(9))
                emp_list.append(new_emp)
                # print grp.group(1)
                # print grp.group(2)
                # print grp.group(3)
                # print grp.group(4)
                # print grp.group(7)
                # print grp.group(8)
                # print grp.group(9)


        return emp_list
















