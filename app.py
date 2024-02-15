from flask import Flask, session, render_template, redirect, url_for, request, jsonify
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "Angela"

boggle_game = Boggle(board_size=6)


@app.route('/')
def home():
    board = boggle_game.make_board()
    session['board'] = board
    return redirect(url_for('display_board'))

@app.route('/board')
def display_board():
    board = session.get('board', None)
    if board is None:
        return redirect(url_for('home'))
    return render_template('board.html', board=board)

@app.route('/guess', methods=['POST'])
def handle_guess():
    guess = request.json['guess']
    board = session.get('board', [])
    result = boggle_game.check_valid_word(board, guess)
    
    messages = {
        "ok": "Great!, That is a valid word. ",
        "not-on-board": "Oops!, Word not on the board",
        "not-word": "Hmm, That is not a valid word"
    }
    
    return jsonify({"result": result, "message": messages[result]})

@app.route('/reshuffle', methods=['GET'])
def reshuffle():
    board = boggle_game.make_board()
    session['board'] = board
    return jsonify(board=board)
