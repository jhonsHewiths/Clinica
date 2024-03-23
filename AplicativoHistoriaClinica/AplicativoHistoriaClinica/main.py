from models import models
from service import login
from validators import EmployeesInputValidator, PatientInputValidator
Clinic=models.Clinic()
Patient=models.Employees("adminP",1,1,"admin","admin","admin")
Hospital = models.Employees("sup",2,2,"support","sup","sup")
Clinic.Employees.append(Patient)
Hospital.Employees.append(Hospital)
def createDoctor():
    EmployeesInputValidator.createUser(Hospital,"Doctor")
def createNurses():
    EmployeesInputValidator.createUser(Hospital,"Enfermera")
def createPatient():
    EmployeesInputValidator.createPatient(Clinic)
def createMedicalOrder(user):
    PatientInputValidator.createMedicalOrder(Clinic,user)
def adminMenu(user):
    while True:
        option= input("1. Crear ingreso doctor \n2. Crear ingreso enfermera \n3 Crear orden medica \n4.cerrar sesion\n")
        if option=="1":
            createDoctor()
        if option=="2":
            createNurses()
        if option=="3":
            createMedicalOrder()
        if option=="4":
            print("Cerrando sesion \n")
        return
def personalMenu(user):
    while(True):
        option=input("1.Crear paciente \n2. Cerrar")
        if option=="1":
            createPatient()
        if option=="2":
            print("Cerrando sesión")
            return
def clinicMenu(user):
    while(True):
        option=input("1.Crear historia clinica \n2. Cerrar")
        if option=="1":
            createMedicalOrder()
        if option=="2":
            print("Cerrando sesión")
            return