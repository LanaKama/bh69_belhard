from sqlite3 import connect

conn = connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS category (
    id INTEGER primary KEY autoincrement,
    name VARCHAR (32) NOT NULL UNIQUE
);
''')

conn.commit()

cur.execute('''
create table IF NOT EXISTS product (
    id INTEGER PRIMARY KEY autoincrement,
    name VARCHAR (128) NOT NULL,
    descr VARCHAR (4096),
    price decimal (8, 2) not null check (price > 0 ),
    is_published boolean default (true),
    category_id integer not null,
    foreign key (category_id) references category(id) on delete cascade
);
''')

conn.commit()

cur.execute('''
    create index if not exists category_id_index on product (category_id);''')

cur.execute('''
    create index if not exists is_published_index on product (is_published);''')
conn.commit()

# cur.execute('''
#     insert into category (name) values (?);
# ''', ('coffe', ))

conn.commit()


cur.execute('''
select * from category
where id >= 1;
''')

print(cur.fetchall())

cur.execute('''
    update category set name = ? where id = 1;
''', ('Кофе', ) )
conn.commit()

cur.execute("delete from category where name like '%акция%';")
conn.commit()










