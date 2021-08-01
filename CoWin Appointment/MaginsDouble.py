import datetime
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame,Paragraph,Spacer
from reportlab.lib.units import cm

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
message="""

<br></br><b>Pin-code1</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code2</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code3</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code4</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code5</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 

<br></br><b>Pin-code6</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code10</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 


<br></br><b>Pin-code11</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code12</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code13</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code14</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code15</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 

<br></br><b>Pin-code16</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code20</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>
<br></br><b>Pin-code16</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code20</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>
<br></br><b>Pin-code16</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code20</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>
<br></br><b>Pin-code16</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code20</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>

<br></br><b>Pin-code16</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code20</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>

<br></br><b>Pin-code16</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>** 
<br></br><b>Pin-code20</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>"""
num="+91-55"
def generate_report(num,message):
    
    pdf=canvas.Canvas(num+".pdf",pagesize=letter)
    flow_obj1=[]
    flow_obj2=[]
    flow_obj3=[]
    pdf.translate(cm,cm)

    frame1=Frame(10,660,540,80,showBoundary=1)
    
    frame2=Frame(10,590,540,60,showBoundary=1)
    
    frame3=Frame(10,0,540,580,showBoundary=1)
    frame1R=Frame(270,-10.755,540,580,showBoundary=0)
   
    
    styles=getSampleStyleSheet()
    text1="""<b><font size=26>  VACCINE SLOT AVAILABILITY REPORT</font></b><br></br><br></br> <br></br>"""
    t1=Paragraph(text1,style=styles["Normal"])
    flow_obj1.append(t1)
    flow_obj1.append(Spacer(6,6))
    text2="""<b>Generated on:</b>""" +" "+str(datetime.datetime.now())
    t2=Paragraph(text2,style=styles["Normal"])
    flow_obj1.append(t2)
    
    text3="""<b>Requested by:</b>""" +" "+num
    t3=Paragraph(text3,style=styles["Normal"])
    

    
    flow_obj1.append(t3)
    
    frame1.addFromList(flow_obj1, pdf)
    
    
    text4="""<b>Disclaimer:</b><br></br> This service is developed using  <u>https://apisetu.gov.in/public/api/cowin</u>  to find appointment availabilty. These APIs are available for use by all third party applications. The appointment availability data is cached and may be upto 30 minutes old. 
    Book vaccination slots using  <u>https://selfregistration.cowin.gov.in/</u>."""
    t4=Paragraph(text4,style=styles["Normal"])
    

    flow_obj2.append(t4)
     
    frame2.addFromList(flow_obj2, pdf)
    
    text5="""<b><font >Vaccination Slots:</font></b><br></br>"""
    t5=Paragraph(text5,style=styles["Normal"])
    flow_obj3.append(t5)
  #  frame3.addFromList(flow_obj3, pdf)
    
    
    # text6=message
    # t6=Paragraph(text6,style=styles["Normal"])
    # flow_obj3.append(t6)
    # frame3.addFromList(flow_obj3, pdf)
    
    # pdf.showPage()
        # pdf.showPage()
    message=message.split("**")


    n=len(message)
    print(len(message),n)
  
    for i in range(0,10,5):
           content=""
           if(i<5+i):
               content+=message[i]
           if(i+1<5+i):
               content+=message[i+1]
           if(i+2<5+i):
               content+=message[i+2]
           if(i+3<5+i):
               content+=message[i+3]
           if(i+4<5+i):
               content+=message[i+4]
           # text6=content
           # t6=Paragraph(text6,style=styles["Normal"])
           # flow_obj3.append(t6)
           # frame3.addFromList(flow_obj3, pdf)
           # pdf.showPage()    
         
           if i+4<=5:
                text6=content
                t6=Paragraph(text6,style=styles["Normal"])
                flow_obj3.append(t6)
                frame3.addFromList(flow_obj3, pdf)
               
                
           else:
                flow_obj3R=[]
                text6=content
                print("CONTENT \n"+content)
                t6=Paragraph(text6,style=styles["Normal"])
                flow_obj3R.append(t6)
                frame1R.addFromList(flow_obj3R, pdf)
                
                


    pdf.showPage()
    
    # left=0
    # right=1
    toggle=0
    # 0: Left
    # 1: Right
    if n>9:
        frame3R=Frame(40,20  ,540,740,showBoundary=1)
        frame3L=Frame(300,20  ,540,740,showBoundary=0)
        
        for i in range(10,len(message),7):
            
            content=""           
            if(i<n):
                content+=message[i]
            if(i+1<n):
                content+=message[i+1]
            if(i+2<n):
                content+=message[i+2]
            if(i+3<n):
                content+=message[i+3]
            if(i+4<n):
                content+=message[i+4]
            if(i+5<n):    
                content+=message[i+5]
            if(i+6<n):
                content+=message[i+6]
                    
            if toggle==0:
                flow_obj3=[]
                frame3R.addFromList(flow_obj3, pdf)
                text6=content
                t6=Paragraph(text6,style=styles["Normal"])
                flow_obj3.append(t6)
                frame3R.addFromList(flow_obj3, pdf)
                toggle=1
                # continue
            if toggle==1:
                flow_obj3=[]
                frame3L.addFromList(flow_obj3, pdf)
                text6=content
                t6=Paragraph(text6,style=styles["Normal"])
                flow_obj3.append(t6)
                frame3L.addFromList(flow_obj3, pdf)
                toggle=0
            pdf.showPage()
           
       #  frame3.addFromList(flow_obj3, pdf)
       
       #  pdf.showPage()
       #  pdf.showPage()
       #  pdf.showPage()
       #  pdf.showPage()
    pdf.showPage()
    pdf.save()
            
generate_report(num,message)

