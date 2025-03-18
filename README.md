# URL Shortener Service

This is a simple URL shortening service built with Flask and SQLite. It allows users to:

- Shorten a long URL.
- Retrieve the original URL from a shortened one.


Time spent on this assignment: 3 hours ⏱️

## 🚀 Setup & Run the Service

###  Prerequisites

Ensure you have Python 3 installed.

### Setup Environment

```sh
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```sh
python routes.py
```

The service will run on `http://localhost:5000/`.

---

##  API Endpoints

### Shorten URL

**Endpoint:** `POST /shorten`

```sh
# Curl
curl -X POST "http://localhost:5000/shorten" \
     -H "Content-Type: application/json" \
     -d '{"url": "www.example.com"}' 

# Postman
POST http://localhost:5000/shorten
Content-Type: application/json

{
  "url": "www.example.com"
}
```
**Response:** 
```
{
    "short_url": "http://localhost:5000/80fc0f"
}
```

### Get Original URL

**Endpoint:** `GET /<short_code>`


```sh
# Curl
curl 'http://localhost:5000/80fc0f'

# Postman
GET http://localhost:5000/80fc0f
```
**Response:** 
```sh
{ 
  "original_url": "www.example.com" 
}
```

---

## ✏️ Design Decisions

- **SQLite Database**: To keep things simple while ensuring URLs are saved permanently
  
- **Hashing function to shorten URL**: Allows for a simple and efficient way to shorten URLs

- **Flask Framework**: Lightweight web framework requiring minimal setup and configuration 

- **Duplicate entries**: If a URL is already shortened, the same short URL will be returned

- **DB Index**: Added an index to the `short_id` column to improve lookup performance
