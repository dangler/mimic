# mimic
Python app for mimicking rest servicess

# Motivation
mimic is a python app for quickly standing up a temporary rest service to be used for testing consumers.

# Dependencies
- python3
- json-schema
- flask

# Usage
python3 mimic contracts.json

contracts.json must validate using the following json-schema in contracts-schema.json

# Todo
- create build for dist
- document how to use
- document required json format
- setup version, features list, etc.
- add support for params and varying api schemas
- clean up README

# Example contracts.json file
```json
[
  {
    "description": "User List",
    "request": {
      "method": "GET",
      "path": "/user/list"
    },
    "response": {
      "body": {
        "users": [
          {
            "user_id": 1,
            "name": "Chris Rivers",
            "mention_name": "chris",
            "email": "chris@hipchat.com",
            "title": "Developer",
            "photo_url": "https:\/\/www.hipchat.com\/chris.png",
            "last_active": 1360031425,
            "created": 1315711352,
            "status": "away",
            "status_message": "gym, bbl",
            "is_group_admin": 1,
            "is_deleted": 0
          },
          {
            "user_id": 3,
            "name": "Peter Curley",
            "mention_name": "pete",
            "email": "pete@hipchat.com",
            "title": "Designer",
            "photo_url": "https:\/\/www.hipchat.com\/pete.png",
            "last_active": 1360031425,
            "created": 1315711352,
            "status": "offline",
            "status_message": "",
            "is_group_admin": 1,
            "is_deleted": 0
          },
          {
            "user_id": 5,
            "name": "Garret Heaton",
            "mention_name": "garret",
            "email": "garret@hipchat.com",
            "title": "Co-founder",
            "photo_url": "https:\/\/www.hipchat.com\/garret.png",
            "last_active": 1360031425,
            "created": 1315711352,
            "status": "available",
            "status_message": "Come see what I'm working on!",
            "is_group_admin": 1,
            "is_deleted": 0
          }
        ]
      },
      "headers": {
        "Content-Type": "application/json"
      },
      "status": 200
    }
  },
  {
    "description": "Show User (user found)",
    "request": {
      "method": "GET",
      "path": "/user/show/5"
    },
    "response": {
      "body": {
        "user": {
          "user_id": 5,
          "name": "Garret Heaton",
          "mention_name": "garret",
          "last_active": 1360031425,
          "created": 1315711352,
          "email": "garret@hipchat.com",
          "title": "Co-founder",
          "photo_url": "https:\/\/www.hipchat.com\/img\/silhouette_125.png",
          "status": "available",
          "status_message": "Come see what I'm working on!",
          "is_group_admin": 1,
          "is_deleted": 0
        }
      }
    },
    "headers": {
      "Content-Type": "application/json"
    },
    "status": 200
  },
  {
    "description": "Show User (unauthorized to view user)",
    "request": {
      "method": "GET",
      "path": "/user/show/6"
    },
    "response": {
      "body": {
  
      },
      "headers": {
        "Content-Type": "application/json"
      },
      "status": 403
    }
  }
]
```
