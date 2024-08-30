# Flask Google Sheets API

This project provides a Flask-based API to receive JSON data via a POST request and update a Google Sheet with the data. It leverages the `gspread` library to interact with Google Sheets and uses OAuth2 for authentication.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Google Sheets Setup](#google-sheets-setup)
- [Environment Variables](#environment-variables)
- [Error Handling](#error-handling)
- [Mind Map](#mind-map)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/flask-google-sheets-api.git
   cd flask-google-sheets-api
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Google Sheets credentials JSON file to the project:**

   Place your `rugged-silo-430612-c6-8c079feacf17.json` file in the project root directory.

## Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

2. **Make a POST request to the `/update_sheet` endpoint with JSON data:**

   ```json
   {
       "UDF1": "John Doe",
       "UDF2": "123456789",
       "UDF3": "Mountain Bike",
       "UDF4": "CH123456",
       "UDF5": "MN123456",
       "UDF6": "Yes",
       "UDF7": "1000",
       "UDF8": "Bike Dealer"
   }
   ```

   The data will be appended to the Google Sheet.

## API Endpoint

### `POST /update_sheet`

- **Description:** Updates the Google Sheet with the provided JSON data.
- **Request Body:** JSON object with the following keys:
  - `UDF1`: Name
  - `UDF2`: Phone
  - `UDF3`: Bike Type
  - `UDF4`: Chassis Number
  - `UDF5`: Motor Number
  - `UDF6`: Payment Done (Yes/No)
  - `UDF7`: Price
  - `UDF8`: Dealer Name
- **Response:**
  - `200 OK`: Data appended successfully.
  - `400 Bad Request`: Invalid data format.
  - `500 Internal Server Error`: Error occurred while processing the request.

## Google Sheets Setup

1. **Create a new Google Sheet** or use an existing one.
2. **Share the sheet** with the service account email from your credentials file.

## Error Handling

The API provides meaningful error messages for common issues such as invalid JSON format, missing credentials, or Google Sheets errors.

## Contributing

Feel free to submit pull requests or open issues to improve the project.


