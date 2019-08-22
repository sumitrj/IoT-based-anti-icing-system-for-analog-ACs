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
