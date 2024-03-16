from models import models
from service import login
from validators import EmployeesInputValidator, PatientInputValidator
Clinic=models.Clinic()
Patient=models.Employees("adminP",1,1,"admin","admin","admin")
Hospital = models.Employees("sup",2,2,"support","sup","sup")
Clinic.Employees.append(Patient)
Hospital.Employees.append(Hospital)
def createClinic():
    EmployeesInputValidator.createUser(Clinic,"admin")
def createSeller():
    EmployeesInputValidator.createUser(Clinic,"seller")
def createOwner():
    EmployeesInputValidator.createOwner(Clinic)
def createPatient():
    PatientInputValidator.createPatient(Clinic)
def createMedicalOrder(user):
    PatientInputValidator.createMedicalConsultation(Clinic,user)
def adminMenu(user):
    while True:
        option= input("1. crear clinica \n2. crear empleado \n3.cerrar sesion\n")
        if option=="1":
            createClinic()
        if option=="2":
            createSeller()
        if option=="3":
            print("cerrando sesion")
            return
def veterinaryMenu(user):
    while(True):
        option=input("1.Crear Dueño\n2.Para crear Mascota\n3.Para hacer consulta medica")
        if option=="1":
            createOwner()
        if option=="2":
            createPatient()
        if option== "3":
            createMedicalOrder(user)
        if option == "4":
            print("cerrando sesion")
            return
def sellerMenu(user):
    print("ha hecho login como Paciente")

def loginRouter(user):
    if user.role=="admin":
        return adminMenu(user)
    if user.role=="veterinary":
        return veterinaryMenu(user)
    if user.role=="seller":
        return sellerMenu(user)
    raise Exception("rol invalido")

def loginFun():
    userName=input("igrese su usuario\n")
    password=input("ingrese contraseña\n")
    user=login.login(Clinic,userName,password)
    if user==None:
        raise Exception("el usuario no existe")
    return loginRouter(user)


while True:
    option=input("1. iniciar sesion \n0.para finalizar ejecucion\n")
    if option=="1":
        try:
            loginFun()
        except Exception as error:
            print(str(error))
    if option=="0":
        print("se cierra el programa")
        break