import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
print(f"Name: {os.getenv('STUDENT_NAME')} | ID: {os.getenv('STUDENT_ID')}")

root = tk.Tk()
root.withdraw()  # hide the empty tkinter window
path = filedialog.askopenfilename(
    title="Select a CSV file",
    filetypes=[("CSV files", "*.csv")]
)

if path:
    df = pd.read_csv(path)
    print(df.head(3))  # first three rows
else:
    print("No file selected.")