# Flight Data Analytics

## Overview

The **Flight Data Analytics** application provides insights into flight status data through real-time analytics and visualizations. This project demonstrates how to fetch flight data from an API, process and store it in a cloud database, and create interactive visualizations using Dash.

## Features

- **Data Ingestion:** Fetch real-time flight data from AviationStack API.
- **Data Processing:** Clean and prepare data for analysis.
- **Database Storage:** Store processed data in AWS RDS (MySQL/PostgreSQL).
- **Data Visualization:** Interactive charts and graphs using Dash.
- **Cloud Deployment:** Deploy the application using AWS EC2 or Elastic Beanstalk.

## Technologies Used

- **Backend:**
  - Python
  - Flask
- **Data Processing:**
  - Pandas
- **Database:**
  - MySQL
  - AWS RDS
- **Visualization:**
  - Dash
  - Plotly
- **Cloud Deployment:**
  - AWS EC2
  - AWS Elastic Beanstalk

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- AWS account with RDS setup

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/christymugs/flightanalytics.git
   cd flightanalytics

2. Create Virtual Enviornment
  python -m venv venv
  source venv/bin/activate  # For Windows: venv\Scripts\activate

3. Install Dependencies
    pip install -r requirements.txt
4. Fetch and Process Data
     Fetch Data from API:
      python fetch_data.py
     Process Data:
      python process_data.py
   Store Data to Database:
      python store_data.py
5. Run Locally
     python app.py

