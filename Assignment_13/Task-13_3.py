"""Refactored Student class with improved naming, docstrings, and helpers.

This module defines a `Student` class that stores a student's `name`,
`age`, and `marks` (as a list). It provides methods to print details,
compute the total and average, and a readable string representation.
"""
from typing import List


class Student:
    """Represent a student with name, age and marks.

    Attributes:
        name: Student's full name.
        age: Student's age (int).
        marks: List of numeric marks (floats or ints).
    """

    def __init__(self, name: str, age: int, marks: List[float]):
        self.name = name
        self.age = int(age)
        # store marks as a list for easy sum()/len()
        self.marks = [float(m) for m in marks]

    def details(self) -> None:
        """Print the student's basic details in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def total(self) -> float:
        """Return the sum of the student's marks."""
        return sum(self.marks)

    def average(self) -> float:
        """Return the average mark; returns 0.0 if no marks are present."""
        return self.total() / len(self.marks) if self.marks else 0.0

    def __str__(self) -> str:
        return (
            f"Student(name={self.name!r}, age={self.age}, "
            f"marks={self.marks}, total={self.total()}, average={self.average():.2f})"
        )


if __name__ == "__main__":
    # Demo showing usage
    s = Student("Alice Smith", 16, [78, 85, 91])
    s.details()
    print(f"Marks: {s.marks}")
    print(f"Total: {s.total()}")
    print(f"Average: {s.average():.2f}")
    print()  # blank line
    print(s)
