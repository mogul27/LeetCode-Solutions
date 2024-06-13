class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        distance_counter = 0
        students.sort()
        seats.sort()
        new_list = zip(students,seats)

        distances = [abs(student-seat) for student, seat in zip(students, seats)]

        return sum(distances)
