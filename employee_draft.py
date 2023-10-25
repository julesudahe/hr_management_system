"""AndrewID: judahemu"""

class Employee:
    """This class have five main attributes first name, last name, email, employee_id, and salary:
        first name (str): The first name of the employee.
        last name (str): The last name of the employee.
        email (str): Official email of the employee (FORMAT: first_name.last_name@andrew.cmu.edu).
        salary (int): The salary of the employee.
        gender (str): The gender of the employee.
        employee_id (str): The employee_id that is generate automatically by the system.

    The class has many methods but most of them are setters 
    and getters that we will be used mostly by child classes 
    """

    __last_employee_id = 0
    
    def __init__(self, first_name, last_name, employee_gender, salary):
        """Initializing the attributes of this class"""

        # exception handling to make sure that the program does not clash
        if not first_name or not last_name or not employee_gender or salary < 0:
            raise ValueError("Name cannot be empty or Salary is less than zero.")
        
        self._first_name = first_name
        self._last_name = last_name
        self._employee_gender = employee_gender
        self._email = self.generate_email(first_name, last_name)
        self.__salary = salary
        self.__employee_id = self.generate_employee_id()
    
    @classmethod
    def generate_employee_id(cls):
        """Generate automatically the employee ID"""
        employee_id = f"CMUID{cls.__last_employee_id + 1:04}"
        cls.__last_employee_id += 1
        return employee_id
    
    @staticmethod
    def generate_email(first_name, last_name):
        """Generate automatically the email based on first name and last name"""
        return f"{first_name.lower()}.{last_name.lower()}@andrew.cmu.edu"

    def get_full_name(self):
        """Getter to combine the first and last name"""
        return self._first_name + " " + self._last_name

    def get_email(self):
        """Getter for email"""
        return self._email

    def get_salary(self):
        """Getter for salary"""
        return self.__salary

    def get_employee_id(self):
        """Getter for employee_id"""
        return self.__employee_id

    def get_gender(self):
        """Getter for gender"""
        return self._employee_gender

    def show_employee_info(self):
        """Build the print function for this class"""
        print(f'EmployeeID: {self.get_employee_id()}')
        print(f'Full Name: {self.get_full_name()}')
        print(f'Email: {self.get_email()}')
        print('Position: Employee')
        print(f'Gender: {self.get_gender()}')
        print(f'Salary: {self.get_salary():.2f}')
