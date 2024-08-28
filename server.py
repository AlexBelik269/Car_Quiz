from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sqlite3
import random

app = Flask(__name__)
CORS(app) 

fetched_questions = []

def fetch_questions(difficulty):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    if difficulty == 'NOOB':
        cursor.execute("SELECT id, question, option_a, option_b, option_c, option_d, correct_answer FROM questions WHERE difficulty = 'easy'")
    elif difficulty == 'PROFI':
        cursor.execute("SELECT id, question, option_a, option_b, option_c, option_d, correct_answer FROM questions WHERE difficulty = 'hard'")
    else:
        return []

    all_questions = cursor.fetchall()
    available_questions = [q for q in all_questions if q not in fetched_questions]

    if len(available_questions) < 20:
        fetched_questions.clear()
        available_questions = all_questions

    random.shuffle(available_questions)
    selected_questions = available_questions[:20]
    fetched_questions.extend(selected_questions)

    conn.close()
    return selected_questions

@app.route('/questions', methods=['GET'])
def get_questions():
    difficulty = request.args.get('difficulty')
    if not difficulty:
        return jsonify({'error': 'Difficulty parameter is missing'}), 400

    questions = fetch_questions(difficulty)
    if not questions:
        return jsonify({'error': 'No questions found for the specified difficulty'}), 404

    question_list = [
        {
            'id': q[0],
            'question': q[1],
            'options': [q[2], q[3], q[4], q[5]],
            'correct_answer': q[6]
        }
        for q in questions
    ]
    return jsonify(question_list)

if __name__ == '__main__':
    app.run(debug=True)
