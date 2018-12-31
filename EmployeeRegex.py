import re
from Employee import Employee


class EmployeeRegex(object):

    """  parse string list using regex to:
        1- search for specific value (parts : 1, 3, 4, 5)
        2- create employee list
    """

    def __init__(self, text):
        """
        :param text: file content
        :type text: string list

        menu_item: contain employee info as list to let users select one of them by entering  number

        token: contain regex used to find each field eg. name, birth day ...etc

        token_arr: it contain sequence of token that represent one raw in data file i but them in list because if i want
        to search for specific  value eg emp number i will just change element 3 and leave other the same

        """
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


    def create_pattern(self, value, code):
        """
        :param value: searched value eg. value=Abeer (search for employee with name = Abeer)
        :param code: index in token array (index i went to replace with value)
        :return: new token after replace value
        """
        arr = self.token_arr[:]
        arr[code] = value
        all_token = '('+arr[0]+')'
        for item in arr[1:]:
            all_token = all_token + self.token['spaces'] + '('+item+')'
        del arr
        return all_token

    def general_search(self):
        """
        this function display menu to let user choose from it and enter the value want

        """
        print "enter value you want search"
        print(self.menu_item)

        option = input("Enter number of option you want:")
        value = raw_input("Plz txt:")
        value = '(?:' + value + ')'
        print self.search(option-1, [1, 3], value)

    def search_using_id(self):
        """
        this function to display employee info according to user selection and id value

        """
        print "enter the field you want"
        print(self.menu_item)

        option = input("Enter number of option you want:")
        value = raw_input("id value:")
        value = '(?:' + value + ')'
        if option > 4:
            option = option+2
        print self.search(2, [option], value)

    def search(self, code, group_num, value):
        """
        :param code: index in token array (index i went to replace with value)
        :param group_num: list of group number that we want to display
        :param value: value to search for
        :return: searched result
        """
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
        """
        this function to count number of employees that born in specific month

        """
        month = raw_input("Plz enter the month:")
        date_reg = '([1-9] |1[0-9]| 2[0-9]|3[0-1])-'+month

        print self.search(3, [4], date_reg).__len__()

    def search_for_position(self):

        """
        display name and number according to position value, this function has two option
        1- display all employee with that position
        2- display all employee with other position
        """
        value = raw_input('Enter the postion you want:')
        op = input('Enter 1 for positive and 0 for negative:')

        if op == 0:
            value = '((?!' + value + ').)*'

        else:
            value = '(?:' + value + ')'

        print self.search(4, [1, 3], value)

    def create_emp_list(self):
        """
        this function parse file content to create employee list
        :return: list contain objects of type employee
        """
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

        return emp_list
















