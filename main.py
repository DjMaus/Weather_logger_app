from weather_api import WeatherAPI
from excel_logger import ExcelLogger
from utils import format_temperature

def main():
    weather_api = WeatherAPI()
    excel_logger = ExcelLogger()
    
    # Get weather data
    weather_data = weather_api.get_current_weather()
    
    # Format data
    formatted_data = format_temperature(weather_data)
    
    # Log to Excel
    excel_logger.log_weather(formatted_data)

if __name__ == "__main__":
    main()