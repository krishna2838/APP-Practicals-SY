def document_boundary(func):
    def wrapper_function(*args, **kwargs):
        sep = "=" * 60
        print(sep)
        print("DYNAMIC REPORT GENERATOR".center(60))
        print(sep)
        
        func(*args, **kwargs)
        
        print(sep)
        print("END OF REPORT".center(60))
        print(sep)
    return wrapper_function

def inject_creator(func):
    def wrapper_function(instance, *args, **kwargs):
        print(f"\n[Prepared by: {instance.creator_name}]") 
        return func(instance, *args, **kwargs)
    return wrapper_function

class AssignmentDocument:
    
    organization_entity = "ABC Technologies Pvt. Ltd."  

    def __init__(self, heading, creator_name):
        self.heading = heading
        self.creator_name = creator_name
        self.body_lines = []

    def insert_line(self, text_data):
        self.body_lines.append(text_data)

    @classmethod
    def update_organization(cls, new_org_name):
        cls.organization_entity = new_org_name

    @staticmethod
    def print_divider():
        print("-" * 60)

    def __str__(self):
        return f"Report Title : {self.heading}\nAuthor : {self.creator_name}"

    def __len__(self):
        return len(self.body_lines)

    @document_boundary
    @inject_creator
    def output_document(self):
        print("Company :", AssignmentDocument.organization_entity)
        print(self)

        AssignmentDocument.print_divider()
        print("Report Contents:")

        # Replaced enumerate with a manual counter for structural variance
        counter = 1
        for line in self.body_lines:
            print(f"{counter}. {line}")
            counter += 1

        AssignmentDocument.print_divider()
        print("Total Sections :", len(self))


# --- Execution Block ---

practical_doc = AssignmentDocument("Advanced Python Practical Report", "Krishna Ghodke")
practical_doc.insert_line("Completed Experiment No. 2 successfully.")
practical_doc.insert_line("Implemented Decorators, Class Methods, Static Methods and Magic Methods.")
practical_doc.insert_line("Learned Object-Oriented Programming concepts.")
practical_doc.insert_line("Report prepared by Krishna Ghodke.")
practical_doc.output_document()

print("\nChanging Company Name...\n")
AssignmentDocument.update_organization("MIT ADT University")

performance_doc = AssignmentDocument("Employee Performance Report", "Krishna Ghodke")
performance_doc.insert_line("Attendance : 98%")
performance_doc.insert_line("Projects Completed : 8")
performance_doc.insert_line("Rating : Excellent")
performance_doc.insert_line("Department : Computer Engineering")
performance_doc.insert_line("Recommendation : Promotion Approved")
performance_doc.output_document()

result_doc = AssignmentDocument("Student Result Report", "Krishna Ghodke")
result_doc.insert_line("Student Name : Rahul")
result_doc.insert_line("Roll No : 101")
result_doc.insert_line("CGPA : 9.25")
result_doc.insert_line("Status : Pass with Distinction")
result_doc.insert_line("Result : Pass")
result_doc.output_document()