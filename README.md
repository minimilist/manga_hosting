# Manga Hosting Website API

This repository houses the backend code for a Manga Hosting Website API, developed with Flask, PostgreSQL, and Google Cloud services. The API provides essential functionalities for a manga hosting platform, including user registration, authentication, manga uploads, and search capabilities.

## Features

- **User Authentication**: Secure user registration and authentication using JWT tokens.
- **Manga Upload**: Users can upload manga content, with Cloud Vision API integration for explicit content detection.
- **Search Functionality**: Efficient manga search capabilities utilizing GPT-3 for parsing keywords and tags.
- **Database Integration**: SQLAlchemy facilitates the integration of Python objects and classes with a PostgreSQL database.
- **Additional Libraries**: Utilizes PyMuPDF for converting base64-encoded PDF files into PIL images for further processing.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- Google Cloud account with Cloud Vision API enabled

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/manga-hosting-api.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. Configure Google Cloud credentials:

   - Follow Google Cloud documentation to set up and download the JSON credentials file.
   - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the JSON file.

5. Run the application:

   ```bash
   python run.py
   ```

## Usage

- Refer to the API documentation for information on available endpoints and their usage.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to the Flask and SQLAlchemy communities for providing excellent frameworks.
- Special appreciation to the contributors of PyMuPDF, GPT-3, and Google Cloud Vision API for their valuable libraries and services.

Happy coding!
