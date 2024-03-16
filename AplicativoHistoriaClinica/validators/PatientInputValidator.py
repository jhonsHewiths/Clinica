import validators.inputTypeValidators as inputTypeValidators
import service.adminService as adminService
import datetime

def createPatient(Clinic):
    name=input("ingrese el nombre del paciente \n")
    inputTypeValidators.stringValidator(name,"nombre del paciente ")
    ownerId=inputTypeValidators.integerValidator(input("ingrese la cedula del dueño\n"),"cedula del dueño")
    age=inputTypeValidators.integerValidator(input("ingrese la edad del paciente\n"),"edad del paciente")
    id= len(Clinic.Patient)
    adminService.createPatient(Clinic,id,name,ownerId,age)

def createMedicalOrder(Clinic,user):
    date=datetime.datetime.now()
    print(date)
    PatientId=inputTypeValidators.integerValidator(input("el id del paciente\n"),"edad del paciente")
    reasonConsultation=input("ingrese el motivo de consulta del paciente \n")
    inputTypeValidators.stringValidator(reasonConsultation,"motivo de consulta del paciente ")
    symptoms=input("ingrese sintomatologia del paciente \n")
    inputTypeValidators.stringValidator(symptoms,"motivo de consulta de la mascota ")
    diagnosis =input("ingrese el diagnostico del paciente \n")
    inputTypeValidators.stringValidator(diagnosis,"motivo de consulta del paciente ") 
    procedure=input("ingrese el procedimiento del paciente \n")
    if procedure == "":
        procedure="N/A"
    inputTypeValidators.stringValidator(procedure,"motivo de consulta del paciente ")    
    procedureDetail=input("ingrese el detalle de procedimiento del paciente \n")
    if procedureDetail=="":
        procedureDetail="N/A"
    inputTypeValidators.stringValidator(procedureDetail,"motivo de consulta del paciente ")
    medicine=input("ingrese el medicamentos del paciente \n")
    if medicine=="":
        medicine="N/A"
    inputTypeValidators.stringValidator(medicine,"motivo de consulta del paciente ")
    medicineDose=input("ingrese la dosis del paciente \n")
    if medicine=="":
        medicineDose="N/A"
    inputTypeValidators.stringValidator(medicineDose,"motivo de consulta del paciente ")
    adminService.createMedicalOrder(Clinic,user,PatientId,reasonConsultation,symptoms,diagnosis,procedure,procedureDetail,medicine,medicineDose,date)
    
