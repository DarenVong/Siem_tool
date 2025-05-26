import re

class LogParser:
    def __init__(self, log_format="csv"):
        self.log_format = log_format

    # parses a single line log line based on the provided format
    def parse_log_line(self, log_format, line):
        regex_pattern = re.sub(r'<([^>]+)>', r'(?P<\1>.+?)', log_format)
        match = re.match(regex_pattern, line)
        if match:
            return match.groupdict()
        else:
            return None

    # reads the log file and returns a list of lines
    def read_log_file(self, log_file_path):
        try:
            with open(log_file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: File {log_file_path} not found")
            return None
        
    # parses a log file and returns a list of dictionaries.
    def parse_log(self, log_file_path, log_format="csv"):
        if log_format is "csv":
            log_format = self.log_format
        if log_format is None:
            raise ValueError("Log format must be specified either during initialization or when calling parse_log")
            
        log_lines = self.read_log_file(log_file_path)
        if log_lines is None:
            return []
            
        parsed_logs = []
        for line in log_lines:
            parsed_line = self.parse_log_line(log_format, line.strip())
            if parsed_line:
                parsed_logs.append(parsed_line)
        return parsed_logs

# test the log parser
if __name__ == "__main__":
    # Example usage with different log formats
    log_file_path = "http_status.csv"
    
    # Create example log file
    with open(log_file_path, 'w') as f:
        f.write("2025-05-25 12:00:00 INFO This is a test message\n")
        f.write("2025-05-25 12:00:01 ERROR This is an error message\n")
        f.write("2025-05-25 12:00:02 WARNING This is a warning message\n")
    
    # Example 1: Initialize parser with format
    parser1 = LogParser(log_format="<timestamp> <level> <message>")
    parsed_logs = parser1.parse_log(log_file_path)
    print("Example 1 - Parser initialized with format:")
    for log in parsed_logs:
        print(log)
    
    # Example 2: Specify format during parsing
    parser2 = LogParser()
    parsed_logs = parser2.parse_log(log_file_path, log_format="<timestamp> <level> <message>")
    print("\nExample 2 - Format specified during parsing:")
    for log in parsed_logs:
        print(log)
