import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.dates import HourLocator, DateFormatter
import random
import datetime
import mysql.connector

class FitnessApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fitness App")

        # Variables
        self.goal = 10000
        self.points = 0

        # Fetch user details from MySQL database
        self.user_details = self.fetch_user_details()

        # Example steps data for each hour of the day
        self.generate_realistic_steps_data()

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Line Chart
        line_frame = ttk.Frame(self.notebook)
        self.notebook.add(line_frame, text='Daily steps')
        self.line_chart(line_frame)

        # Bar Chart
        bar_frame = ttk.Frame(self.notebook)
        self.notebook.add(bar_frame, text='Weekly steps')
        self.bar_chart(bar_frame)

        # Motivational Quote
        quote_frame = ttk.Frame(self.notebook)
        self.notebook.add(quote_frame, text='Motivational Quote')
        self.motivational_quote(quote_frame)

        # BMI Calculator
        bmi_frame = ttk.Frame(self.notebook)
        self.notebook.add(bmi_frame, text='BMI Calculator')
        self.bmi_calculator(bmi_frame)

    def fetch_user_details(self):
        try:
            # Replace these values with your actual MySQL database connection details
            db_config = {
                'host': 'your_database_host',
                'user': 'your_username',
                'password': 'your_password',
                'database': 'your_database_name',
            }

            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Replace this query with your actual query to fetch user details
            query = "SELECT first_name, last_name FROM your_user_table WHERE user_id = 1;"
            cursor.execute(query)

            # Fetch the result
            result = cursor.fetchone()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            return result

        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching user details from the database: {str(e)}")
            return []

    def generate_realistic_steps_data(self):
        # Generate realistic hourly steps data
        sleep_start = 22  # Sleep starts at 22:00 (10:00 PM)
        sleep_duration = 9  # Sleep duration is 9 hours
        meal_breaks = [2, 5, 10, 14, 18]  # Meal breaks at 2, 5, 10, 14, and 18 hours

        self.steps_data = []
        for hour in range(24):
            if hour in meal_breaks:
                # Reduce steps during meal breaks
                self.steps_data.append(random.randint(200, 500))
            elif hour >= sleep_start and hour < sleep_start + sleep_duration:
                # Reduce steps during sleep hours
                self.steps_data.append(random.randint(0, 100))
            else:
                # Normal steps during waking hours
                self.steps_data.append(random.randint(800, 1200))

    def get_hours(self):
        # Generate datetime objects for each hour from 00:00 to 23:59
        hours = [datetime.datetime(2023, 1, 1, hour) for hour in range(24)]
        return hours

    def line_chart(self, frame):
        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)

        ax.plot(self.get_hours(), self.steps_data, marker='o', linestyle='-', color='orange')
        ax.set_title('Steps Per Hour', color='orange')
        ax.set_xlabel('Time of the Day', color='orange')
        ax.set_ylabel('Steps', color='orange')
        ax.xaxis.set_major_locator(HourLocator())
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))

        # Rotate x-axis labels for better readability
        for label in ax.get_xticklabels():
            label.set_rotation(45)

        # Display user details
        self.display_user_details(frame)

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(expand=True, fill='both')

    def bar_chart(self, frame):
        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)

        # Days of the week
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        ax.bar(days, self.weekly_steps_data, color='orange')
        ax.set_title('Steps per Day', color='orange')
        ax.set_xlabel('Day of the Week', color='orange')
        ax.set_ylabel('Steps', color='orange')

        # Display user details
        self.display_user_details(frame)

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(expand=True, fill='both')

    def motivational_quote(self, frame):
        quote_label = ttk.Label(frame, text="", font=('Arial', 20), wraplength=400, foreground='orange')
        quote_label.pack(expand=True, fill='both')

        frame.update_idletasks()
        quote_label.place(in_=frame, anchor="center", relx=0.5, rely=0.5)

        # Display user details
        self.display_user_details(frame)

        self.update_quote(quote_label)

    def update_quote(self, quote_label):
        quotes = [
            "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
            "The only bad workout is the one that didn't happen.",
            "Success is walking from failure to failure with no loss of enthusiasm.",
            "Your body can stand almost anything. It's your mind that you have to convince.",
            "Don't stop when you're tired. Stop when you're done."
        ]

        random_quote = random.choice(quotes)
        quote_label.config(text=random_quote)
        self.master.after(30000, lambda: self.update_quote(quote_label))

    def bmi_calculator(self, frame):
        class BMIApp:
            def __init__(self, master):
                self.master = master

                # Variables
                self.weight_var = tk.DoubleVar()
                self.height_var = tk.DoubleVar()
                self.gender_var = tk.StringVar(value='male')  # Default gender is male

                # Widgets
                weight_label = ttk.Label(master, text="Weight (kg):")
                weight_entry = ttk.Entry(master, textvariable=self.weight_var)

                height_label = ttk.Label(master, text="Height (m):")
                height_entry = ttk.Entry(master, textvariable=self.height_var)

                gender_label = ttk.Label(master, text="Gender:")
                gender_combobox = ttk.Combobox(master, textvariable=self.gender_var, values=['male', 'female'])

                calculate_button = ttk.Button(master, text="Calculate BMI", command=self.calculate_bmi)

                # Layout
                weight_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
                weight_entry.grid(row=0, column=1, padx=10, pady=5)

                height_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
                height_entry.grid(row=1, column=1, padx=10, pady=5)

                gender_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
                gender_combobox.grid(row=2, column=1, padx=10, pady=5)

                calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

            def calculate_bmi(self):
                try:
                    weight = self.weight_var.get()
                    height = self.height_var.get()
                    gender = self.gender_var.get()

                    if weight <= 0 or height <= 0:
                        messagebox.showwarning("Invalid Input", "Weight and height must be positive numbers.")
                        return

                    bmi = self.calculate_bmi_value(weight, height, gender)
                    category = self.get_bmi_category(bmi)

                    messagebox.showinfo("BMI Result", f"Your BMI is {bmi:.2f}\nCategory: {category}")
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            def calculate_bmi_value(self, weight, height, gender):
                if gender == 'male':
                    # BMI formula for males
                    bmi = weight / (height ** 2)
                elif gender == 'female':
                    # BMI formula for females
                    bmi = 1.3 * weight / (height ** 2)
                else:
                    raise ValueError("Invalid gender. Please select 'male' or 'female'.")

                return bmi

            def get_bmi_category(self, bmi):
                if bmi < 18.5:
                    return "Underweight"
                elif 18.5 <= bmi < 24.9:
                    return "Normal weight"
                elif 25 <= bmi < 29.9:
                    return "Overweight"
                else:
                    return "Obese"

        # Create an instance of the embedded BMIApp class
        bmi_app = BMIApp(frame)

        # Display user details
        self.display_user_details(frame)

    def display_user_details(self, frame):
        # Display user details in the top-left corner of the frame
        user_label = ttk.Label(frame, text=f"Welcome, {self.user_details[0]} {self.user_details[1]}",
                               font=('Arial', 12), foreground='blue')
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

    # ... (remaining existing code)

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.geometry("600x400")
    root.mainloop()
