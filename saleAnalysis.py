Vimport sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect('salesNea.db')
cursor = connection.cursor()


# create table for off peak and peak sales per day
cursor.execute('''
CREATE TABLE IF NOT EXISTS daily_sales (
    monday_peak INTEGER,
    monday_off_peak INTEGER,
    tuesday_peak INTEGER,
    tuesday_off_peak INTEGER,
    wednesday_peak INTEGER,
    wednesday_off_peak INTEGER,
    thursday_peak INTEGER,
    thursday_off_peak INTEGER,
    friday_peak INTEGER,
    friday_off_peak INTEGER,
    saturday_peak INTEGER,
    saturday_off_peak INTEGER,
    sunday_peak INTEGER,
    sunday_off_peak INTEGER
)
''')

cursor.execute(''' 
INSERT INTO daily_sales (
    monday_peak, monday_off_peak,
    tuesday_peak, tuesday_off_peak,
    wednesday_peak, wednesday_off_peak,
    thursday_peak, thursday_off_peak,
    friday_peak, friday_off_peak,
    saturday_peak, saturday_off_peak,
    sunday_peak, sunday_off_peak
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) 
''', (
    90, 80,
    76, 71,
    67, 78,
    98, 89,
    100, 110,
    95, 116,
    85, 95
))
cursor.execute("SELECT monday_peak, monday_off_peak, tuesday_peak, tuesday_off_peak, wednesday_peak, wednesday_off_peak, thursday_peak, thursday_off_peak, friday_peak, friday_off_peak, saturday_peak, saturday_off_peak, sunday_peak, sunday_off_peak FROM daily_sales;")
data = cursor.fetchall()
monday_peak, monday_off_peak, tuesday_peak, tuesday_off_peak, wednesday_peak, wednesday_off_peak, thursday_peak, thursday_off_peak, friday_peak, friday_off_peak, saturday_peak, saturday_off_peak, sunday_peak, sunday_off_peak = data[0]

peak_columns = [
    'monday_peak', 'tuesday_peak', 'wednesday_peak', 'thursday_peak',
    'friday_peak', 'saturday_peak', 'sunday_peak'
]
off_peak_columns = [
    'monday_off_peak', 'tuesday_off_peak', 'wednesday_off_peak', 'thursday_off_peak',
    'friday_off_peak', 'saturday_off_peak', 'sunday_off_peak'
]
peak_values = [
    monday_peak, tuesday_peak, wednesday_peak, thursday_peak,
    friday_peak, saturday_peak, sunday_peak
]

off_peak_values = [
    monday_off_peak, tuesday_off_peak, wednesday_off_peak, thursday_off_peak,
    friday_off_peak, saturday_off_peak, sunday_off_peak
]
plt.bar(peak_columns, peak_values)
plt.show()


##create table for income per day 
cursor.execute('''
CREATE TABLE IF NOT EXISTS daily_profit (
    monday_income INTEGER,
    tuesday_income INTEGER,
    wednesday_income INTEGER,
    thursday_income INTEGER,
    friday_income INTEGER,
    saturday_income INTEGER,
    sunday_income INTEGER
)
''')
profit_collumns = [ 
    'monday_income', 'tuesday_income', 'wednesday_income', 'thursday_income',
    'friday_income', 'saturday_income', 'sunday_income'
    ]
losses_collumns = [
     'monday_losses', 'tuesday_losses', 'wednesday_losses', 'thursday_losses',
    'friday_losses', 'saturday_losses', 'sunday_losses'
    ]
profit_values [ 
    'monday_income', 'tuesday_income', 'wednesday_income', 'thursday_income',
    'friday_income', 'saturday_income', 'sunday_income'
    ]
losses_values [
    'monday_losses', 'tuesday_losses', 'wednesday_losses', 'thursday_losses',
    'friday_losses', 'saturday_losses', 'sunday_losses'
    ]

plt.bar(profit_collumns, profit_values, losses_collumns, losses_values)
plt.show()



cursor.execute('CREATE TABLE IF NOT EXISTS item PRIMARY TEXT KEY, stock_purchased INTEGER, stock_sold INTEGER, shelf_price REAL, stock_price REAL')




