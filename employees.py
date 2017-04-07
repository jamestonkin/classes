class Employee:
    """This represents an employee that can be assigned to a company"""

    def __init__(self, name, title, start_date):
        self.company_name = name
        self.title = title
        self.start_date = start_date

    def get_name(self):
        """Returns the name of the employee"""

        return self.name

    def set_name(self, name):
        """Sets the employee name"""

        self.name.add(name)

    def set_job_title(self, title):
        """Sets the employee job title"""

        self.title.add(title)

    def set_start_date(self, start_date):
        """Sets the employee start date"""

        self.start_date.add(start_date)


class Company(object):
    """This represents a company in which employees work"""

    def __init__(self, company_name):
        self.company_name = company_name
        self.employee_list = set()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def set_company_name(self, company_name):
        """Sets the name of the company"""

        self.company_name.add(company_name)

    def set_employee(self, employee):
        """Sets an employee to the companies employee list"""

        self.employee_list.add(employee)
