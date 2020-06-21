class Patient:
    patient_id=0
    def __init__(self,name,age,disease):
        self.name=name
        self.age=age
        self.disease=disease
        Patient.patient_id+=1

    def display_disease(self):
        print('The disease is {} and {}'.format(self.disease,self.patient_id))

patient1=Patient('sonu',30,'cough')
patient2=Patient('Deepu',30,'cold')

patient1.display_disease()
patient2.display_disease()
print(patient2.patient_id)