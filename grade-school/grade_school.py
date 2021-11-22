from collections import defaultdict
import bisect


class School:
    def __init__(self):
        self._students = defaultdict(list)

    def add_student(self, name, grade):
        # Use bisect to insert in sorted order to avoid having to sort later -
        # An expensive operation.
        bisect.insort(self._students[grade], name)

    def roster(self):
        return [student
                for grade in sorted(self._students)
                for student in self._students[grade]]

    def grade(self, grade_number):
        return self._students[grade_number]
