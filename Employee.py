
class Employee(object):
    def __init__(self):
        self.__name = ''
        self.__phone_number = ''
        self.__emp_number = -1
        self.__birth_day = ''
        self.__position = ''
        self.__manager_id = -1
        self.__department_id = -1

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def set_phone_number(self, value):
        self.__phone_number = value

    def get_phone_number(self):
        return self.__phone_number

    def set_emp_number(self, value):
        self.__emp_number = value

    def get_emp_number(self):
        return self.__emp_number

    def set_birth_day(self, value):
        self.__birth_day = value

    def get_birth_day(self):
        return self.__birth_day

    def set_position(self, value):
        self.__position = value

    def get_position(self):
        return self.__position

    def set_manager_id(self, value):
        self.__manager_id = value

    def get_manager_id(self):
        return self.__manager_id

    def set_department_id(self, value):
        self.__department_id = value

    def get_department_id(self):
        return self.__department_id

    # name = property(set_name, get_name)
    # phone_number = property(set_phone_number, get_phone_number)
    # emp_number = property(set_emp_number, get_emp_number)
    # birth_day = property(set_birth_day, get_birth_day)
    # position = property(set_position, get_position)
    # manager_id = property(set_manager_id, get_manager_id)
    # department_id = property(set_department_id, get_department_id)
