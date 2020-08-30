import mysql.connector


class Connection:
    def __init__(self):
        self.my_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='regmi321',
            auth_plugin='mysql_native_password',
            database='hotel'
        )
        self.my_cursor = self.my_connection.cursor()

    def iud(self, qry, values):
        try:
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def insert_with_id_return(self, qry, values):
        try:
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            self.my_connection.close()
            return self.my_cursor.lastrowid
        except Exception as e:
            print(e)
            return 0

    def show_data(self, qry):
        data = []
        try:
            self.my_cursor.execute(qry)
            data = self.my_cursor.fetchall()
            self.my_connection.close()
            return data
        except Exception as e:
            print(e)
            return data

    def search_data(self, qry, val):
        data = []
        try:
            self.my_cursor.execute(qry, val)
            data = self.my_cursor.fetchall()
            self.my_connection.close()
            return data
        except Exception as e:
            print(e)
            return data


class Staff(Connection):
    def __init__(self):
        super().__init__()

    def check_username(self):
        qry = "SELECT username FROM staff"
        occ_user = self.show_data(qry)
        return occ_user

    def register(self, username, password, name, dob, gender, address, mobile, email, type_):
        qry = "INSERT into staff(username, password, name, dob, gender, address, mobile, email, type) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (username, password, name, dob, gender, address, mobile, email, type_)
        return self.iud(qry, values)

    def login(self, username, password):
        qry = "SELECT * FROM staff WHERE username = %s AND password = %s"
        values = (username, password)
        user = self.search_data(qry, values)
        return user


class Room(Connection):
    def __init__(self):
        super().__init__()

    def create_rooms(self, room_no, room_category, room_description, price, room_status):
        qry = "INSERT INTO rooms(room_no, room_category, room_description, price, room_status)" \
              " VALUES(%s, %s, %s, %s, %s)"
        values = (room_no, room_category, room_description, price, room_status)
        return self.iud(qry, values)

    def update_rooms(self, room_category, room_description, price, room_status, room_no):
        qry = "UPDATE rooms SET room_category = %s, room_description = %s, price = %s, room_status = %s " \
              "WHERE room_no = %s"
        values = (room_category, room_description, price, room_status, room_no)
        return self.iud(qry, values)

    def show_rooms(self):
        qry = "SELECT * FROM rooms"
        room = self.show_data(qry)
        return room

    def show_rooms_stat(self):
        qry = "SELECT * FROM rooms WHERE room_status = %s OR room_status = %s order by price"
        values = ("Available", "Cleaning")
        room = self.search_data(qry, values)
        return room

    def available_rooms(self):
        qry = "SELECT room_no FROM rooms where room_status = %s"
        values = ("Available",)
        room = self.search_data(qry, values)
        return room

    def change_status(self, status, room):
        qry = "UPDATE rooms SET room_status = %s WHERE room_no = %s"
        values = (status, room)
        return self.iud(qry, values)

    def search_rooms(self, category, value):
        qry = " SELECT * FROM rooms WHERE " + category + " LIKE %s AND room_no in (SELECT room_no from rooms where " \
                                                         "room_status = 'Available' OR room_status = 'Cleaning')"
        values = ("%" + value + "%",)
        room = self.search_data(qry, values)
        return room


class Booking(Connection):
    def __init__(self):
        super().__init__()

    def new_booking(self, name, phone, address, email, check_in, check_out, room, adults, children):
        qry = """INSERT INTO booking
        (cus_name, cus_mobile, cus_add, cus_email, check_in, check_out, room, adults, children, booking_status)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (name, phone, address, email, check_in, check_out, room, adults, children, "Staying")
        return self.iud(qry, values)

    def show_active_booking(self):
        qry = "SELECT id, cus_name, room, check_in, check_out FROM booking where booking_status=%s order by check_out"
        values = ("Staying",)
        return self.search_data(qry, values)

    def check_out(self, out, id):
        qry = "UPDATE booking SET check_out=%s where id=%s"
        values = (out, id)
        return self.iud(qry, values)

    def booking_stat(self, id):
        qry = "UPDATE booking SET booking_status='Checked Out' where id=%s"
        values = (id,)
        return self.iud(qry, values)


class Bill(Connection):
    def __init__(self):
        super().__init__()

    def save_payment(self, booking_id, discount, amount, paid):
        qry = "insert into payment (booking_id, discount, paid_amount, payment_type) values (%s, %s, %s, %s)"
        values = (booking_id, discount, amount, paid)
        return self.iud(qry, values)

    def room_bill(self, booking_id):
        qry = "select cus_name, check_in, check_out, room_no, price " \
              "from booking join rooms on booking.room=rooms.room_no and booking.id=%s"
        values = (booking_id,)
        return self.search_data(qry, values)
