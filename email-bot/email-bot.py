import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('anuragsinghj@gmail.com',"6543")
subject = "textpython"
body = "I love python bhai"
massage = "subject : {}\n\n{}".format(subject,body)
listadd = ['anuragsinghj789@gmail.com','anurag232@gmail.com','prgjaatgaruav@gmail.com']
ob.sendmail('anuragsinghj678@gmail.com',listadd,massage)
print("send mail")
ob.quit()