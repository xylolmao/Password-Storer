from cryptography.fernet import Fernet
import pathlib, os, sys, random

args = ["viewdec", "viewenc", "deldata", "add"]
try:
    arg = sys.argv[1]
    arg = arg.lower()
except:
    print("No Command Given -> Available CMDS: ")
    for a in args:
        print(a)
    os._exit(0)
        
key = Fernet.generate_key()
f = Fernet(key)

pardir = str(pathlib.Path(__file__).parent.resolve())
pdir = "Data"
adir = os.path.join(pardir, pdir)
try:
    os.mkdir(adir)
except:
    pass
    
def randompass() -> str:
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890:;./><'@]}[{=+-_)(*&^%$£!"
    ranpass = ''.join(random.sample(chars, 27))
    return ranpass
    
def viewenc() -> None:
    if os.path.exists(adir + "\\encinfo.txt"):
        with open(adir + "\\encinfo.txt", "r") as encdata:
            for line in encdata:
                for i in range(0, 3):
                    if i == 0:
                        print(f"App/website -> {str(line.strip()).split(', ')[i]}")
                    elif i == 1:
                        print(f"Name -> {str(line.strip()).split(', ')[i]}")
                    elif i == 2:
                        print(f"Email -> {str(line.strip()).split(', ')[i]}")
                    elif i == 3:
                        print(f"Password -> {str(line.strip()).split(', ')[i]}")
    else:
        raise FileNotFoundError(f"Decrypted File Doesn't Exist -> Try Using [python {__file__}.py add] First!")
    
def viewdec() -> None:
    if os.path.exists(adir + "\\decinfo.txt"):
        with open(adir + "\\decinfo.txt", "r") as decdata:
            for line in decdata:
                for i in range(0, 3):
                    if i == 0:
                        print(f"App/website -> {str(line.strip()).split(', ')[i]}")
                    elif i == 1:
                        print(f"Name -> {str(line.strip()).split(', ')[i]}")
                    elif i == 2:
                        print(f"Email -> {str(line.strip()).split(', ')[i]}")
                    elif i == 3:
                        print(f"Password -> {str(line.strip()).split(', ')[i]}")
    else:
        raise FileNotFoundError(f"Decrypted File Doesn't Exist -> Try Using [python {__file__}.py add] First!")
    
def add():
    app = input("Application/Website This Info Is For -> ")
    app += ", "
    name = bytes(input("Name(Optional) -> "), encoding="utf-8")
    email = bytes(input("Email(Optional) -> "), encoding="utf-8")
    password = bytes(input("Password -> "), encoding="utf-8")
    
    if len(password) <= 0:
        print("Password Expected -> Returning")
        return
    elif len(password) <= 4:
        print(f"Weak Password -> I Recommend: {randompass()}")

    with open(adir + "\\encinfo.txt", "a")as y:
        y.write(app + str(f.encrypt(name)).replace("b'", "").replace("'", "") + ", " + str(f.encrypt(email)).replace("b'", "").replace("'", "") + ", " + str(f.encrypt(password)).replace("b'", "").replace("'", "") + "\n")
        filename = y.name
        print(f"Saved Encrypted Data In {filename}")
            
    with open(adir + "\\decinfo.txt", "a")as y:
        y.write(app + str(name).replace("b'", "").replace("'", "") + ", " + str(email).replace("b'", "").replace("'", "") + ", " + str(password).replace("b'", "").replace("'", "") + "\n")
        filename = y.name
        print(f"Saved Decrypted Data In {filename}")
    
try:
    if arg == "viewdec":
        viewdec()
    elif arg == "add":  
        add()
    elif arg == "viewenc":
        viewenc()
    elif arg == "deldata":
        [os.remove(f"Data\\{fs}") for fs in next(os.walk(adir), (None, None, []))[2]]
        os.removedirs(adir)
        print("Successfully Removed All Data Collected By This Tool!")
    else:
        print("Invalid Command Given -> Available CMDS: ")
        for a in args:
            print(a)
        os._exit(0)
except:
    pass

        
