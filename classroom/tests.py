from django.test import TestCase
from classroom.models import Student
# Create your tests here.


class TestStudentModel(TestCase):

    def test_add_a_plus_b(self):
        a = 1
        b = 2
        c = a+b

        self.assertEqual(c, 3)

    # test if model can be created
    def test_student_can_be_created(self):
        Student.objects.create(
            first_name='Caleb',
            last_name='Mbugua',
            admission_number=7559
        )

       # getting last student
        student_result = Student.objects.last()

        self.assertEqual(student_result.first_name, 'Caleb')

    # test the str method
    def test_str_return(self):
        Student.objects.create(
            first_name='Caleb',
            last_name='Mbugua',
            admission_number=7559
        )

        # getting last student
        student_result = Student.objects.last()

        self.assertEqual(str(student_result), "Caleb")

    def test_grade_fail(self):
        Student.objects.create(
            first_name='Caleb',
            last_name='Mbugua',
            admission_number=7559,
            average_score=10
        )

        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Fail")

    def test_grade_pass(self):
        Student.objects.create(
            first_name='Caleb',
            last_name='Mbugua',
            admission_number=7559,
            average_score=60
        )

        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Pass")
    
    def test_grade_excellent(self):
        Student.objects.create(
        first_name='Caleb',
        last_name='Mbugua',
        admission_number=7559,
        average_score=90
        )

        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Excellent")
