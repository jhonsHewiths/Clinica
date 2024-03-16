import validators.inputTypeValidators as inputTypeValidators
import service.editUser as editUser
def createUser(Clinic,role):
    name=input("ingrese el nombre del usuario \n")
    inputTypeValidators.stringValidator(name,"nombre del usuario")
    id=inputTypeValidators.integerValidator(input("ingrese la cedula del usuario\n"),"cedula del usuario")
    age=inputTypeValidators.integerValidator(input("ingrese la edad del usuario\n"),"cedula del usuario")
    userName=input("ingrese el usuario\n")
    inputTypeValidators.stringValidator(userName,"nombre del usuario")
    password=input("ingrese la contraseña del usuario \n")
    inputTypeValidators.stringValidator(password,"nombre del usuario")
    print("se pasaron validaciones")
    editUser.createUser(Clinic,name,id,age,role,userName,password)

def createPatient(Clinic,role="administrativePersonality"):
    name=input("ingrese el nombre del usuario \n")
    inputTypeValidators.stringValidator(name,"nombre del usuario")
    id=inputTypeValidators.integerValidator(input("ingrese la cedula del usuario\n"),"cedula del usuario")
    age=inputTypeValidators.integerValidator(input("ingrese la edad del usuario\n"),"cedula del usuario")
    print("se pasaron validaciones")
    editUser.createUser(Clinic,name,id,age,role,None,None)
    