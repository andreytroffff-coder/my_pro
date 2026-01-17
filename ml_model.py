# Импортируем всё необходимое (как «включить станки на заводе»)
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# Загружаем данные — картинки цифр (28x28 пикселей)
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Говорим сети: «Пиксели от 0 до 255 преврати в 0.0–1.0»
train_images = train_images / 255.0
test_images = test_images / 255.0

# Создаём сеть: 3 слоя как «сборочная линия»
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # 1. Расплющиваем картинку в ленту
    layers.Dense(128, activation='relu'),  # 2. Станок с 128 «руками»
    layers.Dense(10, activation='softmax') # 3. Выход: 10 корзин для цифр
])

# Говорим сети, как учиться
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Учим сеть 5 эпох (5 проходов по всем данным)
model.fit(train_images, train_labels, epochs=5)

# Проверяем точность на тестовых данных
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"\nТочность: {test_acc * 100:.2f}%")