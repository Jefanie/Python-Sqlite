import sqlite3

conn = sqlite3.connect('world_updated.db')
c = conn.cursor()
# c.execute('select name from sqlite_master where type = \'table\'')
# c.execute('select sql from sqlite_master where name = \'city\'')
# print(c.fetchall())


# Inserting data into a table
c.execute('DELETE FROM city where city.ID = 5000')

c.execute("""INSERT INTO city VALUES (5000, "King's Landing", "WTO", "", "5000000000")""")

c.execute('SELECT * FROM city WHERE city.ID = 5000')
print(c.fetchall())


# Selecting areas fields for a certain condition
c.execute('SELECT countryName, Continent, Region, Population_country FROM country where Population_country > 1000000000')
print(c.fetchall())

c.execute('SELECT * from city where CountryCode = "USA" AND Population_city > 1000000')
print(c.fetchall())


#How many cities?
c.execute('SELECT COUNT(cityName) from city where CountryCode = "USA" AND Population_city > 1000000')
print(c.fetchone())


#Average population?
c.execute('SELECT AVG(Population_city) from city where CountryCode = "USA" AND Population_city > 1000000')
print(c.fetchone())


conn.commit()
conn.close()
