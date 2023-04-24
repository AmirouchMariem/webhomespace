import crypt
import os
import spwd

class Authentication :
    def __init__(self,username : str, password : str) -> None:
        self.username = username
        self.password = password

    def FindNameUtilis(self) -> bool:
        try:
            if self.username in os.listdir("/home"):
                return True
        except :
            return False
        return False
    
    def ComparePassWord(self) -> bool:
        try:
            user_info = spwd.getspnam(self.username)
            hashed_password, salt = user_info.sp_pwd, user_info.sp_pwdp
            generated_hash = crypt.crypt(self.password, salt)
            if generated_hash == hashed_password:
                return True 
        except :
            return False
        return False

    def authenti(self) -> bool:
        try :
            if self.ComparePassWord() == True and self.FindNameUser() == True :
                return True
        except : 
            return False
        return False

if __name__ == "__main__":
    p = Authentication("dev","1234")
    print(p.authenti())