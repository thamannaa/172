
class Doctor():
    def __init__(self):
        print("class doctor")
        
    def BMI(weight,height):
        bmi=weight/(height*height)
        print("your bmi is "+str(bmi))
        
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("your heart rate is normal")
        else:
            print("your heart rate does not seem normal please visit the clinic")
            
            
class Patient(Doctor):
    def __init__(self,name,weight,height,heart_rates):
        self.patient_name=name
        self.patient_weight=weight
        self.patient_height=height
        self.patient_heart_rates=heart_rates
        
    def health_check(self):
        print("patient name:"+self.patient_name)
        Doctor.BMI(self.patient_weight,self.patient_height)
        Doctor.heart_rate(self.patient_heart_rates)
        
obj_patient1=Patient("Michael",30,0.9144,80)
obj_patient2=Patient("Jessica",40,1,120)
obj_patient1.health_check()
obj_patient2.health_check()
        
        


