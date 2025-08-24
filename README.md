# Patient Management System API (Request_Body)
---
#### 🏥 Project Overview
- The Patient Management System API is a FastAPI-based RESTful service designed to efficiently manage patient records with automatic BMI calculation and health categorization. This system provides healthcare providers with tools to store, retrieve, update, and analyze patient data with proper validation and error handling.
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
---
#### Step-by-Step Setup

##### 1) Create Project Directory

```
mkdir patient-management-api
cd patient-management-api
```
##### 2) Set Up Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
##### 3) Install Dependencies
```
pip install fastapi uvicorn
```
##### 4) Create Project Files
```
# Create main application file
touch main.py

# Create empty JSON data file
echo "{}" > patients.json
```
##### 5) Copy the Code
```
Paste the provided FastAPI code into main.py
```
##### 6) Run the Application

```
uvicorn main:app --reload
```
##### 7) Access the API

- **API will be available at**: http://localhost:8000
- **Interactive documentation**: http://localhost:8000/docs
- **Alternative documentation**: http://localhost:8000/redoc
---
#### Data Structure
##### Patient Model
```
{
  "id": "P001",  # Unique identifier
  "name": "Prajwal Ghotkar",  # Full name (2-100 characters)
  "city": "Austin",  # City of residence
  "age": 24,  # Age in years (0-120)
  "gender": "male",  # Gender (male/female/other)
  "height": 1.75,  # Height in meters (>0)
  "weight": 68.5,  # Weight in kilograms (>0)
  "bmi": 22.4,  # Computed automatically
  "verdict": "Normal weight"  # Computed automatically
}
```
---
#### API Usage Examples
##### 1) Create a New Patient
curl -X POST "http://localhost:8000/create" \
-H "Content-Type: application/json" \
-d '{
  "id": "P001",
  "name": "Prajwal Ghotkar",
  "city": "Austin",
  "age": 24,
  "gender": "male",
  "height": 1.75,
  "weight": 68.5
}'

---
##### 2) Retrieve All Patients
curl -X GET "http://localhost:8000/view"

--- 
##### 3) Get Specific Patient
curl -X GET "http://localhost:8000/patient/P001"

---
##### 4) Sort Patients by BMI (Descending)
curl -X GET "http://localhost:8000/sort?sort_by=bmi&order=desc"

---
##### 5) Update Patient Information
curl -X PUT "http://localhost:8000/update/P001" \
-H "Content-Type: application/json" \
-d '{
  "weight": 72.0,
  "city": "Dallas"
}'

---

##### 6) Delete a Patient
curl -X DELETE "http://localhost:8000/delete/P001"

---
#### Testing the API
##### Using the Interactive Documentation
- Navigate to http://localhost:8000/docs
- Explore all available endpoints
- Use the "Try it out" feature to test endpoints directly
- View request and response schemas

---
#### Error Handling
##### The API returns appropriate HTTP status codes:

- **200 OK**: Successful request
- **201 Created**: Resource successfully created
- **400 Bad Request**: Invalid input parameters
- **404 Not Found**: Requested resource doesn't exist
- **422 Unprocessable Entity**: Validation error

---
#### Future Enhancements
- **Database Integration**: Replace JSON file with proper database (SQLite, PostgreSQL)
- **Authentication**: Add user authentication and authorization
- **Advanced Filtering**: Add more filtering options beyond sorting
- **Medical History**: Expand to include medical history and appointments
- **Export Functionality**: Add data export features (CSV, PDF reports)
- **Frontend Interface**: Develop a web-based user interface
---
#### License
This project is open source and available under the MIT License.

#### 🤝 Contributing
- Fork the repository
- Create a feature branch
- Make your changes
- Add tests if applicable
- Submit a pull request
This Patient Management System API provides a solid foundation for healthcare applications with its comprehensive features and robust design.
this all description
