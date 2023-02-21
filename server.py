import os
import psutil

# Créer un tube nommé pour recevoir les requêtes du client
request_pipe = os.mkfifo('request_pipe', 0o666)

def get_memory_info():
    mem = psutil.virtual_memory()
    return f"Total : {mem.total / 2**20:.2f} Mo\nDisponible : {mem.available / 2**20:.2f} Mo\nUtilisé : {mem.used / 2**20:.2f} Mo"

def get_process_info():
    processes = []
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            process_id = proc.pid
            processes.append(f"{process_id} - {process_name}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return "\n".join(processes)

def get_cpu_info():
    cpu_percentages = psutil.cpu_percent(percpu=True)
    return "\n".join([f"CPU{i}: {percentage}%" for i, percentage in enumerate(cpu_percentages)])

while True:
    # Lire la requête du client
    request = os.open('request_pipe', os.O_RDONLY)
    data = os.read(request, 1024)
    os.close(request)

    # Traiter la requête en fonction de l'option sélectionnée par le client
    choice = data.decode()
    if choice == "1":
        break
    elif choice == "2":
        response = get_memory_info()
    elif choice == "3":
        response = get_process_info()
    elif choice == "4":
        response = get_cpu_info()
    else:
        response = "Option invalide"

    # Envoyer la réponse au client
    response_pipe = os.mkfifo('response_pipe', 0o666)
    response_fd = os.open('response_pipe', os.O_WRONLY)
    os.write(response_fd, response.encode())
    os.close(response_fd)