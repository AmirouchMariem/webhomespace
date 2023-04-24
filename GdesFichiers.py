import os
import subprocess
import zipfile

class GdesFichiers :

    def __init__(self) -> None:
        self.serchFIle = []
    
    def getPath(self,path):
        l = []
        try:
            for j in os.listdir(path) :
                if j[0] != '.':
                    l.append({
                        'chemin':path+"/"+j,
                        'nom' : j
                    })
        except:
            return []
        return l

    def getUserDerictory(self, path : str) :
        l : list[str] = []
        try: 
            for i in os.listdir(path) : 
                if os.path.isdir(path+"/"+i) :
                    l.append(i)
        except :
            return []
        return l

    def getUserFiles(self, path : str) :
        l : list[str] = []
        try :
            for i in os.listdir(path) : 
                if os.path.isfile(path+"/"+i) :
                    l.append(i)
        except :
            return []
        return l
        
    def getnbrFichier(self, path : str) -> int :
        cmp : int = 0
        try:
            for i in os.listdir(path) : 
                if os.path.isfile(path+"/"+i) and i[0] != '.':
                    cmp += 1
        except :
            return 0
        return cmp

    def getnbrDirectory(self, path : str) -> int : 
        cmp : int = 0
        try :
            for i in os.listdir(path) : 
                if os.path.isdir(path+"/"+i) :
                    cmp += 1
        except:
            return 0
        return cmp
    
    def gettaille(self, path : str) -> None :
        cmd = ['du', '-s', path]
        try:
            return subprocess.run(cmd, capture_output=True, text=True).stdout.split()[0]
        except:
            return 0
        
    def rechercheFilesNameFileExtention(self,path:str,filename : str )  : 
        l = []
        try:
            for i in os.listdir(path) :
                if i[0] != '.':
                    if(i.count(filename)): 
                        l.append({
                            'chemin':path+"/"+i,
                            'nom' : i
                        })
        except:
            return []
        return l 
    
    def telechercherHomeDerectory(self,username) -> None :
        home_dir = os.path.expanduser('/home/'+username)
        zip_filename = "/home/"+username+"/"+username+".zip"
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(home_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, home_dir))


if __name__ == "__main__" :
    a= GdesFichiers()
    a.getPath("/home/t")
    #print(str(a.getnbrFichier("/home")))
    #print(a.gettaille("/home/t"))
    #a.telechercherHomeDerectory()
    #a.rechercheFiles(".html")