
class Employee(object):
    def __init__(self):
        self.name = ''
        self.phone_number = ''
        self.emp_number = -1
        self.birth_day = ''
        self.position = ''
        self.manager_id = -1
        self.department_id = -1
        pass

    def set_name(self, value):
        self.name = value

    def get_name(self):
        return self.name

    def set_phone_number(self, value):
        self.phone_number = value

    def get_phone_number(self):
        return self.phone_number

    def set_emp_number(self, value):
        self.emp_number = value

    def get_emp_number(self):
        return self.emp_number

    def set_birth_day(self, value):
        self.birth_day = value

    def get_birth_day(self):
        return self.birth_day

    def set_position(self, value):
        self.position = value

    def get_position(self):
        return self.position

    def set_manager_id(self, value):
        self.manager_id = value

    def get_manager_id(self):
        return self.manager_id

    def set_department_id(self, value):
        self.department_id = value

    def get_department_id(self):
        return self.department_id

    # name = property(set_name, get_name)
    # phone_number = property(set_phone_number, get_phone_number)
    # emp_number = property(set_emp_number, get_emp_number)
    # birth_day = property(set_birth_day, get_birth_day)
    # position = property(set_position, get_position)
    # manager_id = property(set_manager_id, get_manager_id)
    # department_id = property(set_department_id, get_department_id)
