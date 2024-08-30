from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Function to get the worksheet
def get_worksheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key('').sheet1
    return sheet

# API endpoint to receive data and update the sheet
@app.route('/update_sheet', methods=['POST'])
def update_sheet():
    data = request.json
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid data format. Expected a dictionary."}), 400

    try:
        worksheet = get_worksheet()
        
        # Check if the header row exists
        header_row = ['Name', 'Phone', 'BikeType', 'ChassisNumber', 'MotorNumber', 'PaymentDone', 'Price', 'DealerName']
        if worksheet.row_count == 0 or worksheet.row_values(1) != header_row:
            worksheet.insert_row(header_row, 1)
            
            header_format = {
                "backgroundColor": {
                    "red": 0.8,
                    "green": 0.8,
                    "blue": 0.8
                },
                "textFormat": {
                    "bold": True
                }
            }
            worksheet.format('A1:H1', header_format)

        # Prepare new row data
        row_data = [
        data.get("UDF1", ""),
        data.get("UDF2", ""),
        data.get("UDF3", ""),
        data.get("UDF4", ""),
        data.get("UDF5", ""),
        data.get("UDF6", ""),
        data.get("UDF7", ""),
        data.get("UDF8", "")
    ]
        
        # Append the new row
        worksheet.append_row(row_data)
        
        # Auto-resize columns
        worksheet.columns_auto_resize(0, 8)
        
        return jsonify({"message": "Data appended successfully."}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)