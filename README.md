# HNG 11 Stage 1 Task - Backend

### Description

This is a simple api that returns a welcome message to the visitor.

### Technologies

-   Python
-   Flask
-   Gunicorn
-   Nginx
-   Azure

### Installation

-   Clone the repository
-   Setup the app with `sudo ./setup.sh`
-   Start the app with `sudo ./start.sh`

### Usage

-   Visit the app at `http://api2.0xtech-wiz.tech/api/`

### Endpoints

-   `/api/help` - Returns a welcome message
    ```json
    {
    	"client_ip": "127.0.0.1", // The IP address of the requester
    	"location": "New York", // The city of the requester
    	"greeting": "Hello, Mark!, the temperature is 11 degrees Celcius in New York"
    }
    ```

### Author

-   [Ukeme Edet](https://github.com/Ukeme-Edet)

### License

-   MIT
