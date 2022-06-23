import psycopg2


def create_db(conn):
    with conn.cursor() as cursor:
        table_name = ('client', 'number_phone')
        table_exists = []
        table_return = ''
        for name in table_name:
            cursor.execute(
                f'''SELECT EXISTS(
                SELECT 1 AS result 
                FROM pg_tables 
                WHERE schemaname = 'public' 
                AND tablename = '{name}');'''
                )
            table_exists.append(cursor.fetchone()[0])
        if not table_exists[0]:
            cursor.execute(
            f'''CREATE TABLE {table_name[0]}(
            id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            e_mail VARCHAR(50),
            CONSTRAINT client_pkey PRIMARY KEY (id));'''
            )
        else:
            table_return += f'Таблица {table_name[0]} уже создана! \n'
        if not table_exists[1]:
            cursor.execute(
            f'''CREATE TABLE {table_name[1]}(
            id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
            number VARCHAR(20),
            id_client INT NOT NULL,
            CONSTRAINT number_phone_pkey PRIMARY KEY (id),
            FOREIGN KEY (id_client) REFERENCES client(id));'''
            )
        else:
            table_return += f'Таблица {table_name[1]} уже создана!'
        if table_return:
            print(table_return)
        else:
            print('Таблицы созданы!')


def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cursor:
        cursor.execute(
            f'''SELECT EXISTS(
            SELECT 1 AS result
            FROM client 
            WHERE first_name = '{first_name}' 
            AND last_name = '{last_name}');'''
            )
        if not cursor.fetchone()[0]:
            cursor.execute(
                f'''INSERT INTO client (first_name, last_name, e_mail)
                VALUES ('{first_name}', '{last_name}', '{email}');'''
                )
            if phones is not None:
                for phone in phones.split():
                    cursor.execute(
                        f'''INSERT INTO number_phone (number, id_client)
                        VALUES ('{phone}', (SELECT id FROM client WHERE first_name = '{first_name}' and last_name = '{last_name}'))
                        ;'''
                        )
            print('Клиент добавлен!')
        else:
            print('Клиент уже существует!')


def add_phone(conn, client_id, phone):
    with conn.cursor() as cursor:
        cursor.execute(
            f'''SELECT EXISTS(
            SELECT 1 AS result
            FROM number_phone 
            WHERE number = '{phone}');'''
            )
        if not cursor.fetchone()[0]:
            cursor.execute(
                f'''INSERT INTO number_phone (number, id_client)
                VALUES ('{phone}', {client_id});'''
                )
            print(f'Номер телефона клиенту {client_id} добавлен!')
        else:
            print(f'Номер телефона у клиента {client_id} уже существует!')


with psycopg2.connect(dbname='postgres', user='postgres', password='3616', host='localhost') as conn:
    create_db(conn)
    add_client(conn, 'Dima', 'PUDLO', 'dpmail.ru', phones='89228513682 89292825456')
    add_phone(conn, 1, '89228513682')