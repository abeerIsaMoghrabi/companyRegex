
class Department(object):

    def __init__(self):
        self.__manager_id = -1
        self.__department_id = -1
        self.__department_name = ''
        self.employees = []

    def set_manager_id(self, value):
        self.__manager_id = value

    def get_manager_id(self):
        return self.__manager_id

    def set_department_id(self, value):
        self.__department_id = value

    def get_department_id(self):
        return self.__department_id

    def set_department_name(self, value):
        self.__department_name = value

    def get_department_name(self):
        return self.__department_name

