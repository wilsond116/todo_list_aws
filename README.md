# To-Do List API

This is a simple To-Do List API built using AWS services, including DynamoDB, AWS Lambda, and API Gateway. The API allows users to manage their to-do tasks with functionalities to create, read, and delete tasks.

## Features

- **Create a Task**: Add a new task to the to-do list.
- **Read Tasks**: Retrieve all tasks from the to-do list.
- **Delete a Task**: Remove a task from the to-do list.

## Technologies Used

- **AWS Lambda**: Serverless compute service to run the API code.
- **AWS API Gateway**: To create, publish, maintain, and secure the API.
- **Amazon DynamoDB**: NoSQL database to store the tasks.

## API Endpoints

### 1. Create a Task

- **Method**: POST
- **Endpoint**: `/todo`
- **Request Body**:
  ```json
  {
    "task": "Your task description",
    "completed": false
  }
{
  "id": "unique-task-id",
  "task": "Your task description",
  "completed": false
}

Feel free to customize it with your information, such as your name and any additional details about the project!
