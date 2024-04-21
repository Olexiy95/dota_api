from datetime import datetime


def convert_timestamp(timestamp):
    try:
        # Check if the input is a Unix timestamp (integer)
        if isinstance(timestamp, int):
            # Convert Unix timestamp to datetime object
            dt_object = datetime.fromtimestamp(timestamp)
            # Convert datetime object to string
            dt_string = dt_object.strftime("%Y-%m-%d %H:%M:%S")
            return dt_string
        # Check if the input is a datetime string
        elif isinstance(timestamp, str):
            # Convert datetime string to datetime object
            dt_object = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            # Convert datetime object to Unix timestamp
            unix_timestamp = int(dt_object.timestamp())
            return unix_timestamp
        else:
            return "Invalid input"
    except Exception as e:
        return str(e)
