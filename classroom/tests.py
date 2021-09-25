from django.test import TestCase
from classroom.models import Student
from mixer.backend.django import mixer
# Create your tests here.


class TestStudentModel(TestCase):

    # Helps me avoid repeated code when writing Tests
    # def setUp(self):
    #     # i am defining obj as property of the class
    #     self.student1 = Student.objects.create(
    #         first_name='Caleb',
    #         last_name='Mbugua',
    #         admission_number=7552
    #     )

    def test_add_a_plus_b(self):
        a = 1
        b = 2
        c = a+b

        #self.assertEqual(c, 3)
        assert c == 3

    # test if model can be created
    def test_student_can_be_created(self):
        student1 = mixer.blend(Student, first_name='Caleb')
        student_result = Student.objects.last()

        assert student_result.first_name == 'Caleb'

    # test the str method
    def test_str_return(self):
        student1 = mixer.blend(Student, first_name='Caleb')
        student_result = Student.objects.last()
        # self.assertEqual(student_result.first_name, "Caleb")
        assert student_result.first_name == "Caleb"


    def test_grade_fail(self):
        student1 = mixer.blend(Student, average_score=10)
        student_result = Student.objects.last()
        assert student_result.get_grade() == "Fail"

    def test_grade_pass(self):
        student1 = mixer.blend(Student, average_score=60)

        student_result = Student.objects.last()
        assert student_result.get_grade() == "Pass"

    def test_grade_excellent(self):
        student1 = mixer.blend(Student, average_score=90)

        student_result = Student.objects.last()

        assert student_result.get_grade() == "Excellent"
