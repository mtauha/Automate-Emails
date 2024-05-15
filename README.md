# Python Email Client

This is a Python application that demonstrates how to send emails using the SMTP protocol. It includes a `EmailClient` class that encapsulates the functionality for connecting to an SMTP server, logging in, sending emails, and closing the connection.

## Features

- Connect to an SMTP server securely using STARTTLS.
- Login to the SMTP server with email credentials.
- Send emails with customizable subject, body, and recipient(s).
- Gracefully handle errors during connection, login, and email sending.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/mtauha/automate-emails.git
   ```
2. Navigate to the project directory:

   ```bash
   cd Automate-Emails
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:

   Create a `.env` file in the project root directory and add your email credentials and SMTP server information:

   ```dotenv
   EMAIL=your_email@example.com
   PASSWD=your_password
   SMTP_SERVER=smtp.example.com
   SMTP_PORT=587
   ```

## Usage

1. Create an instance of the `EmailClient` class in your Python script:

   ```python
   from EmailClient import EmailClient

   instance = EmailClient()
   ```
2. Connect to the SMTP server:

   ```python
   instance.connect()
   ```
3. Login to the SMTP server:

   ```python
   instance.login()
   ```
4. Send an email:

   ```python
   subject = "Testing Script"
   body = "This is a test email."
   to_email = "recipient@example.com"

   instance.send(subject, body, to_email)
   ```
5. Close the connection when done:

   ```python
   instance.close()
   ```


## Usage with Docker

To run the Python Email Client application using Docker, follow these steps:

1. Build the Docker image from the project directory:

   ```bash
   docker build -t Automate-Emails .
   ```
2. Run a Docker container from the created image:

   ```bash
   docker run -it --rm --env-file .env Automate-Emails
   ```

   Replace `.env` with the path to your environment file containing email credentials and SMTP server information.

This will start the Python Email Client application inside a Docker container, and you should see the output in the terminal indicating the status of the email sending process.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
