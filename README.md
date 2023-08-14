# Crowd Clique
## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Environment Variables](#environment-variables)
  - [Install Dependencies](#install-dependencies)
- [How to Run](#how-to-run)
- [Screenshots](#screenshots)

## Description

Crowd Clique is a web application that leverages the Ticketmaster API to facilitate the creation of social networks among live event-goers. The application offers a user-friendly interface for account creation, live event searching, event page joining, commenting and replying on event pages, and browsing other user accounts.

This project was built with Python (Flask) and SQLAlchemy, utilizing the Ticketmaster API to provide event-related information.

## Requirements

Ensure you have the following dependencies installed:

```
Flask==2.0.3
flask-behind-proxy==0.1.1
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
Pillow==8.4.0
gunicorn==20.1.0
SQLAlchemy>=1.4.0,<1.5.0
email_validator==1.3.1
requests>=2.16.0,<3.0.0
```

## Setup

To set up the Crowd Clique project locally, follow these steps:

### Environment Variables

1. Obtain access to the Ticketmaster API by registering for an API key at [Ticketmaster Developer Portal](https://developer.ticketmaster.com/).
2. Export the acquired API key as environment variable:

   ```bash
   export TICKETMASTER_API_KEY=your-api-key
   ```

### Install Dependencies

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/crowd-clique.git
   ```

2. Navigate to the project directory:

   ```bash
   cd crowd-clique
   ```

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Run the application using Flask's development server:

   ```bash
   flask run
   ```

2. Access the application in your web browser at `http://localhost:5000`.
