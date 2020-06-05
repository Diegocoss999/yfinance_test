import tkinter as tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
def plot(symbol):
    pass
    # try:
    #     d1m = pd.read_csv('data/'+symbol+"_1m_macd.csv")
    #     d2m= pd.read_csv('data/'+symbol+"_2m.csv")
    #     d1h= pd.read_csv('data/'+symbol+"_1h.csv")
    #     d1d = pd.read_csv('data/'+symbol+"_1d.csv")
    #     plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #     plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    #     """raw data"""
    #     plt.plot(d1m[1:-1]['Datetime'], d1m[1:-1]['Close'], label='1m') # normal
    #     # plt.plot(d2m[1:-1]['Datetime'], d2m[1:-1]['Close'], label='2m')# normal
    #     # plt.plot(d1h[1:-1]['Date'], d1h[1:-1]['Close'], label='1h')# normal
    #     # plt.plot(d1d[1:-1]['Date'], d1d[1:-1]['Close'], label='1d') #
    #     """moving average"""
    #     # plt.plot(d1m[1:-1]['Datetime'], d1m[1:-1]['moving average 10'], label='1m_av')
    #     l1 = 'ema 12-26'
    #     plt.plot(d1m[1:-1]['Datetime'], d1m[1:-1][l1], label=l1)
    #     l2 = 'ema 9'
    #     plt.plot(d1m[1:-1]['Datetime'], d1m[1:-1][l2], label=l2)
    #     """ewm"""
    #     # plt.plot(d1m[1:-1]['Datetime'], d1m[1:-1]['ewm 10'], label='1m_ewm_10')
    #     # plt.plot(days,y)
    #     plt.gcf().autofmt_xdate()
    #     plt.xlabel('Date')
    #     plt.ylabel('Price (open)')
    #     plt.title('Prediction plot')
    #     plt.legend()
    #     plt.show()
    # except(FileNotFoundError):
    #     pass
class Graph(Frame):    

    def __init__(self, parent, graphs = None):
        Frame.__init__(self, parent)
        Label( parent,text="Hello w").pack()
        self.graph = Frame(self)
        self.graph.pack()

        buttons = Frame(self)
        buttons.pack()
        self.left = Button(buttons, text="Prev", width=10, command=lambda: self.prev_1())
        self.left.grid(row=0, column=0)
        self.next = Button(buttons, text="Next", width=10, command=lambda: self.next_1())
        self.next.grid(row=0, column=1)
    def build_graph(self):
        pass
    def prev_1(self):
        print(':')
    def next_1(self):
        print(':')
    
def gui():
    root = tk.Tk()
    root.title('Anomaly Detection')
    root.geometry("1920x1080")
    f  = Graph(root)
    f.pack()
    # graph_frame = Frame(root)
    # graph_frame.pack()
    # self.f = Figure(figsize=(5, 5), dpi=100)

    # self.timeseries = self.f.add_subplot(111)

    # self.timeseries.set_title('Events', fontsize=16)
    # # a.set_title ("Time Series", fontsize=16)
    # self.timeseries.set_ylabel("Number of Events", fontsize=14)
    # self.timeseries.set_xlabel("Time (min)", fontsize=14)

    # self.canvas = FigureCanvasTkAgg(self.f, graph_frame)
    # self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    # toolbar = NavigationToolbar2Tk(self.canvas, graph_frame)
    # toolbar.update()
    # self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
gui()