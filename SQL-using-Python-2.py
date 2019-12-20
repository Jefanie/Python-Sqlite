import sqlite3

#create database
conn = sqlite3.connect('company.db')
c = conn.cursor()

#department table
c.execute('drop table if exists department')
c.execute("""create table department 
(dept_no text primary key, 
dept_name text, 
location text)""")

#employee table
c.execute('drop table if exists employee')
c.execute("""create table employee 
(emp_no integer primary key, 
emp_fname text, 
emp_lname text,
dept_no text,
foreign key (dept_no) references department(dept_no))""")

#project table
c.execute('drop table if exists project')
c.execute("""create table project 
(project_no text primary key, 
project_name text, 
budget integer)""")

#works_on table
c.execute('drop table if exists works_on')
c.execute("""create table works_on 
(emp_no integer, 
project_no text, 
job text,
enter_date text,
foreign key (emp_no) references employee(emp_no),
foreign key (project_no) references project(project_no))""")

#insert into department
c.execute("""insert into department values
('d1', 'Research', 'Dallas'),
('d2', 'Accounting', 'Seattle'),
('d3', 'Marketing', 'Dallas')""")

#insert into employee
c.execute("""insert into employee values
(25348, 'Matthew', 'Smith', 'd3'),
(10102, 'Ann', 'Jones', 'd3'),
(18316, 'John', 'Barrimore', 'd1'),
(29346, 'James', 'James', 'd2'),
(9031, 'Elke', 'Hansel', 'd2'),
(2581, 'Elsa', 'Bertoni', 'd2'),
(28559, 'Sybill', 'Moser', 'd1')""")

#insert into project
c.execute("""insert into project values
('p1', 'Apollo', 120000),
('p2', 'Gemini', 95000),
('p3', 'Mercury', 186500)""")

#insert into works_on
c.execute("""insert into works_on values
(10102, 'p1', 'Analyst', '2006.10.1'),
(10102, 'p3', 'Manager', '2008.1.1'),
(25348, 'p2', 'Clerk', '2007.2.15'),
(18316, 'p2', '', '2007.6.1'),
(29346, 'p2', '', '2006.12.15'),
(2581, 'p3', 'Analyst', '2007.10.15'),
(9031, 'p1', 'Manager', '2007.4.14'),
(28559, 'p1', '', '2007.8.1'),
(28559, 'p2', 'Clerk', '2008.2.1'),
(9031, 'p3', 'Clerk', '2006.11.15'),
(29346, 'p1', 'Clerk', '2007.1.4')""")

#update department
c.execute("update department set location = 'Atlanta' where dept_no = 'd3'")

#delete employee
c.execute("delete from employee where emp_no = 2581")

#print all employee
c.execute("select * from employee")
print(c.fetchall())

#print all department
c.execute("select * from department")
print(c.fetchall())

#print employee name/department name/department location for Gemini
c.execute("select employee.emp_fname, employee.emp_lname, department.dept_name, department.location from project join works_on on project.project_no = works_on.project_no join employee on works_on.emp_no = employee.emp_no join department on employee.dept_no = department.dept_no where project.project_name = 'Gemini'")
print(c.fetchall())

conn.commit()
conn.close()