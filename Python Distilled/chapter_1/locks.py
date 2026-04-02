import threading
import time

balance = 0
lock = threading.Lock() 
amount = 100000
def deposit():
    """Deposit money into the account. Blocks the thread while doing so."""

    global balance
    for _ in range(amount):
        temp_balance = balance
        time.sleep(0.0001)  # Simulate a delay
        balance = temp_balance + 1


def withdraw():
    """Withdraw money from the account. Blocks the thread while doing so."""

    global balance
    for _ in range(amount):
        temp_balance = balance
        time.sleep(0.0001)  # Simulate a delay
        balance = temp_balance - 1

def deposit_with_lock():
    """Deposit money into the account. Uses a lock to prevent race conditions."""

    global balance
    for _ in range(amount):
        
        with lock:
            temp_balance = balance
            time.sleep(0.0001)  # Simulate a delay
            balance = temp_balance + 1
            
def withdraw_with_lock():
    """Withdraw money from the account. Uses a lock to prevent race conditions."""

    global balance
    for _ in range(amount):
        with lock:
            temp_balance = balance
            time.sleep(0.0001)  # Simulate a delay
            balance = temp_balance - 1

if __name__ == "__main__":
    
    t1 = threading.Thread(target=deposit)
    t2 = threading.Thread(target=withdraw)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Final balance blocking:", balance)
    
    balance = 0  # Reset balance for the next test

    t1 = threading.Thread(target=deposit_with_lock)
    t2 = threading.Thread(target=withdraw_with_lock)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Final balance with lock:", balance)
