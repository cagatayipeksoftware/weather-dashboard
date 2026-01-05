# Vibe Coding Weather Dashboard

## Project Description

A functional Desktop Weather Dashboard application built using Python and Tkinter. This project was developed to demonstrate "Vibe Coding" using the **Cursor** AI editor. It fetches real-time weather data using the Open-Meteo API (no API key required).

## Features

- Clean Graphical User Interface (GUI).
- Real-time temperature and wind speed data.
- City search functionality with error handling.
- No API Key required (uses Open-Meteo).

## Technologies Used

- **Language:** Python 3.0
- **Libraries:** `tkinter` (Standard), `requests`
- **Vibe Coding Tool:** Cursor (AI-First Code Editor)

## Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone <your-repo-url>
    cd weather-dashboard-vibe
    ```

2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    _(Note: Tkinter is usually included with Python. If not, you may need to install `python-tk`)_.

3.  **Run the Project:**
    ```bash
    python main.py
    ```
## 🐳 Running with Docker

You can containerize this application to run it consistently across different environments.

### Prerequisites
- [Docker](https://www.docker.com/get-started) installed on your machine.

### Build the Image
Open your terminal in the project root directory and run:

```bash
docker build -t weather-dashboard .
## Credits

Developed by Çağatay İpek for the Software Development Assignment (Week 10).
Generated with the assistance of Cursor AI.
