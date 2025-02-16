# 📍 ZIP Code Lookup - FastAPI API  

This project provides a **complete ZIP code lookup, management, and export service**, built using **Python, FastAPI, and MongoDB**.  

## 🎯 Objective  

Develop a system that:  
✅ **ZIP Code Lookup**: Fetches ZIP codes using the ViaCEP API.  
✅ **Storage**: Saves query results in a **MongoDB** database.  
✅ **Export Data**: Supports exporting data in **JSON** or **CSV** format.  
✅ **CRUD Operations**: Implements **Create, Read, Update, and Delete** for managing stored data.  

## ⚙️ Features  

### 🔎 ZIP Code Lookup  
- Search for ZIP codes by **state and specific code**.  
- Uses the **ViaCEP API** to fetch details.  
- Includes **validation and error handling**.  

### 🗄️ Storage in MongoDB  
- Saves query results in **MongoDB**.  
- **Prevents duplication** by checking existing records before saving.  

### 📤 Data Export  
Supports exporting stored data in:  
- **JSON**: Structured for API integrations.  
- **CSV**: Ideal for spreadsheets and data analysis.  

### 🔧 CRUD Operations  
- **Create**: Manually add a new ZIP code record.  
- **Read**: Retrieve all stored ZIP codes.  
- **Update**: Modify an existing ZIP code entry.  
- **Delete**: Remove unwanted records.  

## 🛠️ Technologies Used  
🚀 **Python** - Main programming language.  
⚡ **FastAPI** - API framework.  
💾 **MongoDB** - NoSQL database for storage.  
🌍 **ViaCEP API** - External service for ZIP code queries.  
🛠 **Postman** - API testing and validation tool.  

## 📚 Additional Libraries  
- **pymongo** - MongoDB connection.  
- **csv, json** - Data manipulation and export.  
- **requests** - External API consumption.  

## 🔧 Installation  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/your-username/zip-code-lookup.git
cd zip-code-lookup
