# SIEM Tool

A lightweight Security Information and Event Management (SIEM) tool designed to collect, analyze, and visualize security logs, aiding in threat detection and incident response.

---

## 🚀 Features

* **Log Collection**: Aggregates logs from various sources for centralized analysis.
* **Real-time Monitoring**: Continuously monitors logs to detect anomalies and potential threats.
* **Alerting System**: Generates alerts based on predefined rules and thresholds.
* **Dashboard Visualization**: Provides an intuitive dashboard for visual representation of security events.
* **Modular Architecture**: Easily extendable to integrate additional log sources and analysis modules.

---

## 🛠️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/DarenVong/Siem_tool.git
   cd Siem_tool
   ```



2. **Create a Virtual Environment** (Optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```



---

## 📈 Usage

1. **Configure the Tool**:

   Edit the configuration file located at `config/config.yaml` to specify log sources, alert thresholds, and other settings.

2. **Run the Application**:

   ```bash
   python main.py
   ```



3. **Access the Dashboard**:

   Open your web browser and navigate to `http://localhost:5000` to view the dashboard.

---

## 🧪 Testing

To run the test suite:

```bash
pytest tests/
```



---

## 📁 Project Structure

```bash
Siem_tool/
├── config/             # Configuration files
├── src/                # Source code
├── tests/              # Test cases
├── main.py             # Entry point of the application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

