import unittest
from Connection import *


class MyTest(unittest.TestCase):
    check = Staff()
    room = Room()
    book = Booking()

    def test_register1(self):
        result = self.check.register(None, '1234567890', 'Diptan Regmi', '1999-04-30', 'ale', 'Kathmandu',
                                     '9818133208', 'drt347826@gmail.com', 'Admin')
        self.assertFalse(result)

    def test_register2(self):
        result = self.check.register('diptan', '1234567890', 'Diptan Regmi', '1999-04-30', 'ale', 'Kathmandu',
                                     '9818133208', 'drt347826@gmail.com', 'Admin')
        self.assertFalse(result)

    def test_register3(self):
        result = self.check.register('diptan', '1234567890', 'Diptan Regmi', '1999-04-30', 'Male', 'Kathmandu',
                                     '9818133208', 'drt347826@gmail.com', 'Admin')
        self.assertTrue(result)

    def test_register4(self):
        result = self.check.register('employee', 'asdfghjkl', 'Front Desk', '2000-12-31', 'Female', 'Kathmandu',
                                     '1234567890', None, 'User')
        self.assertTrue(result)

    def test_login1(self):
        actual_result = self.check.login('diptan', '1234567890')
        expected_result = 1
        self.assertEqual(expected_result, len(actual_result))

    def test_login2(self):
        actual_result = self.check.login('user', 'aaaaa')
        expected_result = []
        self.assertEqual(expected_result, actual_result)

    def test_login3(self):
        actual_result = self.check.login(None, None)
        expected_result = []
        self.assertEqual(expected_result, actual_result)

    def test_create_room1(self):
        result = self.room.create_rooms(None, 'Single Deluxe', 'AC', '4500')
        self.assertFalse(result)

    def test_create_room2(self):
        result = self.room.create_rooms('900', 'Single Deluxe', 'AC', '4500')
        self.assertTrue(result)

    def test_create_room3(self):
        result = self.room.create_rooms('901', 'Single Deluxe', 'AC', 5000)
        self.assertTrue(result)

    def test_show_rooms1(self):
        actual_result = self.room.show_rooms()
        expected_result = 1
        self.assertLessEqual(expected_result, len(actual_result))

    def test_new_booking1(self):
        result = self.book.new_booking('Diptan Regmi', '9818133208', 'Kathmandu', 'drt347826@gmail.com',
                                       '2020-1-1', '2020-2-2', None, 1, 0)
        self.assertFalse(result)

    def test_new_booking2(self):
        result = self.book.new_booking('Diptan Regmi', '9818133208', 'Kathmandu', 'drt347826@gmail.com',
                                       None, '2020-2-2', 900, 1, 0)
        self.assertFalse(result)

    def test_new_booking3(self):
        result = self.book.new_booking('Diptan Regmi', '9818133208', 'Kathmandu', 'drt347826@gmail.com',
                                       '2020-1-1', '2020-2-2', '900', 1, 0)
        self.assertTrue(result)
