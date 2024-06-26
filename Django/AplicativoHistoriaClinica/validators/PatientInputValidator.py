import validators.inputTypeValidators as inputTypeValidators
import service.adminService as adminService
import datetime

def createUser(Clinic,role):
    name=input("Ingrese el nombre del usuario \n")
    inputTypeValidators.stringValidator(name,"nombre del usuario \n")
    id=inputTypeValidators.integerValidator(input("Ingrese el documento del usuario \n"),"cedula del usuario \n")
    email=input("Ingrese el correo del usuario \n")
    inputTypeValidators.stringValidator(email,"correo del usuario \n")
    userName=input("Ingrese el usuario \n")
    inputTypeValidators.stringValidator(userName, "Nombre del usuario \n")
    password=input("Ingrese la contraseña del usuario \n")
    inputTypeValidators.stringValidator(password, "contraseña \n")
    birthdate=input("Ingrese la fecha de nacimiento del usuario \n")
    inputTypeValidators.stringValidator(birthdate,"fecha de nacimiento \n")
    adress=input("Ingrese la direccion del usuario \n")
    inputTypeValidators.stringValidator(adress,"direccion del usuario \n")
    print("Se completaron las validaciones")
    adminService.createUser(Clinic,name,id,email,role,userName,password,adress,birthdate)

def createPatient(Clinic):
    id=inputTypeValidators.integerValidator(input("Ingrese el documento del Paciente \n"),"cedula del Paciente \n")
    name=input("Ingrese el nombre del Paciente \n")
    inputTypeValidators.stringValidator(name,"nombre del Paciente \n")
    birthdate=input("Ingrese la fecha de nacimiento del Paciente \n")
    inputTypeValidators.stringValidator(birthdate,"fecha de nacimiento del Paciente \n")
    gender=input("Ingrese el genero del Paciente \n")
    inputTypeValidators.stringValidator(gender,"genero del Paciente \n")
    adress=input("Ingrese la direccion del Paciente \n")
    inputTypeValidators.stringValidator(adress,"direccion del Paciente \n")
    numberPhone=inputTypeValidators.integerValidator(input("Ingrese el numero de contacto del Paciente \n"),"movil del Paciente \n")
    email=input("Ingrese el correo del Paciente \n")
    inputTypeValidators.stringValidator(email,"correo del Paciente \n")
    print("Se completaron las validaciones")
    adminService.createPatient(Clinic,id,name,birthdate,gender,adress,numberPhone,email)

def createClinicHistory(Clinic,user):
    date=datetime.datetime.today()
    print(date)
    id=inputTypeValidators.integerValidator(input("Ingrese el documento del usuario \n"),"cedula del usuario \n")
    reasonConsultation=input("Ingrese el motivo de la consulta \n")
    inputTypeValidators.stringValidator(reasonConsultation,"Consulta realizada \n")
    symptoms=input("Ingrese el diagnostico registrado \n")
    inputTypeValidators.stringValidator(symptoms,"sinmatologia \n")
    diagnosis=input("Ingrese el dianostico del usuario \n")
    inputTypeValidators.stringValidator(diagnosis,"Diagnostico realizado \n")
    adminService.createClinicHistory(Clinic,user,id,reasonConsultation,symptoms,diagnosis)
    
def createNurseVisit(Clinic, user):
    id=inputTypeValidators.integerValidator(input("Ingrese el documento del usuario \n"),"cedula del usuario \n")
    bloodPressure=input("Ingrese la apresion \n")
    inputTypeValidators.stringValidator(bloodPressure,"presion realizada \n")
    temperature=input("Ingrese temperatura \n")
    inputTypeValidators.stringValidator(temperature,"temperatura registrada \n")
    pulse=input("Ingrese el pulso del usuario \n")
    inputTypeValidators.stringValidator(pulse,"Pulso realizado \n")
    oxygenLevel=input("Ingrese oxigeno del usuario \n")
    inputTypeValidators.stringValidator(oxygenLevel,"Oxigeno agregados \n")
    procedure=input("Ingrese el procedimiento realizado \n")
    inputTypeValidators.stringValidator(procedure,"Procedimiento agregado \n")
    procedureDetail=input("Ingrese el detalle del procedimiento al  usuario \n")
    inputTypeValidators.stringValidator(procedureDetail,"Detalle guardado \n")
    medicine=input("Ingrese la medicina suministrada al usuario \n")
    inputTypeValidators.stringValidator(medicine,"Medicina registrada \n")
    medicineDose=input("Ingrese el detalle de la dosis de la medicina del usuario \n")
    inputTypeValidators.stringValidator(medicineDose,"Diagnostico de medicina realizado \n")
    tests=input("Ingrese las pruebas realizadas \n")
    inputTypeValidators.stringValidator(tests,"prueba registrada\n")
    observation=input("Observacion del usuario \n")
    inputTypeValidators.stringValidator(observation,"observacion realizado \n")
    date=input("dato del usuario \n")
    inputTypeValidators.stringValidator(date,"dato realizado \n")
    adminService.createNurseVisit(Clinic, user, id, bloodPressure,temperature,pulse,oxygenLevel,medicine,procedure, procedureDetail, tests, observation,date)