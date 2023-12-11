import json

student_data = {
    'name': 'John Doe',            
    'age': 18,                      
    'grade': 12,                    
    'subjects': ['Math', 'English', 'Science'],  
    'address': {
        'street': '123 Main St',    
        'city': 'Cityville',         
        'state': 'Stateville',       
        'zipcode': '12345'           
    }
}
f = open("student.json","w")
f.write(json.dumps(student_data, indent=1))