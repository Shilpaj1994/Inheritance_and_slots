#!/usr/bin/env python3
"""
Module containing simple object-oriented system using inheritance, method overriding, method extension, delegation, and the use of slots
"""
# Standard Library Imports
from typing import NoReturn, Literal, List


class Person:
    """
    Class containing a Person's details
    """
    def __init__(self, name: str, age: int, job: str) -> NoReturn:
        """
        Constructor
        """
        self._name = name
        self._age = age
        self._job = job
    
    @property
    def name(self):
        """
        Read only property for Person's name 
        """
        return self._name

    @property
    def age(self):
        """
        Read only property for Person's age
        """
        return self._age
    
    @property
    def job(self):
        """
        Read only property for Person's job
        """
        return self._job
    
    def get_details(self):
        """
        Method to get the Person's details
        """
        return f"Name: {self._name}, Age: {self._age}, Job: {self._job}"


class Student(Person):
    """
    Class containing Student's details
    """
    def __init__(self, name: str, age: int, job: str, grade: Literal['A', 'B']):
        """
        Constructor
        """
        super().__init__(name, age, job)
        self._grade = grade

    def grade_info(self):
        """
        Method to return grade information
        """
        return f", Grade: {self._grade}"

    def get_details(self):
        """
        Method overriding Person's get_details to include Student's grades
        """
        return super().get_details() + self.grade_info()


class Professor(Person):
    """
    Class containing Professor's details
    """
    def __init__(self, name: str, age: int, job: str, courses: List[str]):
        """
        Constructor
        """
        super().__init__(name, age, job)
        self._courses = courses
    
    def course_info(self):
        """
        Method to get the courses information
        """
        return f", Courses: {self._courses}"

    def get_details(self):
        """
        Method overriding Person's get_details to include Professor's courses
        """
        return super().get_details() + self.course_info()


class Employee(Person):
    """
    Class containing an Employee's details
    """
    def __init__(self, name: str, age: int, job: str, department: str):
        """
        Constructor
        """
        super().__init__(name, age, job)
        self._department = department
    
    def get_details(self):
        """
        Method overriding Person's get_details to include Professor's courses
        """
        return super().get_details() + f", Department: {self._department}"


class StudentProfessor(Student, Professor):
    """
    Class containing StudentProfessor's details
    """
    def __init__(self, name: str, age: int, job: str, courses: List[str], grade: Literal['A', 'B']):
        """
        Constructor
        """
        Person.__init__(self, name, age, job)
        self._grade = grade
        self._courses = courses
    
    def get_details(self):
        """
        Method overriding both parent classes to display the details
        """
        return super().get_details()


class Location:
    """
    Class containing location data
    """
    __slots__ = ["_name", "_longitude", "_latitude"]

    def __init__(self, name: str, longitude: float, latitude: float):
        """
        Constructor
        """
        self._name = name
        self._longitude = longitude
        self._latitude = latitude

    def get_coordinates(self):
        """
        Method to return coordinates
        """
        return self._longitude, self._latitude

    @property
    def name(self):
        """
        Property to get the location name
        """
        return self._name
    
    @name.setter
    def name(self, value):
        """
        Property to update the location name
        """
        self._name = value
