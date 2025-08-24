# Patient Management System API (Request_Body)
---
#### 🏥 Project Overview
The Patient Management System API is a FastAPI-based RESTful service designed to efficiently manage patient records with automatic BMI calculation and health categorization. This system provides healthcare providers with tools to store, retrieve, update, and analyze patient data with proper validation and error handling.
---
#### Features
Core Functionality
- **Patient CRUD Operations**: Create, read, update, and delete patient records
- **Automatic BMI Calculation**: Computes BMI from height and weight measurements
- **Health Assessment**: Provides automatic health verdicts based on BMI categories
- **Data Sorting**: Sort patients by height, weight, or BMI in ascending/descending order
- **Data Validation**: Comprehensive input validation using Pydantic models
- **Error Handling**: Proper HTTP status codes and descriptive error messages
---
#### Technical Features
- **RESTful API Design**: Clean and intuitive endpoint structure
- **JSON File Storage**: Simple file-based data persistence
- **Type Safety**: Extensive type annotations throughout the codebase
- **Computed Fields**: Automatic calculation of derived properties (BMI and verdict)
--- 
#### API Endpoints
<img width="1589" height="1049" alt="image" src="https://github.com/user-attachments/assets/823d9912-bd08-402d-8cf3-a10a5df95840" />
---
####  BMI Categories
The system automatically categorizes patients based on WHO BMI standards:
<img width="259" height="146" alt="image" src="https://github.com/user-attachments/assets/858b1a5b-927f-4ff8-9e4f-c3776cecb1ae" />
---
#### Installation & Setup:
Prerequisites
- Python 3.8+
- FastAPI
- Uvicorn (ASGI server)

