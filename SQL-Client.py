import psycopg2


def create_db(conn):
    with conn.cursor() as cursor:
        with open('creat_table.sql', 'r') as create_table:
            cursor.execute(create_table.read())
        print('Таблицы созданы!')


def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cursor:
        cursor.execute(
            f'''INSERT INTO client (first_name, last_name, e_mail)
            VALUES ('{first_name}', '{last_name}', '{email}');'''
            )
        if phones is not None:
            for phone in phones.split():
                f'''INSERT INTO number_phone (number, id_client)
                VALUES ('{phone}', (SELECT id 
                FROM client 
                WHERE e_mail = '{email}');'''
        print('Клиент добавлен!')


def add_phone(conn, client_id, phone):
    with conn.cursor() as cursor:
        cursor.execute(f'''INSERT INTO number_phone (number, id_client) VALUES ('{phone}', {client_id});''')
        print(f'Номер телефона клиенту {client_id} добавлен!')


def change_client(conn, client_id, first_name=None, last_name=None, e_mail=None, phones=None):
    with conn.cursor() as cursor:
        values_for_update = {'first_name': first_name, 'last_name': last_name, 'e_mail': e_mail, 'phones': phones}
        for key, value in values_for_update.items():
            if value is not None and key == 'phones':
                cursor.execute(f'DELETE FROM number_phone WHERE id_client = {client_id};')
                for phone in phones.split():
                    cursor.execute(f'''INSERT INTO number_phone (number, id_client) VALUES ('{phone}', {client_id});''')
            elif value is not None:
                cursor.execute(f"UPDATE client SET {key} = '{value}' WHERE id = {client_id}")
    print(f'Данные о клиенте {client_id} обновлены!')


def delete_phone(conn, client_id, phone):
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE FROM number_phone WHERE id_client = {client_id} and number = '{phone}'")
        print(f'Номер телефона у клиента {client_id} удален!')


def delete_client(conn, client_id):
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE FROM number_phone WHERE id_client = {client_id}")
        cursor.execute(f"DELETE FROM client WHERE id = {client_id}")
        print(f'Информация о клиенте {client_id} удалена!')


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cursor:
        if email is not None:
            cursor.execute(f"SELECT * FROM client WHERE e_mail = '{email}'")
            print(cursor.fetchall())
            cursor.execute(
                f'''SELECT number 
                FROM number_phone 
                WHERE id_client = (SELECT id 
                FROM client 
                WHERE e_mail = '{email}')''')
            print(cursor.fetchall())
            return
        if phone is not None:
            cursor.execute(
                f'''SELECT * 
                FROM client 
                WHERE id = (SELECT id_client 
                FROM number_phone 
                WHERE number = '{phone}')''')
            print(cursor.fetchall())
            cursor.execute(
                f'''SELECT number 
                FROM number_phone 
                WHERE id_client = (SELECT id_client 
                FROM number_phone 
                WHERE number = '{phone}')''')
            print(cursor.fetchall())
            return
        if first_name is not None and last_name is None:
            cursor.execute(f"SELECT * FROM client WHERE first_name = '{first_name}'")
            print(cursor.fetchall())
            cursor.execute(
                f'''SELECT number FROM number_phone 
                WHERE id_client IN (SELECT id FROM client WHERE first_name = '{first_name}')''')
            print(cursor.fetchall())
            return
        if last_name is not None and first_name is None:
            cursor.execute(f"SELECT * FROM client WHERE last_name = '{last_name}'")
            print(cursor.fetchall())
            cursor.execute(
                f'''SELECT number FROM number_phone 
                WHERE id_client IN (SELECT id FROM client WHERE last_name = '{last_name}')''')
            print(cursor.fetchall())
            return
        if last_name is not None and first_name is not None:
            cursor.execute(f"SELECT * FROM client WHERE last_name = '{last_name}' and first_name = '{first_name}'")
            print(cursor.fetchall())
            cursor.execute(
                f'''SELECT number FROM number_phone 
                WHERE id_client IN (SELECT id FROM client 
                WHERE last_name = '{last_name}' and first_name = '{first_name}')''')
            print(cursor.fetchall())
            return

with psycopg2.connect(dbname='postgres', user='postgres', password='3616', host='localhost') as conn:
    create_db(conn)
    add_client(conn, 'Dima', 'PUDLO', 'dpmail.ru', phones='89228513682 89292825456')
    # add_client(conn, 'Sergey', 'PUDLO', 'spmail.ru', phones='123456789')
    # add_phone(conn, 1, '89228513682')
    # change_client(conn, 1, phones='123123123123 321321321321')
    # delete_phone(conn, 1, phone='123123123123')
    # delete_client(conn, 2)
    # find_client(conn, first_name=None, last_name=None, email=None, phone=None)