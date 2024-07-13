from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str,"%d/%m/%Y")
    actual_datetime = datetime.now()
    
    time_diff = actual_datetime - birthdate
    
    minutes = time_diff.total_seconds() / 60
    
    print(f"You lived {minutes} minutes.")

birthdate_str = "25/09/2005" 
minutes_lived(birthdate_str)
