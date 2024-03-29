def c(file):
    import re
    import parse
    import pdfplumber
    import pandas as pd
    from collections import namedtuple

    Line=namedtuple('Line','SEAT_N0  NAME MECHANICS MECHANLICS_LAB SME SME_LAB BEE BEE_LAB EM_1 EM_1_LAB PHYSICS PHYSICS_LAB WORKSHOP ES_1 GRAPHICS GRAPHICS_LAB BXE BXE_LAB EM_2 EM_2_LAB CHEMISTRY CHEMISTRY_LAB PPS PPS_LAB PBL ES_2 PE DEMOCRACY')
    seatno_re=re.compile(r'(F\B\d{9})')
    seatno_re1=re.compile(r'(SEAT NO.:\B) (.*) NAME :')
    name_re=re.compile(r'(NAME :\B) (.*) MOTHER :')
    patt4=re.compile(r'(\s(\d+)\s)')
    #file="FE-2019 course-result ledger-may-22-22.09.22.pdf"
    file1="cegp010440_S.E.(2019 PAT.)(COMPUTER).pdf"
    lines=[]
    one=''
    two=''
    l1=['','','','','','','','','','','','','','','','','','','','','','','','']
    with pdfplumber.open(file) as pdf:
        pages=pdf.pages
        for page in pdf.pages:
            text=page.extract_text()
            l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for line in text.split('\n'):
                print(line)
                comp = seatno_re1.search(line)
                comp1 = name_re.search(line)
                comp2 = patt4.search(line)
                #print(l1)
                if comp:
                    one=comp.group(2)
                    #print(one)
                if comp1:
                    two=comp1.group(2)
                    #print(one," ",two)
                    #lines.append(Line(one, two))
                if line.startswith("101011"):
                    #print("hi ",l[0])
                    if(l[0]==0):
                        l1[0]=comp2.group(1)
                        #print("do"," ",l1[0]," ha ",l[0])
                        l[0]+=1
                        if(l1[0]==' 04 ' or l1[0]==' 01 ' or l1[0]==' 03 ' or l1[0]==' 02 ' or l1[0]==' 05 ' or l1[0]==' 06 '):
                            l1[0]=' FF '
                        elif(l1[0]==' 00 '):
                            l1[0]=' PP '
                    #print(l[0])
                    else:
                        #print("da")
                        l1[1]=comp2.group(1)
                        l[0]=0
                        if(l1[1]==' 04 ' or l1[1]==' 01 ' or l1[1]==' 03 ' or l1[1]==' 02 ' or l1[1]==' 05 ' or l1[1]==' 06 '):
                            l1[1]=' FF '
                        elif(l1[1]==' 00 '):
                            l1[1]=' FF '
                            
                elif line.startswith("102003"):
                    if(l[1]==0):
                        l1[2]=comp2.group(1)
                        l[1]+=1
                        if(l1[2]==' 04 ' or l1[2]==' 01 ' or l1[2]==' 03 ' or l1[2]==' 02 ' or l1[2]==' 05 ' or l1[2]==' 06 '):
                            l1[2]=' FF '
                        elif(l1[2]==' 00 '):
                            l1[2]=' PP '
                    else:
                        l1[3]=comp2.group(1)
                        l[1]=0
                        if(l1[3]==' 04 ' or l1[3]==' 01 ' or l1[3]==' 03 ' or l1[3]==' 02 ' or l1[3]==' 05 ' or l1[3]==' 06 '):
                            l1[3]=' FF '
                        elif(l1[3]==' 00 '):
                            l1[3]=' PP '
                elif line.startswith("103004"):
                    if(l[2]==0):
                        l1[4]=comp2.group(1)
                        l[2]+=1
                        if(l1[4]==' 04 ' or l1[4]==' 01 ' or l1[4]==' 03 ' or l1[4]==' 02 ' or l1[4]==' 05 ' or l1[4]==' 06 '):
                            l1[4]=' FF '
                        elif(l1[4]==' 00 '):
                            l1[4]=' PP '
                    else:
                        l1[5]=comp2.group(1)
                        l[2]=0
                        if(l1[5]==' 04 ' or l1[5]==' 01 ' or l1[5]==' 03 ' or l1[5]==' 02 ' or l1[5]==' 05 ' or l1[5]==' 06 '):
                            l1[5]=' FF '
                        elif(l1[5]==' 00 '):
                            l1[5]=' PP '
                elif line.startswith("107001"):
                    if(l[3]==0):
                        l1[6]=comp2.group(1)
                        l[3]+=1
                        if(l1[6]==' 04 ' or l1[6]==' 01 ' or l1[6]==' 03 ' or l1[6]==' 02 ' or l1[6]==' 05 ' or l1[6]==' 06 '):
                            l1[6]=' FF '
                        elif(l1[6]==' 00 '):
                            l1[6]=' PP '
                    else:
                        l1[7]=comp2.group(1)
                        l[3]=0
                        if(l1[7]==' 04 ' or l1[7]==' 01 ' or l1[7]==' 03 ' or l1[7]==' 02 ' or l1[7]==' 05 ' or l1[7]==' 06 '):
                            l1[7]=' FF '
                        elif(l1[7]==' 00 '):
                            l1[7]=' PP '
                elif line.startswith("107002"):
                    if(l[4]==0):
                        l1[8]=comp2.group(1)
                        l[4]+=1
                        if(l1[8]==' 04 ' or l1[8]==' 01 ' or l1[8]==' 03 ' or l1[8]==' 02 ' or l1[8]==' 05 ' or l1[8]==' 06 '):
                            l1[8]=' FF '
                        elif(l1[8]==' 00 '):
                            l1[8]=' PP '
                    else:
                        l1[9]=comp2.group(1)
                        l[4]=0
                        if(l1[9]==' 04 ' or l1[9]==' 01 ' or l1[9]==' 03 ' or l1[9]==' 02 ' or l1[9]==' 05 ' or l1[9]==' 06 '):
                            l1[9]=' FF '
                        elif(l1[9]==' 00 '):
                            l1[9]=' PP '
                elif line.startswith("111006"):
                        l1[10]=comp2.group(1)
                        if(l1[10]==' 04 ' or l1[10]==' 01 ' or l1[10]==' 03 ' or l1[10]==' 02 ' or l1[10]==' 05 ' or l1[10]==' 06 '):
                            l1[10]=' FF '
                        elif(l1[10]==' 00 '):
                            l1[10]=' PP '
                elif line.startswith("102012"):
                    if(l[5]==0):
                        l1[11]=comp2.group(1)
                        l[5]+=1
                        if(l1[11]==' 04 ' or l1[11]==' 01 ' or l1[11]==' 03 ' or l1[11]==' 02 ' or l1[11]==' 05 ' or l1[11]==' 06 '):
                            l1[11]=' FF '
                        elif(l1[11]==' 00 '):
                            l1[11]=' PP '
                    else:
                        l1[12]=comp2.group(1)
                        l[5]=0
                        if(l1[12]==' 04 ' or l1[12]==' 01 ' or l1[12]==' 03 ' or l1[12]==' 02 ' or l1[12]==' 05 ' or l1[12]==' 06 '):
                            l1[12]=' FF '
                        elif(l1[12]==' 00 '):
                            l1[12]=' PP '
                elif line.startswith("104010"):
                    if(l[6]==0):
                        l1[13]=comp2.group(1)
                        l[6]+=1
                        if(l1[13]==' 04 ' or l1[13]==' 01 ' or l1[13]==' 03 ' or l1[13]==' 02 ' or l1[13]==' 05 ' or l1[13]==' 06 '):
                            l1[13]=' FF '
                        elif(l1[13]==' 00 '):
                            l1[13]=' PP '
                    else:
                        l1[14]=comp2.group(1)
                        l[6]=0
                        if(l1[14]==' 04 ' or l1[14]==' 01 ' or l1[14]==' 03 ' or l1[14]==' 02 ' or l1[14]==' 05 ' or l1[14]==' 06 '):
                            l1[14]=' FF '
                        elif(l1[14]==' 00 '):
                            l1[14]=' PP '
                elif line.startswith("107008"):
                    if(l[7]==0):
                        l1[15]=comp2.group(1)
                        l[7]+=1
                        if(l1[15]==' 04 ' or l1[15]==' 01 ' or l1[15]==' 03 ' or l1[15]==' 02 ' or l1[15]==' 05 ' or l1[15]==' 06 '):
                            l1[15]=' FF '
                        elif(l1[15]==' 00 '):
                            l1[15]=' PP '
                    else:
                        l1[16]=comp2.group(1)
                        l[7]=0
                        if(l1[16]==' 04 ' or l1[16]==' 01 ' or l1[16]==' 03 ' or l1[16]==' 02 ' or l1[16]==' 05 ' or l1[16]==' 06 '):
                            l1[16]=' FF '
                        elif(l1[16]==' 00 '):
                            l1[16]=' PP '
                elif line.startswith("107009"):
                    if(l[8]==0):
                        l1[17]=comp2.group(1)
                        l[8]+=1
                        if(l1[17]==' 04 ' or l1[17]==' 01 ' or l1[17]==' 03 ' or l1[17]==' 02 ' or l1[17]==' 05 ' or l1[17]==' 06 '):
                            l1[17]=' FF '
                        elif(l1[17]==' 00 '):
                            l1[17]=' PP '
                    else:
                        l1[18]=comp2.group(1)
                        l[8]=0
                        if(l1[18]==' 04 ' or l1[18]==' 01 ' or l1[18]==' 03 ' or l1[18]==' 02 ' or l1[18]==' 05 ' or l1[18]==' 06 '):
                            l1[18]=' FF '
                        elif(l1[18]==' 00 '):
                            l1[18]=' PP '
                elif line.startswith("110005"):
                    if(l[9]==0):
                        l1[19]=comp2.group(1)
                        l[9]+=1
                        if(l1[19]==' 04 ' or l1[19]==' 01 ' or l1[19]==' 03 ' or l1[19]==' 02 ' or l1[19]==' 05 ' or l1[19]==' 06 '):
                            l1[19]=' FF '
                        elif(l1[19]==' 00 '):
                            l1[19]=' PP '
                    else:
                        l1[20]=comp2.group(1)
                        l[9]=0
                        if(l1[20]==' 04 ' or l1[20]==' 01 ' or l1[20]==' 03 ' or l1[20]==' 02 ' or l1[20]==' 05 ' or l1[20]==' 06 '):
                            l1[20]=' FF '
                        elif(l1[20]==' 00 '):
                            l1[20]=' PP '
                elif line.startswith("110013"):
                    l1[21]=comp2.group(1)
                    if(l1[21]==' 04 ' or l1[21]==' 01 ' or l1[21]==' 03 ' or l1[21]==' 02 ' or l1[21]==' 05 ' or l1[21]==' 06 '):
                            l1[21]=' FF '
                    elif(l1[21]==' 00 '):
                        l1[21]=' PP '
                    #print("hello")
                    #print(lines)
                    lines.append(Line(one, two,l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7],l1[8],l1[9],l1[10],'  AC',l1[11],l1[12],l1[13],l1[14],l1[15],l1[16],l1[17],l1[18],l1[19],l1[20],l1[21],'  AC','  AC','  AC'))
    df=pd.DataFrame(lines)
    df.head()
    df.info()
    s=df.to_csv('pr_33.csv',index=False)
    return s
"""f="home\FE-2019 course-result ledger-may-22-22.09.22.pdf"
a=c(f)
print(type(a))"""
def s(file1):
    import re
    import parse
    import pdfplumber
    import pandas as pd
    from collections import namedtuple


    sub=['SEAT_NO','NAME','DISCRETE_MATHEMATICS','FUND_DATA_STRUCTURE','OOP','COMPUTER_GRAPHICS','DELD','DATA_STRUC_LAB','OOP_CG_LAB','DELD_LAB','BCSL','HSS','AUDIT_COURSE1','EM_III','EM_III_LAB','DSA','SOFTWARE_ENGG','MICROPROCESSOR','PPL','DSAL','MICROPROCESSOR_LAB','PBL_II','CODE_OF_CONDUCT','AUDIT_COURSE_II']
    """ n=int(input("Enter the number of subjects?"))
    for i in range(n):
        sub.append(input())"""
    Line=namedtuple('Line',sub)

    seatno_re=re.compile(r'(S\B\d{9})')
    seatno_re1=re.compile(r'(SEAT NO.:\B) (.*) NAME :')
    name_re=re.compile(r'(NAME :\B) (.*) MOTHER :')
    patt4=re.compile(r'(\s(\d+)\s)')
    #patt=re.compile(r'\s{4}(\d+)')
    patt=re.compile(r'\A(\d{2})')
    patt2=re.compile(r'\s{3}(\d+)')
    #file="FE-2019 course-result ledger-may-22-22.09.22.pdf"
    #file1="cegp010440_S.E.(2019 PAT.)(COMPUTER).pdf"
    file2="T.E.(2019 PAT.)(COMPUTER).pdf"
    lines=[]
    one=''
    two=''
    l=[]
    with pdfplumber.open(file1) as pdf:
        pages=pdf.pages
        for page in pdf.pages:
            text=page.extract_text()
            count=0
            for line in text.split('\n'):
                comp = seatno_re1.search(line)
                comp1 = name_re.search(line)
                comp2 = patt4.search(line)
                comp3=patt.search(line)
                comp4=patt2.search(line)
                
                if comp:
                    l.append(comp.group(2))

                    #print(one)
                if comp1:
                    
                    l.append(comp1.group(2))

                if comp3:
                    #print(comp2)
                    l.append(comp2.group(0))
                    if(l[len(l)-1]==' 04 ' or l[len(l)-1]==' 01 ' or l[len(l)-1]==' 03 ' or l[len(l)-1]==' 02 ' or l[len(l)-1]==' 05 ' or l[len(l)-1]==' 06 '):
                        l.remove(l[len(l)-1])
                        
                        l.append(' FF ')
                    elif(l[len(l)-1]==' 00 '):
                        l.remove(l[len(l)-1])
                        l.append(' PP ')

                if line.startswith('SECOND'):
                    #print(len(l))
                    for j in range(len(l),24):
                        l.append("--")
                    lines.append(Line(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17],l[18],l[19],l[20],l[21],l[22],l[23]))

                    l=[]

    df=pd.DataFrame(lines)
    df.head()
    df.info()
    df.to_csv('pr_33.csv',index=False)

def t(file):
    import re
    import parse
    import pdfplumber
    import pandas as pd
    from collections import namedtuple


                
    sub=['SEAT_NO','NAME','DISTRIBUTED_SYSTEMS','COMPUTER_NETWORK','OPERATING_SYSTEM','THEORY_OF_COMPUTATION','DATABASE_MANAGEMENT_SYSTEMS','SEMINAR_AND_TECHNOLOGY','LABORATORY_PRACTICE_1','DATABASE_MANAGEMENT_SYSTEMS_LAB','COMPUTER_NETWORK_LAB','AUDIT_COURSE','HONOURS','HONOURS_LAB','LABORATORY_PRACTICE_2','INTERNSHIP','CLOUD_COMPUTING','ARTIFICIAL_INTELLIGENCE','WEB_TECHNOLOGY_LAB','WEB_TECHNOLOGY','DATA_SCIENCE_LAB','DATA_SCIENCE','DIGITAL_AND_SOCIAL_MEDIA_MARKETING','HONOURS_2']
    """n=int(input("Enter the number of subjects?"))
    for i in range(n):
        sub.append(input())"""
    Line=namedtuple('Line',sub)

    seatno_re=re.compile(r'(S\B\d{9})')
    seatno_re1=re.compile(r'(SEAT NO.:\B) (.*) NAME :')
    name_re=re.compile(r'(NAME :\B) (.*) MOTHER :')
    patt4=re.compile(r'(\s(\d+)\s)')
    """patt=re.compile(r'\s{4}(\d+)')"""
    patt=re.compile(r'\A(\d+)')
    patt2=re.compile(r'\s{3}(\d+)')
    #file="FE-2019 course-result ledger-may-22-22.09.22.pdf"
    file1="cegp010440_S.E.(2019 PAT.)(COMPUTER).pdf"
    file2="T.E.(2019 PAT.)(COMPUTER).pdf"
    lines=[]
    one=''
    two=''
    l=[]
    with pdfplumber.open(file) as pdf:
        pages=pdf.pages
        for page in pdf.pages:
            text=page.extract_text()
            count=0
            for line in text.split('\n'):
                comp = seatno_re1.search(line)
                comp1 = name_re.search(line)
                comp2 = patt4.search(line)
                comp3=patt.search(line)
                comp4=patt2.search(line)

                if comp:
                    l.append(comp.group(2))

                    #print(one)
                if comp1:

                    l.append(comp1.group(2))
                if (line.startswith("SEM.:2") and len(l)==12):
                    l.append("--")
                    l.append("--")
                if comp3:

                    l.append(comp2.group(0))
                    if(l[len(l)-1]==' 04 ' or l[len(l)-1]==' 01 ' or l[len(l)-1]==' 03 ' or l[len(l)-1]==' 02 ' or l[len(l)-1]==' 05 ' or l[len(l)-1]==' 06 '):
                        l.remove(l[len(l)-1])
                        print("hi")
                        l.append(' FF ')
                    elif(l[len(l)-1]==' 00 '):
                        l.remove(l[len(l)-1])
                        l.append(' PP ')

                if line.startswith('THIRD'):
                    print(len(l))
                    for i in range(len(l),24):
                        l.append("--")
                    lines.append(Line(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17],l[18],l[19],l[20],l[21],l[22],l[23]))

                    l=[]

    df=pd.DataFrame(lines)
    df.head()
    df.info()
    df.to_csv('pr_33.csv',index=False)
 
def b(file):
    import re
    import parse
    import pdfplumber
    import pandas as pd
    from collections import namedtuple

    sub=['SEAT_NO','NAME','DESIGN_AND_ANALYSIS_OF_ALGORITHM','MACHINE_LEARNING','BLOCKCHAIN_TECHNOLOGY','ELECTIVE_III','ELECTIVE_IV','LABROTARY_PRACTICE_III','LABROTARY_PRACTICE_IV','PROJECT_STAGE_I','H0N_MACHINE_LEARNING','H0N_MACHINE_LEARNING_LAB','AUDIT_COURSE']
    l=[]
    file1="Nov 2022_B.E. (2019 PAT.)(COMPUTER).pdf"

    Line=namedtuple('Line',sub)

    seatno_re=re.compile(r'(S\B\d{9})')
    seatno_re1=re.compile(r'(SEAT NO.:\B) (.*) NAME :')
    name_re=re.compile(r'(NAME :\B) (.*) MOTHER :')
    patt4=re.compile(r'(\s(\d+)\s)')
    """patt=re.compile(r'\s{4}(\d+)')"""
    patt=re.compile(r'\A(\d+)')
    patt2=re.compile(r'\s{3}(\d+)')
    lines=[]
    one=''
    two=''

    with pdfplumber.open(file) as pdf:
        pages=pdf.pages
        for page in pdf.pages:
            text=page.extract_text()
            count=0
            for line in text.split('\n'):
                comp = seatno_re1.search(line)
                comp1 = name_re.search(line)
                comp2 = patt4.search(line)
                comp3=patt.search(line)
                comp4=patt2.search(line)
                
                if comp:
                    l.append(comp.group(2))

                    #print(one)
                if comp1:
                    
                    l.append(comp1.group(2))
                if line.startswith('410249'):
                    print("hi")
                    if(len(l)==10):
                        l.append(' -- ')
                        l.append(' -- ')
                        l.append(' PP ')
                elif comp3:
                    #print(comp2)
                            
                    l.append(comp2.group(0))
                    if(l[len(l)-1]==' 04 ' or l[len(l)-1]==' 01 ' or l[len(l)-1]==' 03 ' or l[len(l)-1]==' 02 ' or l[len(l)-1]==' 05 ' or l[len(l)-1]==' 06 '):
                        l.remove(l[len(l)-1])
                        print("hi")
                        l.append(' FF ')
                    elif(l[len(l)-1]==' 00 '):
                        l.remove(l[len(l)-1])
                        l.append(' PP ')        
                       
                if line.startswith('SGPA1'):
                    print(l)
                    for j in range(len(l),13):
                        l.append("--")
                    lines.append(Line(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12]))
                    
                    l=[]

    df=pd.DataFrame(lines)
    df.head()
    df.info()
    df.to_csv('pr_33.csv',index=False)
