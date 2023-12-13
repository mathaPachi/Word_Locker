import sqlite3
import pwdGen as pp
# Set up a connection
con = sqlite3.connect('database.db')

# Create a cursor
cur = con.cursor()

# Perform operations on the database
cur.execute(
  'create table if not exists passwords(site_ID INTEGER PRIMARY KEY, website_name text, username text,password text,website_link text,email text)'
)

def db_to_list():
  query = ("SELECT * FROM passwords")
  cur.execute(query)
  p = cur.fetchall()
  if p == []:
  print(
      '================================================================================================================================================================================================================'
    )
  print("")
  print("Add passwords , you don't have passwords saved")
  print("")
  print(
    '================================================================================================================================================================================================================'
  )
  d = {}
  L = []
  for i in p:
  d = {
    'ID': i[0],
    'website_name': i[1],
    'username': i[2],
    'password': i[3],
    'website_link': i[4],
    'email': i[5]
  }
  L.append(d)
  con.commit()
  return L
#insert values into table
def insert_val(web_id, website_name, username, password, website_link, email):
  print('You have chosen to add a new password')
  query = (
    "INSERT INTO passwords( site_ID , website_name, username, password, website_link, email) VALUES(:site_ID,:website_name , :username, :password ,:website_link , :email); "
  )

  val = {
    'site_ID': web_id,
    'website_name': website_name,
    'username': username,
    'password': password,
    'website_link': website_link,
    'email': email
  }
  cur.execute(query, val)
  print(
      '================================================================================================================================================================================================================'
  )
  print("")
  print('Your password has been added ')
  print("")
  print(
      '================================================================================================================================================================================================================'
  )
  con.commit()


#view a password
def get_val(website_name):
  print("")
  print('You have chosen to view a password')
  print("")
  query = ("SELECT * FROM passwords where website_name = :website_name")
  val = {'website_name': website_name}
  cur.execute(query, val)
  p = cur.fetchall()
  if p == []:
    print('No Passwords Found')
  d = {
    'ID': p[0][0],
    'website_name': p[0][1],
    'username': p[0][2],
    'password': p[0][3],
    'website_link': p[0][4],
    'email': p[0][5]
  }
  print('')
  con.commit()
  return d


#print the whole table
def print_table():
  print("")
  print('You have chosen to view all passwords')
  print("")
  query = ("SELECT * FROM passwords")
  cur.execute(query)
  p = cur.fetchall()
  if p == []:
  print("")
  print("Add passwords , you don't have passwords saved")
  print("")
  d = {}
  L = []
  for i in p:
  d = {
    'ID': i[0],
    'website_name': i[1],
    'username': i[2],
    'password': i[3],
    'website_link': i[4],
    'email': i[5]
  }
  L.append(d)
  con.commit()
  return L


#change a password
def change_val(website_name):
  print("")
  print('You have chosen to change a password')
  print("")
  query = (
    "UPDATE passwords SET password = :password WHERE website_name = :website_name"
  )
  password = pp.generator()
  val = {'website_name': website_name, 'password': password}
  cur.execute(query, val)
  p = cur.fetchall()
  if p == []:
  print('No Passwords Found')
  print("")
  print(      
    'Your password has been updated , To view your pasword go to menu and select option 3 '
  )
  print("")
  con.commit()


def delete_password(website_name):
  print("")
  print('You have chosen to delete a password')
  print("")
  query = ("DELETE FROM passwords WHERE website_name = :website_name")
  val = {'website_name': website_name}
  cur.execute(query, val)
  p = cur.fetchall()
  if p == []:
  print('No Passwords Found')
  print("")
  print(
    'Your password has been deleted , To view your pasword go to menu and select option 3 '
  )
  print("")
  con.commit()


# Close the connection
