from PIL import Image, ImageTk
import tkinter as tk
import random


# Функция для создания цветного изображения
def create_color_image(width, height):
    # Создаем новое изображение в режиме 'P' (палитра)
    image = Image.new('P', (width, height))

    # Генерируем палитру цветов (256 цветов)
    palette = []
    for i in range(256):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        palette.extend((r, g, b))

    # Устанавливаем палитру в изображение
    image.putpalette(palette)

    # Заполняем изображение случайными индексами палитры
    for x in range(width):
        for y in range(height):
            index = random.randint(0, 255)
            image.putpixel((x, y), index)

    return image


# Функция для отображения изображения в окне
def show_image(image):
    root = tk.Tk()
    root.title("Цветное изображение")

    # Преобразуем изображение в формат, который может быть показан в tkinter
    img_tk = ImageTk.PhotoImage(image)

    # Создаем метку для отображения изображения
    label = tk.Label(root, image=img_tk)
    label.pack()

    # Выводим двоичный код пикселей в консоль
    width, height = image.size
    binary_data = []

    for x in range(width):
        for y in range(height):
            index = image.getpixel((x, y))
            binary_data.append(format(index, '08b'))  # Двоичный код 8 бит

    print("Двоичный код пикселей:")
    print(binary_data)

    # Запускаем главный цикл приложения
    root.mainloop()


# Основная программа
if __name__ == "__main__":
    width, height = 100, 100  # Задаем размеры изображения
    color_image = create_color_image(width, height)  # Создаем изображение
    show_image(color_image)  # Отображаем изображение в окне