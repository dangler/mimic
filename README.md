# mimic
Python app for mimicking rest servicess

# Motivation
mimic is a python app for quickly standing up a temporary rest service to be used for testing consumers.

# Dependencies
json-schema
flask

# Usage
python3 mimic clients.json
    clients.json must validate using the following json-schema
   
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "minItems": 1,
    "uniqueItems": true,
    "properties": {
      "description": {
        "type": "string"
      },
      "request": {
        "type": "object",
        "properties": {
          "method": { "type": "string" },
          "path": { "type": "string" }
        },
        "required": ["method", "path"]
      },
      "response": {
        "type": "object",
        "properties": {
          "body": { "type": "object" },
          "headers": {
            "type": "object",
            "properties": {
              "Content-Type": { "type": "string"}
            },
            "required": ["Content-Type"]
          },
          "status": { "type": "integer" }
        },
        "required": ["body", "headers", "status"]
      }
    },
    "required": ["description", "request", "response"]
  }
}
```

# Todo
- create build for dist
- document how to use
- document required json format
- setup version, features list, etc.

# Example contract.json file
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
      "path": "/user/show?id=5"
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
      "path": "/user/show?id=6"
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
