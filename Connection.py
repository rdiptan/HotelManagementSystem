import mysql.connector


class Connection:
    """
            This class connects python file with database.

            Methods:
                iud()
                insert_with_id_return()
                show_data()
                search_dat()

            """
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
        """insert, update and delete data in database tables"""
        try:
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def insert_with_id_return(self, qry, values):
        """insert data to database and return primary key"""
        try:
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            self.my_connection.close()
            return self.my_cursor.lastrowid
        except Exception as e:
            print(e)
            return 0

    def show_data(self, qry):
        """fetch data from database table"""
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
        """search for data in database"""
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
    """
            This class works with login and registration of user for application.

            Methods:
                check_username()
                register()
                login()

            """
    def __init__(self):
        super().__init__()

    def check_username(self):
        """fetch usernames from staff table"""
        qry = "SELECT username FROM staff"
        occ_user = self.show_data(qry)
        return occ_user

    def register(self, username, password, name, dob, gender, address, mobile, email, type_):
        """insert data to staff table"""
        qry = "INSERT into staff(username, password, name, dob, gender, address, mobile, email, type) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (username, password, name, dob, gender, address, mobile, email, type_)
        return self.iud(qry, values)

    def login(self, username, password):
        """verify username and password for login"""
        qry = "SELECT * FROM staff WHERE username = %s AND password = %s"
        values = (username, password)
        user = self.search_data(qry, values)
        return user


class Room(Connection):
    """
            This class works with rooms for hotel.

            Methods:
                create_rooms()
                update_rooms()
                show_rooms()
                show_room_stat()
                available_rooms()
                change_status()
                search_rooms()
                delete_rooms()

            """
    def __init__(self):
        super().__init__()

    def create_rooms(self, room_no, room_category, room_description, price):
        """save new rooms data to database"""
        qry = "INSERT INTO rooms(room_no, room_category, room_description, price)" \
              " VALUES(%s, %s, %s, %s)"
        values = (room_no, room_category, room_description, price)
        return self.iud(qry, values)

    def update_rooms(self, room_category, room_description, price, room_no):
        """update room details in database"""
        qry = "UPDATE rooms SET room_category = %s, room_description = %s, price = %s WHERE room_no = %s"
        values = (room_category, room_description, price, room_no)
        return self.iud(qry, values)

    def show_rooms(self):
        """returns all rooms"""
        qry = "SELECT * FROM rooms"
        room = self.show_data(qry)
        return room

    def show_rooms_stat(self):
        """return rooms with room status available and cleaning"""
        qry = "SELECT * FROM rooms WHERE room_status = %s OR room_status = %s order by price"
        values = ("Available", "Cleaning")
        room = self.search_data(qry, values)
        return room

    def available_rooms(self):
        """returns available rooms"""
        qry = "SELECT room_no FROM rooms where room_status = %s"
        values = ("Available",)
        room = self.search_data(qry, values)
        return room

    def change_status(self, status, room):
        """update room status"""
        qry = "UPDATE rooms SET room_status = %s WHERE room_no = %s"
        values = (status, room)
        return self.iud(qry, values)

    def search_rooms(self, category, value):
        """search for rooms"""
        qry = " SELECT * FROM rooms WHERE " + category + " LIKE %s AND room_no in (SELECT room_no from rooms where " \
                                                         "room_status = 'Available' OR room_status = 'Cleaning')"
        values = ("%" + value + "%",)
        room = self.search_data(qry, values)
        return room

    def delete_rooms(self, room):
        """delete specific room"""
        qry = "DELETE FROM rooms WHERE room_no = %s"
        values = (room,)
        return self.iud(qry, values)


class Booking(Connection):
    """
                This class works with booking of hotel's customer.

                Methods:
                    new_booking()
                    show_active_booking()
                    check_out()
                    booking_stat()
                    view_booking()

                """
    def __init__(self):
        super().__init__()

    def new_booking(self, name, phone, address, email, check_in, check_out, room, adults, children):
        """add new customer details"""
        qry = """INSERT INTO booking
        (cus_name, cus_mobile, cus_add, cus_email, check_in, check_out, room, adults, children)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (name, phone, address, email, check_in, check_out, room, adults, children)
        return self.iud(qry, values)

    def show_active_booking(self):
        """returns the customer staying in hotel currently"""
        qry = "SELECT id, cus_name, room, check_in, check_out FROM booking where booking_status=%s order by check_out"
        values = ("Staying",)
        return self.search_data(qry, values)

    def check_out(self, out, id):
        """change check_out date"""
        qry = "UPDATE booking SET check_out=%s where id=%s"
        values = (out, id)
        return self.iud(qry, values)

    def booking_stat(self, id):
        """on checking out of the hotel change status of customer to checked_out"""
        qry = "UPDATE booking SET booking_status='Checked Out' where id=%s"
        values = (id,)
        return self.iud(qry, values)

    def view_booking(self):
        """returns all bookings"""
        qry = "select cus_name, cus_add, cus_mobile, check_in, check_out, room, room_category, adults, children " \
              "from booking left join rooms on booking.room=rooms.room_no;"
        value = self.show_data(qry)
        return value


class Bill(Connection):
    """
                This class works with Billing of hotel.

                Methods:
                    save_payment()
                    room_bill()
                    view_bill()

                """
    def __init__(self):
        super().__init__()

    def save_payment(self, booking_id, discount, amount, paid):
        """save billing details"""
        qry = "insert into payment (booking_id, discount, paid_amount, payment_type) values (%s, %s, %s, %s)"
        values = (booking_id, discount, amount, paid)
        return self.iud(qry, values)

    def room_bill(self, booking_id):
        """returns the customer details of stay in hotel and room for billing"""
        qry = "select cus_name, check_in, check_out, room_no, price " \
              "from booking join rooms on booking.room=rooms.room_no and booking.id=%s"
        values = (booking_id,)
        return self.search_data(qry, values)

    def view_bill(self):
        """returns all the paid bills"""
        qry = "select cus_name, cus_add, cus_mobile, paid_amount, discount, payment_type, check_in, check_out, room " \
              "from payment join booking on payment.booking_id = booking.id;"
        value = self.show_data(qry)
        return value
