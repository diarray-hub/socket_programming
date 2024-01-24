# socket_programming
This repository contains code for a multi-connection server that performs 15 mathematical and arithmetic functions based on clients' demands. The implementation utilizes socket and thread programming to handle multiple client connections concurrently.
## Features

- **Multi-Connection Support:** The server is designed to handle multiple client connections simultaneously, allowing users to make mathematical requests concurrently.

- **Mathematical Operations:** The server provides functionality for 15 mathematical and arithmetic operations, catering to a variety of computation needs.

- **Socket Programming:** The communication between the server and clients is achieved using sockets, enabling data exchange over a network.

- **Thread Programming:** Threads are employed to manage concurrent connections, ensuring efficient and responsive handling of client requests.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/diarray-hub/socket_programming
   cd socket_programming

2. **Run the Server:**
   ```bash
   python3 calculus_server.py

3. **Run the clients:**
   ```bash
   python3 calculus_clientX.py

You can try to run the two clients simultaneously. Note that all these codes were written and tested with python version (3.10.12)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
