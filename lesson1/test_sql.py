import os
import tempfile
import unittest

import crud


class StudentDatabaseTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_db_name = sql.DB_NAME
        sql.DB_NAME = os.path.join(self.temp_dir.name, "test_school.db")
        sql.create_table()

    def tearDown(self):
        sql.DB_NAME = self.original_db_name
        self.temp_dir.cleanup()

    def test_add_and_get_student(self):
        sql.add_student("Amina", 17)

        students = sql.get_all_students()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0][1], "Amina")
        self.assertEqual(students[0][2], 17)

    def test_get_student_by_id(self):
        sql.add_student("Marko", 18)
        student_id = sql.get_all_students()[0][0]

        student = sql.get_student_by_id(student_id)

        self.assertEqual(student, (student_id, "Marko", 18))

    def test_update_student_age(self):
        sql.add_student("Sara", 16)
        student_id = sql.get_all_students()[0][0]

        sql.update_student_age(student_id, 17)

        student = sql.get_student_by_id(student_id)
        self.assertEqual(student[2], 17)

    def test_delete_student(self):
        sql.add_student("Edis", 19)
        student_id = sql.get_all_students()[0][0]

        sql.delete_student(student_id)

        self.assertEqual(sql.get_all_students(), [])
        self.assertIsNone(sql.get_student_by_id(student_id))


if __name__ == "__main__":
    unittest.main()
