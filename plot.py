import tkinter as tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

'''my files'''
import download
'''weird matlab plot'''
import matplotlib
matplotlib.use("TkAgg")
if True:
    from matplotlib.figure import Figure
    from matplotlib import *
    from matplotlib.backends import *
    from matplotlib.backends.backend_tkagg import *

"""non tkinter plots"""
def sub_plot(subplot, symbol, type,df ):
    pass
def plot(symbol, df):
    try:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
        """raw data"""
        
        plt.gcf().autofmt_xdate()
        plt.xlabel('Date')
        plt.ylabel('Price (open)')
        plt.title('Prediction plot')
        plt.legend()
        plt.show()
    except(FileNotFoundError):
        pass
"""gui with some nice plots"""
class Graph(Frame):
    def __init__(self, parent, graphs):
        Frame.__init__(self, parent)
        self.graphs = graphs

        Label( parent,text="Hello w").pack()

        self.graph = Frame(self)
        self.graph.pack()
        self.build_graph(graphs)

        buttons = Frame(self)
        buttons.pack()

        self.left = Button(buttons, text="Prev", width=10, command=lambda: self.prev_1())
        self.left.grid(row=0, column=0)
        self.next = Button(buttons, text="Next", width=10, command=lambda: self.next_1())
        self.next.grid(row=0, column=1)

    def build_graph(self, df):

        # for strat in list(df.keys()):
        #     for interval in list(df[strat].keys()):
        #         df[strat][interval]
        # using the variable ax for single a Axes
        '''
        fig, ax = plt.subplots()

        # using the variable axs for multiple Axes
        fig, axs = plt.subplots(2, 2)

        # using tuple unpacking for multiple Axes
        fig, (ax1, ax2) = plt.subplot(1, 2)
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplot(2, 2)
        '''
        self.f = Figure(figsize=(10, 4))

        self.plot = self.f.add_subplot(111)

        self.plot.set_title('Invest', fontsize=16)
        # a.set_title ("Time Series", fontsize=16)
        self.plot.set_ylabel("Performance", fontsize=14)
        self.plot.set_xlabel("Time (min)", fontsize=14)
        # self.plot.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        # self.plot.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
        self.plot.plot(df['macd']['1m']['Datetime'], df['macd']['1m']['Close'])
        self.plot.set_xticklabels([])
        # self.plot.gca().axes.get_yaxis().set_visible(False)
        self.canvas = FigureCanvasTkAgg(self.f, self.graph)
        self.canvas.get_tk_widget().grid(row=0,column=0)
        self.canvas.draw()
        # self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    def prev_1(self):
        pass
    def next_1(self):
        pass
    def sub_plot(self, subplot, symbol, type,df ):
        pass
        # figure = Figure(figsize=(5, 4), dpi=100)
        # figure.align_xlabels()
        # plot  = figure.add_subplot(2, 1)
        # figure.get
        # canvas = FigureCanvasTkAgg(figure, subplot)
        # canvas.get_tk_widget().grid(row=0, column=0)
        # '''plot ploting'''
        # plot.plot(x, y, color="blue", marker="x", linestyle="")
    def plot(self, symbol, df):
        pass
def gui(df):
    root = tk.Tk()
    root.title('Anomaly Detection')
    root.geometry("1920x1080")
    f  = Graph(root,df)
    f.pack()
    # graph_frame = Frame(root)
    # graph_frame.pack()
    # self.f = Figure(figsize=(5, 5), dpi=100)

    # self.plot = self.f.add_subplot(111)

    # self.plot.set_title('Events', fontsize=16)
    # # a.set_title ("Time Series", fontsize=16)
    # self.plot.set_ylabel("Number of Events", fontsize=14)
    # self.plot.set_xlabel("Time (min)", fontsize=14)

    # self.canvas = FigureCanvasTkAgg(self.f, graph_frame)
    # self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    # toolbar = NavigationToolbar2Tk(self.canvas, graph_frame)
    # toolbar.update()
    # self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()