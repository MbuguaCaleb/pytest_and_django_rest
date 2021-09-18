from django.test import TestCase
from classroom.models import Student
# Create your tests here.


class TestStudentModel(TestCase):

    # Helps me avoid repeated code when writing Tests
    def setUp(self):
        # i am defining obj as property of the class
        self.student1 = Student.objects.create(
            first_name='Caleb',
            last_name='Mbugua',
            admission_number=7552
        )

    def test_add_a_plus_b(self):
        a = 1
        b = 2
        c = a+b

        self.assertEqual(c, 3)

    # test if model can be created
    def test_student_can_be_created(self):
        self.assertEqual(self.student1.first_name, 'Caleb')

    # test the str method
    def test_str_return(self):
        self.assertEqual(str(self.student1), "Caleb")

    def test_grade_fail(self):
        Student.objects.create(
            first_name='Caleb',
            last_name='Mbugua',
            admission_number=7556,
            average_score=10
        )

        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Fail")

    def test_grade_pass(self):
        Student.objects.create(
            first_name='Caleb',
            last_name='Mbugua',
            admission_number=7551,
            average_score=60
        )

        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Pass")

    def test_grade_excellent(self):
        Student.objects.create(
            first_name='Caleb',
            last_name='Mbugua',
            admission_number=7550,
            average_score=90
        )

        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Excellent")
