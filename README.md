# SVCE Student Cloud Dashboard (Assignment I)

This repository contains the implementation of a cloud application using Flask and Python, fulfilling the Cloud Computing and Security (BIS613D) assignment requirement:
*"Implement cloud applications using GAE, AWS, Azure/simulate cloud applications using Cloudsim/ Greencloud/ Cloud Analyst etc.."*

## Features
- **Student Dashboard:** Beautiful, dark-themed UI with glassmorphism to show student details.
- **Server Information:** Real-time extraction of Hostname, Platform, Timestamp, and User-Agent.
- **Cloud Resources Tracker:** Visual trackers for various simulated cloud services.
- **Dynamic Assignments:** Add your projects and assignments dynamically to the dashboard.
- **Cloud Guestbook:** Interactive form submission built into the UI.

## How to Run Locally

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python main.py
   ```
3. Open `http://127.0.0.1:8080` in your browser.

## Deployment to Google App Engine (GAE)
1. Install Google Cloud SDK.
2. Initialize and login: `gcloud init`
3. Deploy the application:
   ```bash
   gcloud app deploy app.yaml
   ```

## Deployment to Render (Free Cloud Hosting)
Render is an excellent alternative for deploying Python web apps quickly.
1. Create a free account at [Render](https://render.com/).
2. Click **New +** and select **Web Service**.
3. Connect your GitHub account and select this repository.
4. Configure the Web Service:
   - **Environment:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn main:app`
5. Click **Create Web Service**. Render will automatically build and deploy your application!