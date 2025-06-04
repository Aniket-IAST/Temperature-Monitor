import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def launch_temperature_gui(df, normal_max=50, warning_max=75):
    color_map = {"NORMAL": "blue", "WARNING": "orange", "CRITICAL": "red"}
    colors = df["State"].map(color_map)
    window = tk.Tk()
    window.title("Temperature Monitoring System")
    window.geometry("900x500")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.scatter(df["Timestamp"], df["Temperature"], c=colors)
    ax.plot(df["Timestamp"], df["Temperature"], linestyle="--", alpha=0.4)
    ax.axhline(y=normal_max, color='blue', linestyle='--', label=f'Normal Max ({normal_max}°C)')
    ax.axhline(y=warning_max, color='orange', linestyle='--', label=f'Warning Max ({warning_max}°C)')
    ax.set_title("Temperature History with Zone Highlights")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    fig.autofmt_xdate()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    canvas.draw()
    window.mainloop()