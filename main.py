import logging
import requests
import time


while True:
    interruption = requests.get('http://169.254.169.254/latest/meta-data/spot/instance-action');
    rebalance = requests.get('http://169.254.169.254/latest/meta-data/events/recommendations/rebalance');
    if '404' in interruption.text and '404'in rebalance.text:
      logging.info("No interruption is coming.... The application can continue working...")
    
    if '404' not in interruption.text:
      logging.warning("EC2 Spot Instance interruption notice received... Will not read a message from the queue...")
      time.sleep(10)
        
    if '404' not in rebalance.text:
      logging.warning("EC2 Spot Instance Rebalance notice received... Will not read a message from the queue...")
      time.sleep(10)

