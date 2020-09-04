import unittest
from Connection import *


class MyTest(unittest.TestCase):

    def test_register1(self):
        check = Staff()
        result = check.register(None, '1234567890', 'Diptan Regmi', '1999-04-30', 'Male', 'Kathmandu',
                                '9818133208', 'drt347826@gmail.com', 'Admin')
        self.assertFalse(result)

    def test_register2(self):
        check = Staff()
        result = check.register('diptan', '1234567890', 'Diptan Regmi', '1999-04-30', 'ale', 'Kathmandu',
                                '9818133208', 'drt347826@gmail.com', 'Admin')
        self.assertFalse(result)

    def test_register3(self):
        check = Staff()
        result = check.register('diptan', '1234567890', 'Diptan Regmi', '1999-04-30', 'Male', 'Kathmandu',
                                '9818133208', 'drt347826@gmail.com', 'Admin')
        self.assertTrue(result)

    def test_register4(self):
        check = Staff()
        result = check.register('employee', 'asdfghjkl', 'Front Desk', '2000-12-31', 'Female', 'Kathmandu',
                                '1234567890', None, 'User')
        self.assertTrue(result)

    def test_rlogin1(self):
        check = Staff()
        actual_result = check.login('diptan', '1234567890')
        expected_result = 1
        self.assertEqual(expected_result, len(actual_result))

    def test_login2(self):
        check = Staff()
        actual_result = check.login('user', 'aaaaa')
        expected_result = []
        self.assertEqual(expected_result, actual_result)

    def test_login3(self):
        check = Staff()
        actual_result = check.login(None, None)
        expected_result = []
        self.assertEqual(expected_result, actual_result)

    def test_create_room1(self):
        room = Room()
        result = room.create_rooms(None, 'Single Deluxe', 'AC', '4500')
        self.assertFalse(result)

    def test_create_room2(self):
        room = Room()
        result = room.create_rooms('900', 'Single Deluxe', 'AC', '4500')
        self.assertTrue(result)

    def test_create_room3(self):
        room = Room()
        result = room.create_rooms('901', 'Single Deluxe', 'AC', 5000)
        self.assertTrue(result)

    def test_create_room4(self):
        room = Room()
        result = room.create_rooms('901', 'Double Deluxe', 'Smoking', '5000')
        self.assertFalse(result)

    def test_show_rooms(self):
        room = Room()
        actual_result = room.show_rooms()
        expected_result = 1
        self.assertLessEqual(expected_result, len(actual_result))

    def test_new_booking1(self):
        book = Booking()
        result = book.new_booking('Diptan Regmi', '9818133208', 'Kathmandu', 'drt347826@gmail.com',
                                  '2020-1-1', '2020-2-2', 600, 1, 0)
        self.assertFalse(result)

    def test_new_booking2(self):
        book = Booking()
        result = book.new_booking('Diptan Regmi', '9818133208', 'Kathmandu', 'drt347826@gmail.com',
                                  None, '2020-8-1', 900, 1, 0)
        self.assertFalse(result)

    def test_new_booking3(self):
        book = Booking()
        result = book.new_booking('Diptan Regmi', '9818133208', 'Kathmandu', 'drt347826@gmail.com',
                                  '2020-8-1', '2020-8-1', '202', 1, 0)
        self.assertTrue(result)

    def test_new_booking4(self):
        book = Booking()
        result = book.new_booking('Diptan Regmi', '9818133208', 'Kathmandu', 'drt347826@gmail.com',
                                  '2020-1-1', '2020-2-2', '900', 'one', 0)
        self.assertFalse(result)

    def test_add_item1(self):
        menu = Item()
        result = menu.add_item('Juice', 'Fresh', 'hundred')
        self.assertFalse(result)

    def test_add_item2(self):
        menu = Item()
        result = menu.add_item('Juice', 'Fresh', None)
        self.assertFalse(result)

    def test_add_item3(self):
        menu = Item()
        result = menu.add_item('Juice', 'Fresh', 100)
        self.assertTrue(result)

    def test_add_item4(self):
        menu = Item()
        result = menu.add_item(None, 'Milkshake', 150)
        self.assertFalse(result)

    def test_add_item5(self):
        menu = Item()
        result = menu.add_item('Milkshake', None, 150)
        self.assertTrue(result)

    def test_show_items(self):
        menu = Item()
        actual_result = menu.show_items()
        expected_result = 1
        self.assertLessEqual(expected_result, len(actual_result))
