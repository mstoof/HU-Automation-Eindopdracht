from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def dashboard():
    """
    De function is de main directory voor de webserver, alle gegevens worden opgehaald doormiddel van Javascript
    Dus de function heeft geen input requirements.
    :return: Dashboard.html -> /
    """
    return render_template('dashboard.html')

@app.route('/report', methods=['POST'])
def receive_report():
    """
    De function kan alleen gebruikt worden voor de POST requests van de Salt Agents, de gegevens die hier mee gegeven
    worden zijn nodig om door javascript de statestieken te laden.

    Store_data is een functie die de gegevens opslaat in een SQLlite3 database.
    :return: HTML succesmelding
    """
    data = request.json
    print(data)
    store_data(data)
    return jsonify({'status': 'success'}), 200

def store_data(data):
    """
    Deze function ontvangt de gegevens van de receive_report functie. De functie slaat de gegevens op in de database.
    :param data: Dit is een voorbeeld van alle data die wordt meegegeven, niet alles wordt op het dashboard getoont om
    te voorkomen dat het te druk wordt op de dashboard.
    {
    'cpu_percent': 3.0,
    'memory_info': {'total': 7966388224, 'available': 6740779008, 'percent': 15.4,
    'used': 1017729024, 'free': 6112514048, 'active': 385531904, 'inactive': 1190404096, 'buffers': 6561792,
    'cached': 829583360, 'shared': 28524544, 'slab': 139976704}, 'disk_info': {'total': 17609785344,
    'used': 4473065472, 'free': 13136719872, 'percent': 25.4},
    'ip_address': '192.168.1.144'}
    :return: Er hoeft niks gereturned te worden, alles wat we nodig hebben wordt in de database opgeslagen.
    """
    connection = sqlite3.connect('static/management.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS system_stats (
        id INTEGER PRIMARY KEY,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        cpu_usage REAL,
        memory_usage REAL,
        disk_usage REAL
    )
    ''')

    cursor.execute('INSERT INTO system_stats (cpu_usage, memory_usage, disk_usage) VALUES (?, ?, ?)',
                   (data['cpu_percent'], data['memory_info']['percent'], data['disk_info']['percent']))

    connection.commit()
    connection.close()

@app.route('/stats/cpu', methods=['GET'])
def cpu_stats():
    """
    Deze functie haalt de gegevens uit de database en zet dit om naar JSON wat makkelijk leesbaar is voor Javascript.
    :return: een gejsonified variant van alle CPU data.
    """
    cpu_data = retrieve_stats('cpu_usage')
    return jsonify(cpu_data)

@app.route('/stats/memory', methods=['GET'])
def memory_stats():
    """
    Deze functie haalt de gegevens uit de database en zet dit om naar JSON wat makkelijk leesbaar is voor Javascript.
    :return: een gejsonified variant van alle Memory data.
    """
    memory_data = retrieve_stats('memory_usage')
    return jsonify(memory_data)

@app.route('/stats/disk', methods=['GET'])
def disk_stats():
    """
    Deze functie haalt de gegevens uit de database en zet dit om naar JSON wat makkelijk leesbaar is voor Javascript.
    :return: een gejsonified variant van alle Disk data.
    """
    disk_data = retrieve_stats('disk_usage')
    return jsonify(disk_data)

def retrieve_stats(stat_type):
    """
    Deze functie haalt alle statestieken uit de database, dus niet alle de lossen statestieken.
    :param stat_type: Welke type wil je hebben
    :return: een dictionary met de timestamp en de waardes voor de CPU, Memory en Disk usage.
    """
    connection = sqlite3.connect('static/management.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT timestamp, {stat_type} FROM system_stats ORDER BY timestamp ASC LIMIT 100')
    rows = cursor.fetchall()
    connection.close()
    # Formatteer de gegevens voor de grafiek
    return [{'timestamp': row[0], 'value': row[1]} for row in rows]



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Runs the server on all interfaces on port 5000.
