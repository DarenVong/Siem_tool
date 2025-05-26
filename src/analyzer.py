class Analyzer:
    def __init__(self):
        self.rules = {
            "failed_login": {
                "pattern": "failed login",
                "severity": "medium",
                "description": "Detected failed login attempt"
            },
            
        }

    def analyze_log(self, log_entry):
        pass
    # My understing of this code is that im making a function that will analyze the log entry and return a list of alerts
