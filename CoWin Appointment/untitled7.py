import datetime
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame,Paragraph,Spacer
from reportlab.lib.units import cm

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

message="""<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**<br></br><b>Pin-code</b>: 411011<br></br><b>Available on</b>: 15-05-2021<br></br><b>Centre</b>: Kamala Nehru Hosp<br></br><b>Block</b>: Haveli<br></br><b>Price</b>: Free<br></br><b>Available Capacity</b>:<b>0</b><br></br><b>Vaccine</b>: COVAXIN<br></br>**"""
num="+91-55"
def generate_report(num,message):
    pdf=canvas.Canvas(num+".pdf")
    flow_obj1=[]
    flow_obj2=[]
    flow_obj3=[]
    pdf.translate(cm,cm)

    frame1=Frame(10,660,540,80,showBoundary=1)
    
    frame2=Frame(10,590,540,60,showBoundary=1)
    
    frame3=Frame(10,0,540,580,showBoundary=1)
    
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
    
    text6=message
    t6=Paragraph(text6,style=styles["Normal"])
    flow_obj3.append(t6)
    frame3.addFromList(flow_obj3, pdf)
    pdf.showPage()
   
  
    text6="Hi mom"
    frame3=Frame(10,0,540,580,showBoundary=1)
    t6=Paragraph(text6,style=styles["Normal"])
    flow_obj3.append(t6)
    frame3.addFromList(flow_obj3, pdf)
    pdf.showPage()
    
    pdf.save()
            
generate_report(num,message)
            
            
    
    

