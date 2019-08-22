import serial
#Check available USB ports using ls /dev/tty* in the Terminal
ser = serial.Serial(
    port='COM9',\ 
    baudrate=9600,    bytesize=serial.EIGHTBITS,        timeout=0)

print("connected to: " + ser.portstr)
while True:
    k = str(ser.readline())[2:-5]
    k = k.split(',')
    T1 = k[0]
    T2 = k[1]
    f = 0
    if(T1>5):
        f = 1
    notify(T2,f)
    upload(T1,T2,f)
    
def notify(u,f):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("Email1", "Password1") 
    msg['From'] = "Email1"
    msg['To'] = "Email2"
    if(f):
        t = 'AC Temperature' + u
    else:
        t = 'AC Frozen'
    msg['Subject'] = t
    s.sendmail("Email1","Email2",msg.as_string())
    
def upload(T1,T2,f):
    
    import pyrebase
    
    firebaseConfig = {
    apiKey: "AIzaSyAes_2s17si0I7I7sPH3pAGVhhzc8I7Uvg",
    authDomain: "microproject-e091e.firebaseapp.com",
    databaseURL: "https://microproject-e091e.firebaseio.com",
    projectId: "microproject-e091e",
    storageBucket: "microproject-e091e.appspot.com",
    messagingSenderId: "272254815642",
    appId: "1:272254815642:web:c585021d85413169"
    }
    
    firebase=pyrebase.initialize_app(firebaseConfig)
    #creating database
    db=firebase.database()
    
    #defining data
    data={"Pipe Temperature":str(T1), "Room Temperature":str(T2) }
    db.child("AC").child("Room Environment Temperature").update({"Room Temperature":str(T2)})
    db.child("AC").child("Pipe Temperature").update({"Pipe Temperature":str(T1)})
 
