from tkinter import *
import random
from datetime import date
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import os

# Create the main window
window = Tk()
window.minsize(width=860, height=860)
window.title("MY_Travel_Mate")
window.configure(bg='white')


def save_ticket_info(ticket_info):
    try:
        current_date = date.today()
        filename = f"ticket_{current_date}.txt"

        if os.path.exists(filename):
            # Append the ticket information to the existing file
            with open(filename, 'a') as file:
                file.write(ticket_info + "\n")  # Add a new line after each ticket
        else:
            # Create a new file and write the ticket information
            with open(filename, 'w') as file:
                file.write(ticket_info + "\n")  # Add a new line after each ticket
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the ticket information: {str(e)}")
   
  
def busTime():
    
      # Get the current date
    current_date = date.today()

    # Convert the date to a string in the desired format
    date_string = current_date.strftime("%Y-%m-%d")  # Example format: YYYY-MM-DD

    # Create a label to display the date
    label = Label(window, text="Date: " + date_string, bg='black', fg='white')
    label.pack()
#intro
    welcoming_frame=Frame(window,bg='black')
    welcoming_label=Label(welcoming_frame,text='My Travel Mate',font=("Arial", 20, "bold") ,bg='black',fg='white')
    welcoming_label.pack()
    welcoming_label2=Label(welcoming_frame,text='start your journey with us... ',font=("Arial") ,bg='black' ,fg='white')
    welcoming_label2.pack()

    welcoming_frame.pack()
#Station 1 timing information
    station_label=Label(window,text='Station 1 DEPARTURE TIMINGS',font=("Arial", 14, "bold") ,bg='black',fg='white')
    station_label.place(x=10,y=95)
    timing_frame=Frame(window,bg='black')

    timing_label=Label(timing_frame,text='Bus A-1011: Departure time 8:00 AM, Station 1' ,bg='black',fg='white')
    timing_label.pack()
    timing_label2=Label(timing_frame,text='Bus A-1022: Departure time 9:00 AM, Station 1 ' ,bg='black' ,fg='white')
    timing_label2.pack()
    timing_label3=Label(timing_frame,text='Bus A-1033: Departure time 10:00 AM, Station 1' ,bg='black',fg='white')
    timing_label3.pack()
    timing_label4=Label(timing_frame,text='Bus A-1044: Departure time 11:00 AM, Station 1 ' ,bg='black' ,fg='white')
    timing_label4.pack()
    timing_label5=Label(timing_frame,text='Bus A-1055: Departure time 12:00 PM, Station 1' ,bg='black',fg='white')
    timing_label5.pack()


    timing_labe1=Label(timing_frame,text='Bus B-1011: Departure time 1:00 PM, Station 1' ,bg='black',fg='white')
    timing_label.pack()
    timing_labe22=Label(timing_frame,text='Bus B-1022: Departure time 2:00 PM, Station 1 ' ,bg='black' ,fg='white')
    timing_labe22.pack()
    timing_label33=Label(timing_frame,text='Bus B-1033: Departure time 3:00 PM, Station 1' ,bg='black',fg='white')
    timing_label33.pack()
    timing_label44=Label(timing_frame,text='Bus B-1044: Departure time 4:00 PM, Station 1 ' ,bg='black' ,fg='white')
    timing_label44.pack()
    timing_label55=Label(timing_frame,text='Bus B-1055: Departure time 5:00 PM, Station 1' ,bg='black',fg='white')
    timing_label55.pack()

    timing_frame.place(x=30,y=130)


#station 2 timing information

    station2_label=Label(window,text='Station 2 DEPARTURE TIMINGS',font=("Arial", 14, "bold") ,bg='black',fg='white')
    station2_label.place(x=560,y=95)
    timing_frame=Frame(window,bg='black')

    timings2_label=Label(timing_frame,text='Bus B-1011: Departure time 8:00 AM, Station 2' ,bg='black',fg='white')
    timings2_label.pack()
    timings2_label2=Label(timing_frame,text='Bus B-1022: Departure time 9:00 AM, Station 2 ' ,bg='black' ,fg='white')
    timings2_label2.pack()
    timings2_label3=Label(timing_frame,text='Bus B-1033: Departure time 10:00 AM, Station 2' ,bg='black',fg='white')
    timings2_label3.pack()
    timings2_label4=Label(timing_frame,text='Bus B-1044: Departure time 11:00 AM, Station 2 ' ,bg='black' ,fg='white')
    timings2_label4.pack()
    timings2_label5=Label(timing_frame,text='Bus B-1055: Departure time 12:00 PM, Station 2' ,bg='black',fg='white')
    timings2_label5.pack()


    timing_labe1=Label(timing_frame,text='Bus A-1011: Departure time 1:00 PM, Station 2' ,bg='black',fg='white')
    timing_label.pack()
    timing_labe22=Label(timing_frame,text='Bus A-1022: Departure time 2:00 PM, Station 2 ' ,bg='black' ,fg='white')
    timing_labe22.pack()
    timing_label33=Label(timing_frame,text='Bus A-1033: Departure time 3:00 PM, Station 2' ,bg='black',fg='white')
    timing_label33.pack()
    timing_label44=Label(timing_frame,text='Bus A-1044: Departure time 4:00 PM, Station 2 ' ,bg='black' ,fg='white')
    timing_label44.pack()
    timing_label55=Label(timing_frame,text='Bus A-1055: Departure time 5:00 PM, Station 2' ,bg='black',fg='white')
    timing_label55.pack()

    timing_frame.place(x=570,y=130)



def main():
    busTime()
    


# bus info
bus_seats_st1 = {
    'Bus A-1011': 20,
    'Bus A-1022': 20,
    'Bus A-1033': 20,
    'Bus A-1044': 20,
    'Bus A-1055': 20,
    'Bus B-1011': 20,
    'Bus B-1022': 20,
    'Bus B-1033': 20,
    'Bus B-1044': 20,
    'Bus B-1055': 20
}

bus_seats_st2 = {
    'Bus B-1011': 20,
    'Bus B-1022': 20,
    'Bus B-1033': 20,
    'Bus B-1044': 20,
    'Bus B-1055': 20,
    'Bus A-1011': 20,
    'Bus A-1022': 20,
    'Bus A-1033': 20,
    'Bus A-1044': 20,
    'Bus A-1055': 20
}

#Departure Time

dep_time_st1 = {
    'Bus A-1011': "8:00_AM",
    'Bus A-1022': "9:00_AM",
    'Bus A-1033': "10:00_AM",
    'Bus A-1044': "11:00_AM",
    'Bus A-1055': "12:00_PM",
    'Bus B-1011': "1:00_PM",
    'Bus B-1022': "2:00_PM",
    'Bus B-1033': "3:00_PM",
    'Bus B-1044': "4:00_PM",
    'Bus B-1055': "5:00_PM"
}

dep_time_st2 = {
    'Bus B-1011': "8:00_AM",
    'Bus B-1022': "9:00_AM",
    'Bus B-1033': "10:00_AM",
    'Bus B-1044': "11:00_AM",
    'Bus B-1055': "12:00_PM",
    'Bus A-1011': "1:00_PM",
    'Bus A-1022': "2:00_PM",
    'Bus A-1033': "3:00_PM",
    'Bus A-1044': "4:00_PM",
    'Bus A-1055': "5:00_PM"
}
main()


#available seats
available_seats_frame=Frame(window, bg='white')
available_seats_label = Label(available_seats_frame, text="Avalaible Seats:  20", bg='white', fg='black', font=("Arial", 14))
available_seats_label.pack(side='right')
available_seats_frame.place(x=430, y=530)

def generate_ticket():
    name = name_entry.get()
    location = location_combobox.get()
    date = date_combobox.get()
    bus = bus_combobox1.get()
    price=price_combobox.get()
    departure_time=departure_time_combobox1.get()
    current_value = available_seats_label.cget("text")
    

    if location == "Station 1":
        if bus in bus_seats_st1 and bus_seats_st1[bus] > 0:
            bus_seats_st1[bus] -= 1
            print(bus_seats_st1)
            new_value = f"Avalaible Seats: {bus_seats_st1[bus]}"
            print(new_value)
            available_seats_label.configure(text=new_value)
        else:
            messagebox.showerror("Error", "Selected bus is fully booked.")
    elif location == "Station 2":
        if bus in bus_seats_st2 and bus_seats_st2[bus] > 0:
            bus_seats_st2[bus] -= 1
            print(bus_seats_st2)
            new_value = f"Avalaible Seats: {bus_seats_st1[bus]}"
            print(new_value)
            available_seats_label.configure(text=new_value)
        else:
            messagebox.showerror("Error", "Selected bus is fully booked.")

        ticket_number = random.randint(100000000, 999999999)
        no = str(ticket_number)

        current_time = datetime.now().strftime("%H:%M:%S")

        ticket_info = f"Name: {name}\nDeparture Location: {location}\nDate: {date}\n Price {price}\nTime: {current_time}\nBus: {bus}\nTicket Number: {no} \n Departure Time:{departure_time}" 

        ticket_window = Toplevel(window)
        ticket_window.minsize(width=400, height=120)
        ticket_window.title("Bus Ticket")
        ticket_window.configure(bg='white')

        name_label = Label(ticket_window, bg='white', fg='black', font=("Arial", 14), text=f"Name: {name}")
        name_label.pack()
        
        location_label = Label(ticket_window, bg='white', fg='black', font=("Arial", 14), text=f"Departure Location: {location}")
        location_label.pack()
        
        date_label = Label(ticket_window, bg='white', fg='black', font=("Arial", 14), text=f"Date: {date}")
        date_label.pack()

        current_time_label = Label(ticket_window, bg='white', text=f" Time: {current_time}" ,fg='black', font=("Arial", 14))
        current_time_label.pack()
        
        bus_label = Label(ticket_window, bg='white', fg='black', font=("Arial", 14), text=f"Bus: {bus}")
        bus_label.pack()

        price_label = Label(ticket_window, bg='white', fg='black', font=("Arial", 14), text=f"Price: {price}")
        price_label.pack()
        
        dep_time_label = Label(ticket_window, bg='white', fg='black', font=("Arial", 14), text=f"Departure Time:{departure_time}")
        dep_time_label.pack()

        # Create a label to display the ticket number
        ticket_number_label = Label(ticket_window, bg='white', fg='black', font=("Arial", 14), text=f"Ticket Number: {no}")
        ticket_number_label.pack()
        # Save ticket information to a file
        save_ticket_info(ticket_info)
    else:
        messagebox.showerror("Error", "Selected bus is fully booked.")


# Create a button to generate a new ticket number
generate_button = Button(window, bg='white', fg='black', width=30, font=("Arial", 12), text="Generate Ticket",
                         command=generate_ticket)
generate_button.place(x=350, y=600)

# Input portion
try:
    input_frame = Frame(window, bg='white')
    lab = Label(input_frame, text='FILL THE GIVEN FORM', bg='white', fg='black', font=("Arial", 20, "bold"))
    lab.pack(side='top')
    name_label = Label(input_frame, text='Name:', bg='white', fg='black', font=("Arial", 14))
    name_label.pack(side='left')
    name_entry = Entry(input_frame, width=50, bd=7, font=('Arial 12'))
    name_entry.pack(side='right')
except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Departure frame
dep_frame = Frame(window, bg='white')
location_label = Label(dep_frame, text="Departure Location:", bg='white', fg='black', font=("Arial", 14))
location_label.pack(side='left')
location_combobox = ttk.Combobox(dep_frame, values=["Station 1","Station 2"], width=30, font=('Arial 14'))
location_combobox.set("Select Station")

location_combobox.pack(side='right')

# Date
date_frame = Frame(window, bg='white')
date_label = Label(date_frame, text="Date:", bg='white', fg='black', font=("Arial", 14))
date_label.pack(side='left')
current_date = date.today()
date_combobox = ttk.Combobox(date_frame , width=14, values=[current_date.strftime("%Y-%m-%d")], font=("Arial", 14))
date_combobox.current(0)
date_combobox.pack(side='right')
input_frame.place(x=200, y=400)
dep_frame.place(x=200, y=470)
date_frame.place(x=200, y=530)


#price
price_frame = Frame(window, bg='white')
price_label = Label(price_frame, text="Price:", bg='white', fg='black', font=("Arial", 14))
price_label.pack(side='left')
price_combobox = ttk.Combobox(price_frame , width=14, values=["30.0 Rs"], font=("Arial", 14))
price_combobox.current(0)
price_combobox.pack(side='right')
price_frame.place(x=200, y=560)
# Bus frame
bus_frame = Frame(window, bg='white')
bus_label = Label(bus_frame, text="Bus:", bg='white', fg='black', font=("Arial", 14))
bus_label.pack(side='left')


bus_combobox1 = ttk.Combobox(bus_frame, width=15, font=('Arial 14'))
bus_combobox1.set("Select a bus")
# Set the initial values based on the selected location
def set_bus_values(*args):
    selected_location = location_combobox.get()
    if selected_location == "Station 1":
        bus_combobox1['values'] = list(bus_seats_st1.keys())
    elif selected_location == "Station 2":
        bus_combobox1['values'] = list(bus_seats_st2.keys())
    bus_combobox1.current(0)

# Call the set_bus_values function when the location selection changes
location_combobox.bind("<<ComboboxSelected>>", set_bus_values)

bus_combobox1.pack(side='right')
bus_frame.place(x=200, y=500)

#departure time
try:
    departure_time_frame = Frame(window, bg='white')

    departure_time_label = Label(departure_time_frame, text="Departure Time:", bg='white', fg='black', font=("Arial", 14))
    departure_time_label.pack(side='left')

    departure_time_combobox1 = ttk.Combobox(departure_time_frame, width=12, font=('Arial 14'))
    departure_time_combobox1.pack(side='right')
    departure_time_frame.place(x=435, y=500)
    
except NameError as ne:
    messagebox.showerror("Error", f"NameError: {str(ne)}")
except AttributeError as ae:
    messagebox.showerror("Error", f"AttributeError: {str(ae)}")
except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {str(e)}")



def set_dep_time(*args):
    selected_bus = bus_combobox1.get()
    selected_location = location_combobox.get()
    if selected_location == "Station 1":
        if selected_bus == list(bus_seats_st1.keys())[0]:
            departure_time_combobox1['values'] = list(dep_time_st1.values())[0]
        elif selected_bus == list(bus_seats_st1.keys())[1]:
            departure_time_combobox1['values'] = list(dep_time_st1.values())[1]
        elif selected_bus == list(bus_seats_st1.keys())[2]:
            departure_time_combobox1['values'] = list(dep_time_st1.values())[2]
        elif selected_bus == list(bus_seats_st1.keys())[3]:
            departure_time_combobox1['values'] = list(dep_time_st1.values())[3]
        elif selected_bus == list(bus_seats_st1.keys())[4]:
            departure_time_combobox1['values'] = list(dep_time_st1.values())[4]    
    elif selected_location == "Station 2":
       if selected_bus == list(bus_seats_st2.keys())[0]:
            departure_time_combobox1['values'] = list(dep_time_st2.values())[0]
       elif selected_bus == list(bus_seats_st2.keys())[1]:
            departure_time_combobox1['values'] = list(dep_time_st2.values())[1]
       elif selected_bus == list(bus_seats_st2.keys())[2]:
            departure_time_combobox1['values'] = list(dep_time_st2.values())[2]
       elif selected_bus == list(bus_seats_st2.keys())[3]:
            departure_time_combobox1['values'] = list(dep_time_st2.values())[3]
       elif selected_bus == list(bus_seats_st2.keys())[4]:
            departure_time_combobox1['values'] = list(dep_time_st2.values())[4]
    departure_time_combobox1.current(0)

# Call the set_bus_values function when the location selection changes
bus_combobox1.bind("<<ComboboxSelected>>", set_dep_time)
# Run the main window's event loop
window.mainloop()
