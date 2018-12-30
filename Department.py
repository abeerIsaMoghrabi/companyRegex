
class Department(object):

    def __init__(self):
        self.manager_id = -1
        self.department_id = -1
        self.department_name = ''
        self.employees = []
        pass

    def set_manager_id(self, value):
        self.manager_id = value

    def get_manager_id(self):
        return self.manager_id

    def set_department_id(self, value):
        self.department_id = value

    def get_department_id(self):
        return self.department_id

    def set_department_name(self, value):
        self.department_id = value

    def get_department_name(self):
        return self.department_id

