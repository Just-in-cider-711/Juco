import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import Vars
from Vars import r, g, b, y, number
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')
#  from matplotlib.figure import Figure

background_color = "#4ed0fc"
button_color = "#abd897"
#  Personality Color counters


#   Window Class
labels = ['Red', 'Green', 'Blue', 'Yellow']
sizes = [r, b, g, y]
colors = ["Red", "Green", "Blue", "Yellow"]
explode = (0, 0, 0, 0)


class WindowMaker:
    def __init__(self, name, width, height, title, color):
        # SELF NAME & Safety Net
        self.name = name
        if type(name) == str:
            pass
        elif type(name) != str:
            name = str(name)
        # SELF width & Safety Net
        self.width = width
        if type(width) == int:
            pass
        elif type(width) != int:
            width = len(width)
        # SELF height & Safety Net
        self.height = height
        if type(height) == int:
            pass
        elif type(height) != int:
            height = len(height)
        # SELF title & Safety Net
        self.title = title
        if type(title) == str:
            pass
        elif type(title) != str:
            title = str(title)
        # SELF Color & Safety Net
        self.color = color
        name = tk.Tk()
        name.title(title)
        name.geometry("{0}x{1}+0+0".format(width, height))
        name.maxsize(600, 600)

        #  Applying Background color To Window, Setting up fail Net
        try:
            name.config(bg=color)
        except ValueError:
            name.config(bg='white')
            print("Color Unknown, Defaulting to white")
        # MAIN CODE ________ BELOW _______ BELOW ____________ BELOW __________

        def start():
            name.destroy()

        def qquit():
            exit()

        start_button = tk.Button(name, text='Start', command=start, bg='green')
        quit_button = tk.Button(name, text='Quit', command=qquit, bg='red')

        start_button.place(x=width/4, y=height/2.5)
        quit_button.place(x=width/2 * 1.1, y = height/2.5)

        name.mainloop()


class MainWindowMaker:

    def __init__(self, name, width, height, title, color):
        # SELF NAME & Safety Net
        self.name = name
        if type(name) == str:
            pass
        elif type(name) != str:
            name = str(name)
        # SELF width & Safety Net
        self.width = width
        if type(width) == int:
            pass
        elif type(width) != int:
            width = len(width)
        # SELF height & Safety Net
        self.height = height
        if type(height) == int:
            pass
        elif type(height) != int:
            height = len(height)
        # SELF title & Safety Net
        self.title = title
        if type(title) == str:
            pass
        elif type(title) != str:
            title = str(title)
        # SELF Color & Safety Net
        self.color = color
        name = tk.Tk()
        name.title(title)
        name.geometry("{0}x{1}+0+0".format(width, height))
        name.maxsize(width, height)

        # Applying Background color To Window, Setting up fail Net
        try:
            name.config(bg=color)
        except ValueError:
            name.config(bg='white')
            print("Color Unknown, Defaulting to white")
        #
        #
        #
        #
        #
        # MAIN CODE ________ BELOW _______ BELOW ____________ BELOW __________
        #
        #
        #
        #  SETS UPS AND STUFF FOR QUESTIONS WINDOWS

        def question_one():
            print("Question one")
            title_label.config(text=title+" Question: " + str(number))
            red_button.config(text='I am Red')
            blue_button.config(text='I Am Blue')
            yellow_button.config(text='I am Yellow')
            green_button.config(text='I am Green')
            question_label.config(text='What Color Are you?')

        def question_two():
            print("Question one")
            title_label.config(text=title+" Question: " + str(number))
            red_button.config(text='')
            blue_button.config(text='')
            yellow_button.config(text='')
            green_button.config(text='')
            question_label.config(text='')

        def question_three():
            print("Question one")
            title_label.config(text=title+" Question: " + str(number))
            red_button.config(text='')
            blue_button.config(text='')
            yellow_button.config(text='')
            green_button.config(text='')
            question_label.config(text='')

        def question_four():
            print("Question one")
            title_label.config(text=title+" Question: " + str(number))
            red_button.config(text='')
            blue_button.config(text='')
            yellow_button.config(text='')
            green_button.config(text='')
            question_label.config(text='')

        def question_five():
            print("Question one")
            title_label.config(text=title+" Question: " + str(number))
            red_button.config(text='')
            blue_button.config(text='')
            yellow_button.config(text='')
            green_button.config(text='')
            question_label.config(text='')

        def question_six():
            print("Question one")
            title_label.config(text=title+" Question: " + str(number))
            red_button.config(text='')
            blue_button.config(text='')
            yellow_button.config(text='')
            green_button.config(text='')
            question_label.config(text='')

        def question_seven():
            print("Question one")
            title_label.config(text=title+" Question: " + str(number))
            red_button.config(text='')
            blue_button.config(text='')
            yellow_button.config(text='')
            green_button.config(text='')
            question_label.config(text='')

        def question_eight():
            print("Question one")
            title_label.config(text=title+" Question: " + str(number))
            red_button.config(text='')
            blue_button.config(text='')
            yellow_button.config(text='')
            green_button.config(text='')
            question_label.config(text='')

        def question_nine():
            print("Question one")
            title_label.config(text=title+" Question: " + str(number))
            red_button.config(text='')
            blue_button.config(text='')
            yellow_button.config(text='')
            green_button.config(text='')
            question_label.config(text='')

        def question_ten():
            print("Question one")
            title_label.config(text=title+" Question: " + str(number))
            red_button.config(text='')
            blue_button.config(text='')
            yellow_button.config(text='')
            green_button.config(text='')
            question_label.config(text='')

        # Ticker to keep count of what question were on!

        def red():
            global r, number
            r += 1
            number += 1
            print(r, number)

            if number == 1:
                question_one()
            elif number == 2:
                question_two()
            elif number == 3:
                question_three()
            elif number == 4:
                question_four()
            elif number == 5:
                question_five()
            elif number == 6:
                question_six()
            elif number == 7:
                question_seven()
            elif number == 8:
                question_eight()
            elif number == 9:
                question_nine()
            elif number == 10:
                question_ten()

        def blue():
            global b, number
            b += 1
            number += 1
            print(b, number)
            if number == 0:
                question_one()
            elif number == 2:
                question_two()
            elif number == 3:
                question_three()
            elif number == 4:
                question_four()
            elif number == 5:
                question_five()
            elif number == 6:
                question_six()
            elif number == 7:
                question_seven()
            elif number == 8:
                question_eight()
            elif number == 9:
                question_nine()
            elif number == 10:
                question_ten()

        def green():
            global g, number
            g += 1
            number += 1
            print(g, number)
            if number == 0:
                question_one()
            elif number == 2:
                question_two()
            elif number == 3:
                question_three()
            elif number == 4:
                question_four()
            elif number == 5:
                question_five()
            elif number == 6:
                question_six()
            elif number == 7:
                question_seven()
            elif number == 8:
                question_eight()
            elif number == 9:
                question_nine()
            elif number == 10:
                question_ten()

        def yellow():
            global y, number
            y += 1
            number += 1
            print(y, number)
            if number == 0:
                question_one()
            elif number == 2:
                question_two()
            elif number == 3:
                question_three()
            elif number == 4:
                question_four()
            elif number == 5:
                question_five()
            elif number == 6:
                question_six()
            elif number == 7:
                question_seven()
            elif number == 8:
                question_eight()
            elif number == 9:
                question_nine()
            elif number == 10:
                question_ten()

        #  TKINTER gui's and etc

        title_label = tk.Label(name, text=title+" Question: " + str(number),fg='black', bg=background_color)
        question_label = tk.Label(name, text='Question', bg=background_color)
        red_button = tk.Button(name, text='Red', command=red, bg=button_color)
        green_button = tk.Button(name, text='Green', command=green, bg=button_color)
        blue_button = tk.Button(name, text='Blue', command=blue, bg=button_color)
        yellow_button = tk.Button(name, text='Yellow', command=yellow, bg=button_color)

        # TKINTER FRAME for macholib pie chart
        dimensions_frame = 2
        pie_chart_frame = tk.Frame(name, width=width/dimensions_frame, height=height/dimensions_frame - 20, bg="#d7d3ff")

        '''
        try:
            donut.get_tk_widget().place(x=1000, y=11110)
            del donut
        except NameError:
            pass
'''
        plt.pie([r, b, g, y], explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, colors=colors)
        # CENTURE CIRCLE
        centre_circle = plt.Circle((0, 0), 0.75, color='Black', fc=background_color, linewidth=1.25)
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        fig.set_facecolor(background_color)
        donut = FigureCanvasTkAgg(fig, pie_chart_frame)


        '''
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        pie2 = FigureCanvasTkAgg(fig1, pie_chart_frame)
        #  plt.tight_layout()
        #  plt.show()
        '''
        # PLACING TKINTER GUI's
        title_label.place(x=0, y=0)
        question_label.place(x=1/width + width/10, y=height/2)
        red_button.place(x=1/width, y=height/2 + height/4)
        green_button.place(x=1/width + width/4, y=height/2 + height/4)
        blue_button.place(x=1/width + width/4 * 2, y=height/2 + height/4)
        yellow_button.place(x=1/width + width/4 * 3, y=height/2 + height/4)
        pie_chart_frame.place(x=width - width/dimensions_frame, y=0)
        donut.get_tk_widget().place(x=0, y=0)
        question_one()

#  start_window = WindowMaker("Window", 300, 300, "Personality Tester Start Up", "Blue")

main_window = MainWindowMaker("Window", 1200, 1000, "Personality Tester", background_color)
