import json

#sample DB

EMPLOYEES_DB = {
    "E12345": {
        "name": "Alice Johnson",
        "role": "Software Engineer",
        "department": "Engineering",
        "leave_balance": 12
    },
    "E67890": {
        "name": "Bob Smith",
        "role": "Data Scientist",
        "department": "AI Research",
        "leave_balance": 20
    },
    "E11223": {
        "name": "Charlie Davis",
        "role": "HR Manager",
        "department": "Human Resources",
        "leave_balance": 5
    },
    "E33445": {
        "name": "Diana Prince",
        "role": "Product Manager",
        "department": "Product",
        "leave_balance": 8
    },
    "E55667": {
        "name": "Evan Wright",
        "role": "DevOps Engineer",
        "department": "Operations",
        "leave_balance": 15
    },
    "E77889": {
        "name": "Fiona Green",
        "role": "Marketing Specialist",
        "department": "Marketing",
        "leave_balance": 3
    }
}

INTERVIEW_QUESTIONS_DB = {
    "Software Engineer": [
        "Explain the difference between a process and a thread.",
        "What is the time complexity of QuickSort in the worst case?",
        "Describe the principles of RESTful APIs.",
        "How do you prevent SQL injection?",
        "What is a race condition?"
    ],
    "Data Scientist": [
        "What is the difference between supervised and unsupervised learning?",
        "How do you handle missing data in a dataset?",
        "Explain the concept of overfitting and how to prevent it.",
        "What is the curse of dimensionality?",
        "Explain the ROC curve."
    ],
    "Product Manager": [
        "How do you prioritize features for a new product?",
        "Describe a time you had to say no to a stakeholder.",
        "How do you measure the success of a product launch?",
        "How do you handle feature creep?",
        "Explain the difference between Agile and Waterfall."
    ],
    "DevOps Engineer": [
        "What is CI/CD and why is it important?",
        "Explain the difference between Docker and a Virtual Machine.",
        "How do you handle a production outage?",
        "What is Infrastructure as Code (IaC)?",
        "Explain the concept of load balancing."
    ],
    "Marketing Specialist": [
        "How do you measure ROI for a marketing campaign?",
        "What is your experience with SEO?",
        "How do you handle a social media crisis?",
        "Explain the difference between inbound and outbound marketing.",
        "How do you identify a target audience?"
    ],
    "UI/UX Designer": [
        "What is the difference between UI and UX?",
        "Describe your design process.",
        "How do you handle feedback from developers?",
        "What tools do you use for prototyping?",
        "Explain the importance of accessibility in design."
    ]
}

#functions 

def get_employee_details(employee_id: str) -> dict:
    """
    Retrieves details of an employee (name, department, role).
    
    Args:
        employee_id (str): The ID of the employee (e.g., 'E12345').
        
    Returns:
        dict: Employee details or an error message if not found.
    """
    employee = EMPLOYEES_DB.get(employee_id)
    if employee:
        return {
            "employee_id": employee_id,
            "name": employee["name"],
            "role": employee["role"],
            "department": employee["department"]
        }
    return {"error": "Employee not found."}

def check_leave_balance(employee_id: str) -> dict:
    """
    Returns the remaining leave balance for an employee.
    
    Args:
        employee_id (str): The ID of the employee (e.g., 'E12345').
        
    Returns:
        dict: Leave balance or an error message if not found.
    """
    employee = EMPLOYEES_DB.get(employee_id)
    if employee:
        return {
            "employee_id": employee_id,
            "name": employee["name"],
            "leave_balance": employee["leave_balance"]
        }
    return {"error": "Employee not found."}

def generate_interview_questions(job_role: str) -> list:
    """
    Generates interview questions for a given job role.
    
    Args:
        job_role (str): The role to generate questions for (e.g., 'Data Scientist').
        
    Returns:
        list: A list of interview questions or a default message if the role is unknown.
    """
    
    questions = INTERVIEW_QUESTIONS_DB.get(job_role)
    
    if not questions:
        #questions for unknown roles 
        return [
            f"Tell me about your experience as a {job_role}.",
            "What are your greatest strengths?",
            "Where do you see yourself in 5 years?",
            "Describe a challenging situation you faced at work and how you handled it.",
            "How do you handle conflict with a coworker?"
        ]
        
    return questions