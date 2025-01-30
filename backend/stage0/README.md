# Simple FastAPI Project

This is a simple FastAPI project that demonstrates how to use the FastAPI framework to create a RESTful API. The project includes endpoints for basic CRUD operations and is structured to be easily extensible for more complex use cases.

## Features

- FastAPI-based RESTful API
- Asynchronous request handling
- Basic CRUD operations
- Easy to extend and customize
- Built with best practices in mind

## Installation

To install the project, follow these steps:

1. Clone the repository:
   
   ```bash
   git clone https://github.com/judeo-s/HNG-Internship.git
   cd HNG-Internship/backend/stage0
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI server:

```bash
uvicorn main:app --reload
```

The server will start on `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.