# Chat Application Demo

## How To Run:

1. Make sure you have Python 3.x installed on your computer.
2. Clone this repository to your local machine.
3. Open a terminal/command prompt window and navigate to the project directory.
4. Install the required dependencies by running the following command in your terminal:
```
pip install flask
pip install flask-socketio
```

5. Run the Flask development server by executing the following command in your terminal:
```
flask --app main run
```

6. Open a web browser and go to http://127.0.0.1:5500/templates/index.html to view the chat app.
7. Enter a username and message in the input fields provided and click on the "Send" button to send the message. The message will be publicly displayed on the webpage.

## Roadmap:

1. Direct messaging: Two users can chat with each other
2. Typing indicator: When typing, the recipient gets notified
3. User status: Whether you are online or offline

## Things To Consider

1. Type of messages: Text only? Probably some images too in the future
2. Limits: Size of a single message
3. Security: What type of encryption to use