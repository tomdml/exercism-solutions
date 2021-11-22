plantdict = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets'
}


class Garden:
    def __init__(self, diagram, students):
        self.top, self.bottom = diagram.split('\n')
        self.students = students

    def plants(self, student):
        i = 2 * self.students.index(student)
        return [plantdict[p] for p in self.top[i:i + 2] + self.bottom[i:i + 2]]
