import models.models as models

def createUser(Clinic,name,id,birthdate,role,userName,password,email,adress):
    user= findUserByid(Clinic,id)
    if user:
        raise Exception("ya existe un usuario con esa cedula")
    user = None
    if userName:
        user= findUserByUserName(Clinic,userName)
    if user:
        raise Exception("ya existe un usuario con ese nombre de usuario")
    employees=models.Employees(Clinic,name,id,email,role,userName,password,adress)
    Clinic.Employees.append(employees)

def findUserByUserName(Clinic,userName):
    for employees in Clinic.Employees:
        if userName == employees.userName:
            return employees
    return None

def findUserByid(Clinic,id):
    for employees in Clinic.Employees:
        if id == employees.id:
            return employees
    return None

def createPatient(Clinic,id,name,birthdate,gender,adress,numberPhone,email):
    user=createUser.findUserByid(Clinic,id)
    if user: 
         raise Exception("Ya existe un usuario con este documento")
    user = None
    if user: 
         raise Exception("Ya existe un usuario con este nombre ingresado")
    patient=models.Patient(id,name,birthdate,gender,adress,numberPhone,email)
    Clinic.Patient.append(patient)
    Clinic.ClinicHistory[str(id)]={}

def createClinicHistory(Clinic, user, date, reasonConsultation, symptoms,  diagnosis, procedure, procedureDetail, medicine, medicineDose):
    patient=findPatientById(Clinic,id)
    if patient is None:
        raise Exception("no existe un paciente con el id enviado")
    newClinicHistory={}
    newClinicHistory["date"]=date
    newClinicHistory["doctor"]=user.id
    newClinicHistory["reasonConsultation"]=reasonConsultation
    newClinicHistory["symptoms"]=symptoms
    newClinicHistory["diagnosis"]=diagnosis
    if procedure!="N/A":
        newClinicHistory["procedure"]=procedure
        newClinicHistory["procedureDetail"]=procedureDetail
    if medicine!="N/A":
        medicalOrder=models.MedicalOrder(len(Clinic.MedicalOrder), patient.id,user.id,medicine,date)
        Clinic.MedicalOrder.append(medicalOrder)
        newClinicHistory["order"]=medicalOrder.id
        newClinicHistory["medicine"]=medicine
        newClinicHistory["medicineDose"]=medicineDose
    print("historia nueva")
    print(newClinicHistory)
    if str(id) not in Clinic.ClinicHistory:
        Clinic.ClinicHistory[str(id)]={}

    Clinic.ClinicHistory[str(id)][str(date)]=newClinicHistory
    print("historia paciente")
    print(Clinic.ClinicHistory[str(id)])
    print("historia clinica")
    print(Clinic.ClinicHistory)


def findPatientById(Clinic,id):
    for patient in Clinic.Patient:
        if id == patient.id:
            return patient
    return None

def createNurseVisit(Clinic, user, id, bloodPressure,temperature,pulse,oxygenLevel,medicine,procedure, procedureDetail, tests,observation,date):
    patient = findPatientbyId(Clinic, id)
    if patient is None:
        raise Exception("No existe un paciente con ese id")
    nurseVisit = {
        "date": date,
        "patientId": patient.id,
        "bloodPressure": bloodPressure,
        "temperature": temperature,
        "pulse": pulse,
        "oxygenLevel": oxygenLevel,
        "medicine": medicine,
        "procedure": procedure,
        "procedureDetail": procedureDetail,
        "tests": tests,
        "observation": observation
    }
    if str(patient.id) not in Clinic.ClinicHistory:
        Clinic.ClinicHistory[str(patient.id)] = {}
    if str(date) not in Clinic.ClinicHistory[str(patient.id)]:
        Clinic.ClinicHistory[str(patient.id)][str(date)] = {}
    Clinic.ClinicHistory[str(patient.id)][str(date)]["nurseVisit"] = nurseVisit
    print("El registro de la visita de la enfermera se ha realizado con éxito")  

def findPatientbyId(Clinic, id):
    for patient in Clinic.Patient:
        if id == patient.id:
            return patient
    return None  