import os
import tempfile
import unittest

import crud


class StudentDatabaseTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_db_name = crud.DB_NAME
        crud.DB_NAME = os.path.join(self.temp_dir.name, "test_school.db")
        crud.create_table()

    def tearDown(self):
        crud.DB_NAME = self.original_db_name
        self.temp_dir.cleanup()

    def test_add_and_get_student(self):
        crud.add_student("Amina", 17)

        students = crud.get_all_students()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0][1], "Amina")
        self.assertEqual(students[0][2], 17)

    def test_get_student_by_id(self):
        crud.add_student("Marko", 18)
        student_id = crud.get_all_students()[0][0]

        student = crud.get_student_by_id(student_id)

        self.assertEqual(student, (student_id, "Marko", 18))

    def test_update_student_age(self):
        crud.add_student("Sara", 16)
        student_id = crud.get_all_students()[0][0]

        crud.update_student_age(student_id, 17)

        student = crud.get_student_by_id(student_id)
        self.assertEqual(student[2], 17)

    def test_delete_student(self):
        crud.add_student("Edis", 19)
        student_id = crud.get_all_students()[0][0]

        crud.delete_student(student_id)

        self.assertEqual(crud.get_all_students(), [])
        self.assertIsNone(crud.get_student_by_id(student_id))


if __name__ == "__main__":
    unittest.main()
