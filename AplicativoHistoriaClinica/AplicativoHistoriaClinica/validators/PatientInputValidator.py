import validator.inputTypeValidators as inputTypeValidators
import service.adminService as adminService
import service.administrationService as administrationService
import datetime

def createUser(hospital,role):
    name=input("Ingrese el nombre del usuario \n")
    inputTypeValidators.strinValidator(name,"nombre del usuario \n")
    identification=inputTypeValidators.integerValidator(input("Ingrese el documento del usuario \n"),"cedula del usuario \n")
    mail=input("Ingrese el correo del usuario \n")
    inputTypeValidators.strinValidator(mail,"correo del usuario \n")
    telephone=inputTypeValidators.integerValidator(input("Ingrese el numero de contacto del usuario \n"),"movil del usuario \n")
    userName=input("Ingrese el usuario \n")
    inputTypeValidators.strinValidator(userName, "Nombre del usuario \n")
    password=input("Ingrese la contraseña del usuario \n")
    inputTypeValidators.strinValidator(password, "contraseña \n")
    birthdate=input("Ingrese la fecha de nacimiento del usuario \n")
    inputTypeValidators.strinValidator(birthdate,"fecha de nacimiento \n")
    street=input("Ingrese la direccion del usuario \n")
    inputTypeValidators.strinValidator(street,"direccion del usuario \n")
    print("Se pasaron las validaciones")
    adminService.createUser(hospital,name,identification,mail,telephone,role,userName,password,street,birthdate)

def createPatient(hospital):
    identification=inputTypeValidators.integerValidator(input("Ingrese el documento del Paciente \n"),"cedula del Paciente \n")
    name=input("Ingrese el nombre del Paciente \n")
    inputTypeValidators.strinValidator(name,"nombre del Paciente \n")
    birthdate=input("Ingrese la fecha de nacimiento del Paciente \n")
    inputTypeValidators.strinValidator(birthdate,"fecha de nacimiento del Paciente \n")
    gender=input("Ingrese el genero del Paciente \n")
    inputTypeValidators.strinValidator(gender,"genero del Paciente \n")
    street=input("Ingrese la direccion del Paciente \n")
    inputTypeValidators.strinValidator(street,"direccion del Paciente \n")
    telephone=inputTypeValidators.integerValidator(input("Ingrese el numero de contacto del Paciente \n"),"movil del Paciente \n")
    mail=input("Ingrese el correo del Paciente \n")
    inputTypeValidators.strinValidator(mail,"correo del Paciente \n")
    print("Se pasaron las validaciones")
    adminService.createPatient(hospital,identification,name,birthdate,gender,street,telephone,mail)

def createMedicalConsultation(hospital,user):
    date= datetime.datetime.today()
    print(date)
    identification=inputTypeValidators.integerValidator(input("Ingrese el documento del usuario \n"),"cedula del usuario \n")
    motiveConsultation=input("Ingrese el motivo de la consulta \n")
    inputTypeValidators.strinValidator(motiveConsultation,"Consulta realizada \n")
    symptomatoly=input("Ingrese el diagnostico registrado \n")
    inputTypeValidators.strinValidator(symptomatoly,"sinmatologia \n")
    diagnosis=input("Ingrese el dianostico del usuario \n")
    inputTypeValidators.strinValidator(diagnosis,"Diagnostico realizado \n")

    administrationService.createMedicalConsultation(hospital,user,identification,motiveConsultation,symptomatoly,diagnosis)
    
