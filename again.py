import tkinter as tk
from tkinter import Canvas
import random
import string

def generate_random_data(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_qr_matrix(data):
    size = 21
    qr_matrix = [[0] * size for _ in range(size)]

    for i in range(7):
        for j in range(7):
            if (i == 0 or i == 6 or j == 0 or j == 6) or (i >= 2 and i <= 4 and j >= 2 and j <= 4):
                qr_matrix[i][j] = 1
                qr_matrix[i][size - j - 1] = 1
                qr_matrix[size - i - 1][j] = 1

    data_length = len(data)
    for i in range(data_length):
        if i < size * size:
            qr_matrix[(i // size) % size][(i % size)] = 1 if data[i] != ' ' else 0

    return qr_matrix

def draw_qr(matrix):
    window = tk.Tk()
    window.title("QR Code")

    canvas_size = len(matrix) * 10
    canvas = Canvas(window, width=canvas_size, height=canvas_size)
    canvas.pack()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                x1 = j * 10
                y1 = i * 10
                x2 = x1 + 10
                y2 = y1 + 10
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    window.mainloop()

def show_qr():
    random_data = generate_random_data(10)
    qr_matrix = create_qr_matrix(random_data)
    draw_qr(qr_matrix)

show_qr()