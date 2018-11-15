import pymysql


conn=pymysql.connect(user="root",password="root@1234",host="127.0.0.1",database="metrix")
cur=conn.cursor()

while True:
    SName=input("Enter first name: ")
    Scity=input("Enter city: ")
    SFather_Name=input("Enter Father Name: ")
    sSalary=float(input("Enter Salary: "))
    sql='''INSERT INTO student(name,city,father_name,salary)values(%s,%s,%s,%f)'''%(SName,Scity,SFather_Name,sSalary)    
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    choice=input("Enter your choice(Y/N): ")
    if choice == 'N':
        break


conn.close()
