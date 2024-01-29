import random,sys




domain="@gmail.com"

la=["khan","talukdar","rahaman","ahmed","hossain","islam","hasan","sarkar","sheikh"]
nmb=["123","1234","12345","official","71","99","404","143","420","rabbi","niloy","alom","nahid","ff","gaming","gamer","tohin","akash","rifat","sifat","joy","sagor","ovi","omar","samir","raj","rajib","jakir","ojit","faruk","mia","ridoy","mumit","labib","tutul","habib","abir","jihad","fahim","asad","nafi","nafis","siam","sir","limon","monir","himal","rudro","muhib","sadh","miya","sakil","jisan","milon","surjo","orko","jibon","arab","opu","onik","anik","emon","sami","saimon","antor","asif","abdul","rana","nurul","ismail","naim","ratul","sagor","hamim","roton","rony","safin","sajid","said","suhag","kasem","rasid","omit","drubo","yasin","abid","razu","sohid","wafi","khaled","mursed","suhel","torikul"]
rc=random.choice
rn=random.randint
def mail(user,f1):
    while True:
        e1=f"{f1}{rc(la)}{domain}"
        e2=f"{f1}{rc(nmb)}{domain}"
        e3=f"{f1}{str(rn(1000,9999))}{domain}"
        e4=f"{f1}{rc(la)}{str(rn(1,99))}{domain}"
        e5=f"{f1}{rc(nmb)}{str(rn(1,99))}{domain}"
        e6=f"{f1}{rc(la)}{rc(nmb)}{domain}"
        e7=f"{f1}{rc(la)}{rc(nmb)}{str(rn(1,99))}{domain}"
        e8=f"{f1}{rc(la)}{rc(nmb)}{str(rn(100,999))}{domain}"
        emailG=rc([e1,e2,e3,e4,e5,e6,e7,e8])
        if emailG not in user:
            user.append(emailG)
            sys.stdout.write(f"\r     \033[1;92mDUMPING : \033[1;97m{len(user)}/10000\r"),
            sys.stdout.flush()
        if len(user) >10000:
            break
            



