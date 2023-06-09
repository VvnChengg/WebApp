# NTUIM112 - WebApp Final Project: 好市好事

## Introduction
Welcome to the README file for the final project of NTUIM112 - WebApp. Our project, "好市好事," is designed to create a web application that promotes reusing through the development of a second-hand market website. Within this README, you will discover comprehensive instructions on setting up and running the project, as well as the features we have implemented.

## Prerequisites
Before starting the project, make sure you have the following:

- Python installed on your system
- Redis server installed
- A virtual environment (optional but recommended)

## Setup

To set up the project, follow these steps:

Clone the repository to your local machine.

1. Clone the repository to your local machine.
```git clone https://github.com/VvnChengg/WebApp.git```

2. Navigate to the project directory.
```cd 好市好事```

3. (Optional) Create and activate a virtual environment. It is recommended to use virtual environments to isolate project dependencies.
```
python -m venv env
source env/bin/activate  # For Unix/Linux
env\Scripts\activate  # For Windows
```

4. Install the required packages. This project uses a requirements.txt file to manage dependencies. Run the following command to install them.
```pip install -r requirements.txt```

5. Start the Redis server. Open a new terminal window and run the following command:
```redis-server```

6. Run the development server. Open another terminal window and run the following command:
```python manage.py runserver```

If you are on macOS, you can also try running ```python3 manage.py runserver``` if the above command does not work.

7. Access the web application. Once the server is running, open your web browser and go to `http://localhost:8000` to access the "好市好事" web application.

## Usage
The "好市好事" web application allows users to browse and discover local businesses and events. Users can search for specific businesses or events, view details, and interact with the platform. The application also provides features for businesses and event organizers to create listings and promote their offerings.

## Contributing
If you would like to contribute to this project, please follow these steps:

Fork the repository on GitHub.
Create a new branch with a descriptive name for your feature or bug fix.
Make the necessary changes and commit them.
Push your changes to your forked repository.
Submit a pull request to the main repository, explaining the changes you have made.


> Please note that the above instructions assume a Unix/Linux-based system. If you are using a Windows system, make sure to use the appropriate commands or tools as needed.
