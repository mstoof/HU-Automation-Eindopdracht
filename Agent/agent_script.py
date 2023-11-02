import datetime
import socket
import psutil
import requests
import time

MANAGEMENT_SERVER_URL = 'http://192.168.1.239:5000/report'

def gather_stats():
    """
    Haal alle gegevens op die worden gestuurd naar de master server.
    :return: dictionary met alle gegevens van hieronder.
    """
    stats = {
        'timestamp': datetime.datetime.now(),
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory_info': psutil.virtual_memory()._asdict(),
        'disk_info': psutil.disk_usage('/')._asdict(),
        'ip_address': socket.gethostbyname(socket.gethostbyname()),
    }
    return stats

def post_stats(stats):
    """
    Een POST request voor de API managementserver.
    :param stats: Statestieken die worden opgehaald door de function gather_stats
    :return: POST request naar de Managementserver.
    """
    response = requests.post(MANAGEMENT_SERVER_URL, json=stats)
    if response.status_code == 200:
        print('Data posted successfully')
    else:
        print('Failed to post data')

def main():
    """
    De main function die wordt gedraaid door de
    :return:
    """
    while True:
        stats = gather_stats()
        post_stats(stats)
        # Wait for 60 seconds before gathering the next set of stats
        time.sleep(60)

if __name__ == '__main__':
    main()
