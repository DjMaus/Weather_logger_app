# excel_logger.py
import pandas as pd
from datetime import datetime

class ExcelLogger:
    def __init__(self):
        self.filename = "weather_log.xlsx"
        
    def log_weather(self, data):
        try:
            # Try to read existing file
            existing_df = pd.read_excel(self.filename)
            updated_df = pd.concat([existing_df, data], ignore_index=True)
        except FileNotFoundError:
            # Create new file if it doesn't exist
            updated_df = data
            
        updated_df.to_excel(self.filename, index=False)