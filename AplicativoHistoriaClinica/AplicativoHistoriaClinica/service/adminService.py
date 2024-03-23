import AplicativoHistoriaClinica.service.createUser as createUser
import models.models as models

def createPatient(Clinic,id,name,birthdate,gender,adress,numberPhone,email,contactEmergencyName,patientRelation,emergencyNumberPhone,insurenceCompanyName,policyNumber,validatyPolicy):
    user=createUser.findUserById(Clinic,id)
    if user: 
         raise Exception("Ya existe un usuario con este documento")
    user = None
    if user: 
         raise Exception("Ya existe un usuario con este nombre ingresado")
    Patient=models.Patient(id,name,birthdate,gender,adress,numberPhone,email,contactEmergencyName,patientRelation,emergencyNumberPhone,insurenceCompanyName,policyNumber,validatyPolicy)
    Clinic.Patient.append(Patient)
    Clinic.ClinicHistory[str(id)]={}
def createClinicHistory(Clinic, user, date,doctorId, reasonConsultation, symptoms,diagnosis,procedure,procedureDetail,medicine,medicineDose):
    Patient=findPatientById(Clinic,id)
    if Patient==None:
        raise Exception("no existe un paciente con el id enviado")
    newClinicHistory={}
    newClinicHistory["date"]=date
    newClinicHistory["doctorId"]=user.id
    newClinicHistory["reasonConsultation"]=reasonConsultation
    newClinicHistory["symptoms"]=symptoms
    newClinicHistory["diagnosis"]=diagnosis
    if procedure!="N/A":
        newClinicHistory["procedure"]=procedure
        newClinicHistory["procedureDetail"]=procedureDetail
    if medicine!="N/A":
        MedicalOrder=models.MedicalOrder(len(Clinic.MedicalOrder), Patient,Patient.name,user.id,medicine,date)
        Clinic.MedicalOrder.append(MedicalOrder)
        newClinicHistory["order"]=MedicalOrder.id
        newClinicHistory["medicine"]=medicine
        newClinicHistory["medicineDose"]=medicineDose
    print("historia nueva")
    print(newClinicHistory)
    Clinic.clinicHistory[str(Patient)][str(date)]=newClinicHistory
    print("historia paciente")
    print(Clinic.clinicHistory[str(Patient)])
    print("historia clinica")
    print(Clinic.clinicHistory)


def findPatientById(Clinic,PatientId):
    for Patient in Clinic.Patient:
        if PatientId == Patient.id:
            return Patient
    return None