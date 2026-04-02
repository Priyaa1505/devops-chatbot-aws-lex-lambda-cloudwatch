# DevOps Automation Chatbot with Monitoring

## Overview
This project is a serverless DevOps chatbot built using AWS Lex and AWS Lambda.  
It simulates real-world DevOps operations such as checking server status, triggering deployments, and restarting services.

The project also integrates AWS CloudWatch for logging and monitoring, enabling better debugging and observability.

---

## Tech Stack
- AWS Lex (Chatbot / NLP)
- AWS Lambda (Serverless backend)
- AWS CloudWatch (Logging & Monitoring)
- Python

---

## Features
- ✅ Check server status  
- 🚀 Trigger deployment  
- 🔄 Restart service  
- 📊 Logging using CloudWatch  
- 🤖 Natural language understanding  

---

## Architecture
User → AWS Lex → AWS Lambda → CloudWatch Logs → Response  

### 🔹 Architecture Diagram
img9.png

---

## Screenshots

### 🔹 Chatbot Testing
This screenshot shows the chatbot successfully understanding user commands and responding accordingly.
img4.png

---

### 🔹 AWS Lambda Function
This screenshot shows the backend logic that processes user intents and generates responses.
img3.png

---

### 🔹 CloudWatch Logs
This screenshot shows logs capturing user input, detected intent, and response for monitoring and debugging.
img5.png
img6.png
img7.png
img8.png
---

## 📊 Monitoring with CloudWatch
AWS CloudWatch is used to:
- Capture logs of user inputs and responses  
- Monitor Lambda execution  
- Debug errors and system behavior  

---

## 🧪 Testing

### Example 1:
**Input:**  
check server status  

**Output:**  
Server is running smoothly ✅  

---

### Example 2:
**Input:**  
deploy app  

**Output:**  
Deployment started 🚀  

---

### Example 3:
**Input:**  
restart service  

**Output:**  
Service restarting 🔄  

---

## ▶️ How to Run

1. Create a bot in AWS Lex  
2. Add intents and utterances  
3. Create a Lambda function using Python  
4. Connect Lambda with Lex (intent + alias)  
5. Enable logging using CloudWatch  
6. Build and test the bot  

---

## 🔮 Future Improvements
- Integrate with real CI/CD pipeline (Jenkins)  
- Add API Gateway for external access  
- Connect with real server monitoring  
- Enhance chatbot with more DevOps commands  

---

## 👩‍💻 Author
Priya Prajapati 
