import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.logs"


logs_path = os.path.join(os.getcwd(), "logs")


os.makedirs(logs_path, exist_ok=True)


log_file_path = os.path.join(logs_path, log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == '__main__':
    try:
        logging.info("Logging has started")
        # You can log other information or exceptions here
    except Exception as e:
        logging.error(f"Error occurred: {e}")
