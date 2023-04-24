import subprocess
import os

from Authentication import Authentication
class Account : 
    
    def __init__(self) -> None:
        pass

    def ajouterUtilis(self,username,password) -> bool:
        if username in os.listdir("/home"):
            return False
        try :
            cmd = f"sudo adduser {username} --gecos '' --disabled-password"
            subprocess.run(cmd.split(), check=True)
            cmd = f"echo '{username}:{password}' | sudo chpasswd"
            subprocess.run(cmd, shell=True, check=True)
        except :
            return False
        return True

    def supprimerUtilis(self,username,password) -> bool:
        test = Authentication(username,password)
        try :
            if test.authenti() == False :
                return False
            command = f"sudo deluser {username}"
            os.system(command)
        except :
            return False
        return True
    
    def changePassword(self,username,password,new_password)  -> bool:
        test = Authentication(username,password)
        if test.authenti() == False :
            return False
        try :
            command = f"echo '{username}:{new_password}' | sudo chpasswd"
            os.system(command)
        except : 
            return False
        return True
    
if __name__ == "__main__":
    a =  Account()
    # a.changePassword("cccc","querty")
    # print(a.ajouterUtilis("sss","azerty"))
    #print(a.supprimerUtilis("as","sdsdsd"))

 