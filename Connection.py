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

    def check_out(self, out, id_):
        """change check_out date"""
        qry = "UPDATE booking SET check_out=%s where id=%s"
        values = (out, id_)
        return self.iud(qry, values)

    def booking_stat(self, id_):
        """on checking out of the hotel change status of customer to checked_out"""
        qry = "UPDATE booking SET booking_status='Checked Out' where id=%s"
        values = (id_,)
        return self.iud(qry, values)


class Item(Connection):
    """
            This class works with menu for hotel.

            Methods:
                add_item()
                show_item()
                update_item()
                delete_item()
                search_item()

            """

    def __init__(self):
        super().__init__()

    def add_item(self, name, type_, price):
        """add an item to menu"""
        qry = "INSERT INTO items (name, type, price) VALUES (%s, %s, %s)"
        values = (name, type_, price)
        return self.iud(qry, values)

    def show_items(self):
        """returns all menu details"""
        qry = "SELECT * FROM items"
        res = self.show_data(qry)
        return res

    def update_item(self, id_, name, type_, price):
        """update an item detail of menu"""
        qry = "UPDATE items SET name = %s, type=%s, price =%s WHERE id = %s"
        values = (name, type_, price, id_)
        return self.iud(qry, values)

    def delete_item(self, id_):
        """delete an item from menu"""
        qry = "DELETE FROM items WHERE id = %s"
        values = (id_,)
        return self.iud(qry, values)

    def search_item(self, search):
        """search in menu"""
        qry = "SELECT * FROM items WHERE name LIKE %s OR type LIKE %s OR price LIKE %s"
        values = ("%" + search + "%", "%" + search + "%", "%" + search + "%")
        res = self.search_data(qry, values)
        return res


class Order(Connection):
    """
            This class works with order of customer in hotel.

            Methods:
                add_order()
                show_order()
                delete_order()

            """

    def __init__(self):
        super().__init__()

    def add_order(self, ordered_item_list, cus_id):
        """save orders"""
        for i in ordered_item_list:
            qry = "INSERT INTO orders (item_id, cus_id, qty) VALUES (%s, %s, %s)"
            val = (i[0], cus_id, i[1])
            self.iud(qry, val)

    def show_orders(self, cus_id):
        """displays all orders made by a customer"""
        qry = """SELECT orders.id, items.type, items.name, orders.qty FROM orders
        JOIN items ON orders.item_id = items.id JOIN booking ON booking.id = orders.cus_id 
        where cus_id = %s order by id desc"""
        values = (cus_id,)
        res = self.search_data(qry, values)
        return res

    def delete_order(self, order_id):
        """delete a specific order"""
        qry = "DELETE FROM orders WHERE id = %s"
        values = (order_id,)
        return self.iud(qry, values)


class Bill(Connection):
    """
                This class works with Billing of hotel.

                Methods:
                    save_payment()
                    room_bill()
                    order_bill()
                    total_order()
                    view_bill()
                    search_by_date()
                    search_by_date_sum()
                    search()

                """

    def __init__(self):
        super().__init__()

    def save_payment(self, booking_id, discount, amount, paid, billed_by):
        """save billing details"""
        qry = "insert into payment (booking_id, discount, paid_amount, payment_type, billed_by)" \
              " values (%s, %s, %s, %s, %s)"
        values = (booking_id, discount, amount, paid, billed_by)
        return self.iud(qry, values)

    def room_bill(self, booking_id):
        """returns the customer details of stay in hotel and room for billing"""
        qry = "select cus_name, check_in, check_out, room_no, price " \
              "from booking join rooms on booking.room=rooms.room_no and booking.id=%s"
        values = (booking_id,)
        return self.search_data(qry, values)

    def order_bill(self, cus_id):
        """returns all the orders made by customer"""
        qry = "select concat(type,' ',name), price, qty, price*qty " \
              "from items join orders on orders.item_id = items.id where cus_id = %s;"
        values = (cus_id,)
        return self.search_data(qry, values)

    def total_order(self, cus_id):
        """returns the total orders bill"""
        qry = "select sum(price*qty) from items join orders on orders.item_id = items.id where cus_id = %s;"
        values = (cus_id,)
        return self.search_data(qry, values)

    def view_bill(self):
        """returns all the paid bills"""
        qry = """select cus_name, cus_add, cus_mobile, paid_amount, discount, payment_type, check_in, check_out,
         room, adults, children from payment join booking on payment.booking_id = booking.id"""
        value = self.show_data(qry)
        return value

    def search_by_date(self, a, b):
        """returns all the paid bills of selected date period"""
        qry = """select cus_name, cus_add, cus_mobile, paid_amount, discount, payment_type, check_in, check_out,
                 room, adults, children from payment join booking on payment.booking_id = booking.id
                 where check_out between %s and %s"""
        values = (a, b)
        return self.search_data(qry, values)

    def search_by_date_sum(self, a, b):
        """returns all the paid bills of selected date period"""
        qry = """select sum(paid_amount) from payment join booking on payment.booking_id = booking.id
                 where check_out between %s and %s"""
        values = (a, b)
        return self.search_data(qry, values)

    def search(self, search):
        """search in payments"""
        qry = """select cus_name, cus_add, cus_mobile, paid_amount, discount, payment_type, 
        check_in, check_out, room, adults, children 
        from payment join booking on payment.booking_id = booking.id 
        where cus_name like %s or cus_add like %s or payment_type like %s"""
        values = ("%" + search + "%", "%" + search + "%", "%" + search + "%")
        res = self.search_data(qry, values)
        return res
