import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os

file_path=["media/file.xlsx","media/file.csv","media/file.xls"]

def load_data(file_path):
    file_path="media/"+file_path
    file_ext = os.path.splitext(file_path)[-1].lower()
    try:
        if file_ext == ".csv":
            data = pd.read_csv(file_path)
        elif file_ext in [".xls", ".xlsx"]:
            data = pd.read_excel(file_path, engine='openpyxl')
        else:
            raise ValueError("Unsupported file type. Only CSV or Excel files are allowed.")
        
        print("Data Loaded Successfully!")
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def clean_data(data):
    data.fillna(method='ffill', inplace=True)
    data.fillna(method='bfill', inplace=True)
    print("Missing values handled using forward and backward fill.")
    return data

def getDataList(fileName):
    data=load_data(fileName)
    data = clean_data(data)
    return data.columns.tolist()

def plot_with_matplotlib(file,x_col, y_col):
    data = load_data(file)
    data = clean_data(data)
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_col], data[y_col], marker='o', color='b', linestyle='--')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col} (Matplotlib)")
    plt.grid()
    plt.savefig('media/output.png', format='png')  # Save as an image
    print(f"Matplotlib plot saved as output.png")
    plt.close()

def generate_bar_chart(file,x_col, y_col):
    data = load_data(file)
    data = clean_data(data)
    plt.figure(figsize=(10, 6))
    plt.bar(data[x_col], data[y_col], color='skyblue')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col} (Bar Chart)")
    plt.savefig("media/output.png", format='png')  # Save as an image
    print(f"Bar chart saved as output.png")
    plt.close()


def generate_pie_chart(file,y_col):
    data = load_data(file)
    data = clean_data(data)
    plt.figure(figsize=(8, 8))
    data_counts = data[y_col].value_counts()
    plt.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
    plt.title(f"Pie Chart of {y_col}")
    plt.savefig("media/output.png", format='png')  # Save as an image
    print(f"Pie chart saved as output.png")
    plt.close()
