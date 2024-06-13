class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        students.sort()
        seats.sort()

        distances = [abs(student-seat) for student, seat in zip(students, seats)]

        return sum(distances)
            
