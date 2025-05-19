import psutil
import time
import signal
import sys

# CTRL+C işlemi yakalanınca yapılacak işlemi belirle
def handle_exit_signal(signal, frame):
    print("\nGüvenliğiniz Güvenliğimizdir.")
    print("\nGüvenlikli Günler Dileriz.")
    print("\n-ProcessGUARD")
    sys.exit(0)  # Programı düzgün bir şekilde sonlandırır

# Signal handler'ı kur
signal.signal(signal.SIGINT, handle_exit_signal)

def get_process_list():
    """Şu anki çalışan işlemlerin bir listesini döndüren fonksiyon."""
    processes = {}
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            processes[proc.info['pid']] = proc.info['name']
        except psutil.NoSuchProcess:
            pass
    return processes

def monitor_new_processes():
    """Yeni başlatılan işlemleri izleyen fonksiyon."""
    print("Process İzleyici Çalışıyor... Yeni işlemler başladıkça bildirilecektir.")
    initial_processes = get_process_list()
    print(f"Başlangıçta {len(initial_processes)} işlem çalışıyor.")

    while True:
        time.sleep(1)
        current_processes = get_process_list()
        new_processes = set(current_processes.keys()) - set(initial_processes.keys())

        if new_processes:
            for pid in new_processes:
                process_name = current_processes[pid]
                print(f"Yeni işlem başladı: PID={pid}, Adı={process_name}")

        initial_processes = current_processes

# Ana fonksiyon
def main():
    print("Program çalışıyor. CTRL+C ile durdurabilirsiniz.")
    monitor_new_processes()

if __name__ == "__main__":
    main()
