import models.models as models

def createUser(Clinic, name,id,birthdate,role,userName,password,email,adress):
    user= findUserByid(Clinic,id)
    if user:
        raise Exception("ya existe un usuario con esa cedula")
    user = None
    if userName:
        user= findUserByUserName(Clinic,userName)
    if user:
        raise Exception("ya existe un usuario con ese nombre de usuario")
    Employees=models.Employees(name,id, birthdate, role,userName,password, email, adress)
    Clinic.append(Employees)

def findUserByUserName(Clinic,userName):
    for Employees in Clinic.Employees:
        if userName == Employees.userName:
            return Employees
    return None

def findUserByid(Clinic,id):
    for Employees in Clinic.Employees:
        if id == Employees.id:
            return Employees
    return None