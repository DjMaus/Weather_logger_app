# Weather Data Logger

## Project Overview
The Weather Data Logger is a Python application that retrieves live weather data for a given location, processes it, and logs it into an Excel file for record-keeping. The goal is to create a tool for tracking weather conditions over time with minimal user interaction.

---

## Project Objectives
1. Fetch real-time weather data using a reliable API.
2. Allow user input for location (city name or coordinates).
3. Process and extract essential weather metrics:
   - Temperature
   - Humidity
   - Weather Description
   - Wind Speed
   - Timestamp
4. Log weather data into an Excel file with proper formatting and structure.
5. (Optional) Add data visualization features for logged weather trends.

---

## Technical Requirements

### Tools and Technologies
- **Programming Language**: Python
- **IDE/Editor**: Visual Studio Code
- **Version Control**: GitHub repository
- **Libraries**:
  - `requests`: API calls
  - `openpyxl`: Excel logging
  - `pandas`: Data manipulation (optional)
  - `matplotlib` or `seaborn` (optional): Data visualization

### Weather API Options
- OpenWeatherMap, WeatherAPI, AccuWeather, or NOAA API.


## Application Features

### Phase 1: Basic Weather Logger
- **Input**: Prompt the user for a location (city name).
- **Fetch**: Retrieve weather data from the API.
- **Process**: Parse JSON response for:
  - City name
  - Current temperature
  - Humidity
  - Weather condition description
  - Wind speed
  - Timestamp
- **Log**: Save data to an Excel file with columns:
  - Timestamp
  - City
  - Temperature (°C)
  - Humidity (%)
  - Weather Description
  - Wind Speed (m/s)

### Phase 2: Enhanced Functionality
- **Location Options**: Support for geographic coordinates as input.
- **Error Handling**: Graceful messages for invalid inputs or API failures.
- **Data Validation**: Prevent duplicate logging within a short time span.

### Phase 3: Advanced Features (Optional)
- **Automation**: Schedule periodic logging of weather data.
- **Data Analysis**: Generate trends and summaries from the logged data.
- **Visualization**: Graphs showing temperature and humidity trends over time.
- **User Interface**: Build a simple GUI for input and output.

---

## Folder Structure
