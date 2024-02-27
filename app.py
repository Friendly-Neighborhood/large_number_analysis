from flask import Flask, request, render_template, jsonify
import numpy as np
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def find_longest_sequences(numbers):
    increasing_seq, decreasing_seq = [], []
    current_inc_seq, current_dec_seq = [numbers[0]], [numbers[0]]
    
    for i in range(1, len(numbers)):
        # Зростаюча послідовність
        if numbers[i] > numbers[i-1]:
            current_inc_seq.append(numbers[i])
            if len(current_inc_seq) > len(increasing_seq):
                increasing_seq = current_inc_seq.copy()
        else:
            current_inc_seq = [numbers[i]]
        
        # Спадна послідовність
        if numbers[i] < numbers[i-1]:
            current_dec_seq.append(numbers[i])
            if len(current_dec_seq) > len(decreasing_seq):
                decreasing_seq = current_dec_seq.copy()
        else:
            current_dec_seq = [numbers[i]]
    
    return increasing_seq, decreasing_seq

@app.route('/upload', methods=['POST'])
def upload_file():
    start_time = time.time() # Фіксуємо час початку обробки
    file = request.files['file']
    if file:
        # Перетворення файлу в список чисел
        numbers = np.loadtxt(file, dtype=int)
        # Обчислення необхідних статистик і конвертація їх у стандартні типи Python
        max_val = np.max(numbers).item()
        min_val = np.min(numbers).item()
        median_val = np.median(numbers).item()
        mean_val = np.mean(numbers).item()
        increasing_seq, decreasing_seq = find_longest_sequences(numbers)
        # Для опціональних завдань потрібно буде реалізувати додаткову логіку
        
        processing_time = time.time() - start_time  # Обчислення часу обробки
        
        return jsonify({
            'max': max_val,
            'min': min_val,
            'median': median_val,
            'mean': mean_val,
            'longest_increasing_sequence': [int(x) for x in increasing_seq],  # Конвертація кожного елемента до int
            'longest_decreasing_sequence': [int(x) for x in decreasing_seq],  # Конвертація кожного елемента до int
            'processing_time': processing_time # Додавання часу обробки до відповіді
        })

if __name__ == '__main__':
    app.run(debug=True)