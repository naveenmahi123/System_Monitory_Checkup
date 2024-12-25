import psutil
import logging

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 30
DISK_THRESHOLD = 30

def monitor_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage is normal: {cpu_usage}%")
    
    # Check memory usage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {memory_usage}%")
    else:
        logging.info(f"Memory usage is normal: {memory_usage}%")
    
    # Check disk usage
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High disk usage detected: {disk_usage}%")
    else:
        logging.info(f"Disk usage is normal: {disk_usage}%")
    
    # Check running processes
    process_count = len(psutil.pids())
    logging.info(f"Number of running processes: {process_count}")

if __name__ == "__main__":
    monitor_system_health()
