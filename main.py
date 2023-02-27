import tkinter as tk

def show_info(option):
    for widget in window.winfo_children():
        widget.destroy()

    if option == 1:
        tk.Label(window, text="Solar photovoltaic (PV) panels and solar thermal panels are two different\n"
                              "types of solar panels used for different purposes.\n"
                              "Solar PV panels convert sunlight into electricity, while solar thermal panels\n"
                              "use sunlight to heat water or air for heating and hot water needs.\n"
                              "Photovoltaic cells made of semiconductor materials such as silicon convert\n"
                              "sunlight into direct current. An inverter then converts the DC electricity\n"
                              "into alternating current, which is used in homes and businesses.").pack()
    elif option == 2:
        tk.Label(window, text="Advantages of solar power include:\n"
                              "1. Renewable and sustainable source of energy\n"
                              "2. Reduces reliance on fossil fuels\n"
                              "3. Reduces greenhouse gas emissions\n"
                              "4. Cost-effective in the long run\n"
                              "5. Can be used in remote locations\n"
                              "6. Increases energy independence and security\n"
                              "7. Low maintenance and operating costs\n"
                              "8. Modular and scalable, allowing easy expansion\n"
                              "9. Provides reliability and stability in grid-tied systems\n"
                              "10. Supports local job creation and economic growth\n" ).pack()
    elif option == 3:
        tk.Label(window, text="Electricity from solar energy is produced in the following steps:\n"
                              "1. Sunlight absorbed by solar panels which are made up of photovoltaic (PV) cells.\n"
                              "1. Photons knocks electrons from atoms in PV cell, generating DC electricity\n"
                              "2. The DC electricity is passed through an inverter, which converts it into AC electricity\n"
                              "3. The AC electricity is then sent to a switchboard for distribution\n"
                              "4. Excess electricity can be stored in batteries for later use.").pack()
    else:
        tk.Label(window, text="Interesting facts about Solar Energy:\n"
                              "1. The sun can reach temperatures higher than 15,000,000°C\n"
                              "2. Sunlight is a source of vitamin D, which helps keep bones, teeth and muscles healthy\n"
                              "3. The sun sends over 170,000 terawatts to Earth continually: more energy than we can use\n"
                              "4. Ancient Roman and Greek architects used passive solar power to warm homes\n"
                              "5. The first solar cell was designed by Swiss Scientist Horace-Benedict de Saussure in 1767.\n"
                              "6. In 1905, Einstein published a work here he studied the photoelectric effect. \n"
                              "7. In London 1960, the first solar car was introduced, with a 72-volt battery..\n"
                              "8. During 2018, the UK generated 3.9% of its total electricity using solar power. \n"
                              "9. China is the world leader in solar energy with over 100 GW of installed PV cells\n"
                              "10. In 2020, The UK enjoyed its sunniest March since 1929, with 166 hours of sunshine.\n").pack()

    tk.Button(window, text="Back", command=show_main_menu, highlightbackground="black").pack()

def show_main_menu():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Button(window, text="How does Solar work?", command=lambda: show_info(1), highlightbackground="black").pack()
    tk.Button(window, text="Advantages of Solar Power", command=lambda: show_info(2), highlightbackground="black").pack()
    tk.Button(window, text="How is electricity from Solar produced?", command=lambda: show_info(3), highlightbackground="black").pack()
    tk.Button(window, text="Facts about Solar Power", command=lambda: show_info(4), highlightbackground="black").pack()

    solar_panel_image = tk.PhotoImage(file="solar_panel.png")
    window.solar_panel_image = solar_panel_image
    tk.Label(window, image=solar_panel_image, highlightbackground="black").pack(pady=10)


window = tk.Tk()
window.geometry("600x500")
window.config(bg='black')
window.title("SunVault Solar Briefcase")

show_main_menu()

window.mainloop()
