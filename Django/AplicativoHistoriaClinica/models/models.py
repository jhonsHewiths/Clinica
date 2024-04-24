
class Employees():
    def __init__(self,name,id,birthdate,role,userName,password,email,adress):
        self.name=name
        self.id=id
        self.email=email
        self.adress=adress
        self.birthdate=birthdate
        self.role=role
        self.userName=userName
        self.password=password

class Patient():
    def __init__(self,id,name,birthdate,gender,adress,numberPhone,email):
        self.id=id
        self.name=name
        self.birthdate=birthdate
        self.gender=gender
        self.adress=adress
        self.numberPhone=numberPhone
        self.email=email
        
class ClinicHistory():
    def __init__(self, date,doctorId, reasonConsultation, symptoms,  diagnosis, procedure, procedureDetail, medicine, medicineDose):
        self.date=date
        self.doctorId=doctorId
        self.reasonConsultation=reasonConsultation
        self.symptoms=symptoms
        self.diagnosis=diagnosis
        self.procedure=procedure
        self.procedureDetail=procedureDetail
        self.medicine=medicine
        self.medicineDose=medicineDose

class MedicalOrder():
    def __init__(self, OrderNumber, IdPatient, IdDoctor, CreationDate):
        self.OrderNumber=OrderNumber
        self.IdPatient=IdPatient
        self.IdDoctor=IdDoctor
        self.CreationDate=CreationDate

class Clinic():
    def __init__(self):
        self.Employees=[]
        self.Patient=[]
        self.ClinicHistory={}
        self.MedicalOrder=[]
        self.nurse={}


