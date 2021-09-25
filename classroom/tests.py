from django.test import TestCase
from classroom.models import Student
from classroom.models import Classroom
from mixer.backend.django import mixer
import pytest
# Create your tests here.

# tells pytest not to save the data we are generaring but
# rather just hold it in memory
pytestmark = pytest.mark.django_db


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

        assert str(student_result) == 'Caleb'

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

    def test_grade_error(self):
        student1 = mixer.blend(Student, average_score=900)

        student_result = Student.objects.last()

        assert student_result.get_grade() == "Error"


##No need of passing the django default Unittest because we are using pytest
class TestClassRoomModel:
    def test_classroom_can_be_created(self):
        classroom = mixer.blend(Classroom, name='Laravel')
        classroom_result = Classroom.objects.last()

        assert str(classroom_result) == 'Laravel'
