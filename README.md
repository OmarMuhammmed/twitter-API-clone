# Backend Twitter Clone


## Table of Contents
- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Installation with Docker](#installation-with-docker)
- [Installation without Docker](#installation-without-docker)


## Description

This project is a backend implementation of a Twitter clone using Django, Django REST framework, Django Channels, PostgreSQL, Redis. This project includes a wide range of features, including authentication, tweet management, likes, retweets, notifications, real-time chat, and more


## Features

- **Authentication**: Signup, email activation, login, password reset request, password reset, password change, JWT token refresh, JWT token verification, and logout.
- **Social Auth**: Login with Google.
- **Tweets**: Create, read, update, and delete tweets.
- **Likes**: Manage likes on tweets.
- **Bookmark**: Manage bookmarked tweets.
- **Retweets**: Manage retweets.
- **Retweet Likes**: Manage likes on retweets.
- **User Management**: Get and update user information, manage following and followers.
- **Notifications**: Real-time notification system.
- **Real-Time Chat**: Real-time chat feature.


## Prerequisites

- Python
- Git
- Docker
- PostgreSQL
- Redis


## Getting Started

### Common Setup

1. Clone the repository:

```sh
git clone https://github.com/
```
```sh
cd clone-twitter-backend
```

2. Configure environment variables: Create a `.env` file based on the `.env.example` file and set your environment variables.

### Installation with Docker

Build and start the Docker containers:

```bash
docker-compose up --build
```

### Installation without Docker

1. Create and activate a virtual environment:

```bash
python -m venv venv
```
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```
5. Apply database migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

Your Twitter clone backend should now be up and running. 🎉
The application will be accessible at [http://localhost:8000](http://localhost:8000).


## License

This project is licensed under the [MIT License](LICENSE).
