import tkinter as tk

def show_info(option):
    for widget in window.winfo_children():
        widget.destroy()

    if option == 1:
        tk.Label(window, text="Solar power works by using the energy from the sun to produce electricity.\n"
                              "Photovoltaic (PV) cells made of semiconductor materials such as silicon convert\n"
                              "the sunlight into direct current (DC) electricity. An inverter then converts\n"
                              "the DC electricity into alternating current (AC) electricity, which is what\n"
                              "is used in homes and businesses.", font=("Helvetica", 12)).pack()
    elif option == 2:
        tk.Label(window, text="Advantages of solar power include:\n"
                              "1. Renewable and sustainable source of energy\n"
                              "2. Reduces reliance on fossil fuels\n"
                              "3. Reduces greenhouse gas emissions\n"
                              "4. Cost-effective in the long run\n"
                              "5. Can be used in remote locations\n"
                              "6. Increases energy independence and security.", font=("Helvetica", 12)).pack()
    elif option == 3:
        tk.Label(window, text="Electricity from solar energy is produced in the following steps:\n"
                              "1. Photovoltaic cells convert sunlight into DC electricity\n"
                              "2. The DC electricity is passed through an inverter, which converts it into AC electricity\n"
                              "3. The AC electricity is then sent to the electrical grid for distribution\n"
                              "4. Excess electricity can be stored in batteries for later use.", font=("Helvetica", 12)).pack()
    else:
        tk.Label(window, text="Solar photovoltaic (PV) panels and solar thermal panels are two different\n"
                              "types of solar panels used for different purposes.\n\n"
                              "Solar PV panels convert sunlight into electricity, while solar thermal panels\n"
                              "use sunlight to heat water or air for heating and hot water needs.\n\n"
                              "Both types of panels have their own advantages and disadvantages, and the\n"
                              "best type for a particular use will depend on the specific requirements.", font=("Helvetica", 12)).pack()

    tk.Button(window, text="Back", command=show_main_menu, bg="green", font=("Helvetica", 12)).pack()

def show_main_menu():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Button(window, text="How does solar power work?", command=lambda: show_info(1), bg="green", font=("Helvetica", 12)).pack()
    tk.Button(window, text="Advantages of Solar Power", command=lambda: show_info(2), bg="green", font=("Helvetica", 12)).pack()
    tk.Button(window, text="How is electricity from solar energy produced?", command=lambda: show_info(3), bg="green",
