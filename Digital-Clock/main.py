import time
import datetime as dt
import turtle
import platform  # Importing platform module for system information

# create a turtle to display time and date
t = turtle.Turtle()

# create screen
s = turtle.Screen()

# set background color of the screen
s.bgcolor("orange")

# hide the turtle initially
t.hideturtle()

while True:
    t.clear()  # Clear previous drawings
    
    # obtain current time and date from the system
    current_time = dt.datetime.now()
    hr = current_time.hour % 12  # Convert to 12-hour format
    min = current_time.minute
    sec = current_time.second
    date = current_time.strftime("%A, %B %d, %Y")  # Format date as 'Day, Month Day, Year'
    
    # Get system information
    system_info = f"{platform.system()} {platform.release()} ({platform.architecture()[0]})"
    
    # display the date
    t.penup()
    t.goto(0, 40)  # Center position for date display
    t.pendown()
    t.write(date, align="center", font=("Arial Narrow", 20, "bold"))
    
    # display the time
    t.penup()
    t.goto(0, -15)  # Center position for time display
    t.pendown()
    t.write(f"{str(hr).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}",
             align="center", font=("Arial Narrow", 35, "bold"))
    
    # display the system information
    t.penup()
    t.goto(0, -40)  # Center position for system info display
    t.pendown()
    t.write(system_info, align="center", font=("Arial Narrow", 15, "bold"))
    
    time.sleep(1)
