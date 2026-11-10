from flask import Flask, jsonify, send_from_directory
import random, time

app = Flask(__name__)

balance = 1000.0
trade_count = 0
bot_running = False

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/status')
def status():
    global balance, trade_count
    if bot_running:
        profit = random.uniform(-5, 12)
        balance += profit
        trade_count += 1
    return jsonify({
        "balance": round(balance, 2),
        "trades": trade_count,
        "running": bot_running,
        "time": time.strftime("%H:%M:%S")
    })

@app.route('/api/start')
def start():
    global bot_running
    bot_running = True
    return jsonify({"status": "PUNISHER STARTED"})

@app.route('/api/stop')
def stop():
    global bot_running
    bot_running = False
    return jsonify({"status": "PUNISHER STOPPED"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
