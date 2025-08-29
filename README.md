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
```
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
```
---
##### 2) Retrieve All Patients
```
curl -X GET "http://localhost:8000/view"
```
--- 
##### 3) Get Specific Patient
```
curl -X GET "http://localhost:8000/patient/P001"
```
---
##### 4) Sort Patients by BMI (Descending)
```
curl -X GET "http://localhost:8000/sort?sort_by=bmi&order=desc"
```
---
##### 5) Update Patient Information
```
curl -X PUT "http://localhost:8000/update/P001" \
-H "Content-Type: application/json" \
-d '{
  "weight": 72.0,
  "city": "Dallas"
}'
```
---

##### 6) Delete a Patient
```
curl -X DELETE "http://localhost:8000/delete/P001"
```
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
http://127.0.0.1:8000/docs#/default/create_patient_create_post
---

## screenshot
<img width="1920" height="992" alt="Screenshot 2025-08-24 231429" src="https://github.com/user-attachments/assets/8ef63f8c-bca8-47cb-b915-a0b119635e27" />
<img width="1920" height="976" alt="Screenshot 2025-08-24 231441" src="https://github.com/user-attachments/assets/fcbcbfed-f140-4026-af30-31f4935f7d1a" />
<img width="1892" height="952" alt="Screenshot 2025-08-25 004042" src="https://github.com/user-attachments/assets/b4e8ce5c-3383-4646-8e7c-e2e8a25ef86b" />
<img width="1893" height="953" alt="Screenshot 2025-08-25 004059" src="https://github.com/user-attachments/assets/d1f2711f-b0d8-4893-a434-2c91cb61697b" />
<img width="1881" height="928" alt="Screenshot 2025-08-24 233315" src="https://github.com/user-attachments/assets/74b03689-3f62-4217-b355-0b7ff280fe2c" />
<img width="1888" height="940" alt="Screenshot 2025-08-24 233616" src="https://github.com/user-attachments/assets/9113d914-5567-4991-a77a-c34a7b44b599" />
<img width="1890" height="953" alt="Screenshot 2025-08-24 233634" src="https://github.com/user-attachments/assets/4abab0b0-d4e0-46f6-9a65-2cd07f984cae" />
<img width="1370" height="748" alt="Screenshot 2025-08-25 005534" src="https://github.com/user-attachments/assets/81947614-df4a-473c-ae23-26fd1508b794" />

---

# Insurance premimum category predictor.
<img width="1920" height="984" alt="Screenshot 2025-08-28 115022" src="https://github.com/user-attachments/assets/b34521d4-4657-4de3-bc62-2b0a32e65160" />
<img width="1920" height="967" alt="Screenshot 2025-08-28 115006" src="https://github.com/user-attachments/assets/2e45b39f-4006-49de-8d58-80b687882510" />
<img width="1920" height="965" alt="Screenshot 2025-08-28 115217" src="https://github.com/user-attachments/assets/7e045fc7-10e6-45a9-8667-b7e4cb499d38" />
<img width="1920" height="940" alt="Screenshot 2025-08-28 115513" src="https://github.com/user-attachments/assets/67e17092-144e-4d73-a17a-1ca051da7ac3" />
<img width="1920" height="936" alt="Screenshot 2025-08-28 115520" src="https://github.com/user-attachments/assets/e833ff66-ad97-4c6e-9477-215f7d284c67" />

---
<img width="1920" height="982" alt="Screenshot 2025-08-28 123433" src="https://github.com/user-attachments/assets/81c0132f-b65c-4519-85c7-6de4d3205e98" />
<img width="1920" height="936" alt="Screenshot 2025-08-28 122029" src="https://github.com/user-attachments/assets/4159f144-bb40-4562-8a05-03c785f2071d" />








