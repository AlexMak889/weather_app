import matplotlib.pyplot as plt
import db
import mariadb
def index():
    conn = db.conn
    cur = conn.cursor()
    cur.execute("SELECT temp FROM sensor_data WHERE temp_date = '2024-04-20' AND temp_time BETWEEN '%s:00:00' AND '%s:10:00'")
    data = [item[0] for item in cur.fetchall()]
    cur.close()
    # conn.close()  # Consider uncommenting this line to close the connection
    return data

def index2():
    conn = db.conn
    cur = conn.cursor()
    cur.execute("SELECT temp_time FROM sensor_data WHERE temp_date = '2024-04-20' AND temp_time BETWEEN '%s:00:00' AND '%s:10:00'", ('start_time', 'end_time'))
    data = [item[0] for item in cur.fetchall()]
    cur.close()
    # conn.close()  # Consider uncommenting this line to close the connection
    print(data)

    return data

data_x = index2()
print("data_y length")
print(len(data_x))
data_y = index()
print(len(data_y))
x = list(range(1, len(data_x) + 1))
y = list(range(1, len(data_y) + 1))


plt.plot(data_x, data_y)  

plt.xlabel('Index')
plt.ylabel('Temperature')
plt.title(label="Sensor Data", fontsize=16, color="green")
plt.legend()
plt.show()
