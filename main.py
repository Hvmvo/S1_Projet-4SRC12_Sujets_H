import os

def print_memory_info():
    # Use the 'free' command to get memory info
    memory_info = os.popen("free").read()
    print(memory_info)

def print_process_info():
    # Use the 'ps' command to get process info
    process_info = os.popen("ps").read()
    print(process_info)

def print_cpu_info():
    # Use the 'top' command to get CPU info
    cpu_info = os.popen("top").read()
    print(cpu_info)

def display_menu():
    # Print the menu
    print("1) Quit")
    print("2) Memory Information")
    print("3) Process Information")
    print("4) CPU Information")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        exit(0)
    elif choice == 2:
        print_memory_info()
    elif choice == 3:
        print_process_info()
    elif choice == 4:
        print_cpu_info()
    else:
        print("Invalid choice. Try again.")

while True:
    display_menu()