import pywhatkit 
   
try: 
     
  # send message 
  pywhatkit.sendwhatmsg("+522221818476","Hola mundo!",18, 46)#Time
  # Send an Image to a Group with the Caption as Hello
  pywhatkit.sendwhats_image("PruebaSend", "Images/Hello.png", "Hello")
  # Send an Image to a Contact with the no Caption
  pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")
  # Send a WhatsApp Message to a Group at 12:00 AM
  pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)
  # Send a WhatsApp Message to a Group instantly
  pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!") 
  print("Successfully Sent!")
   
except: 
  #print the error
  print("Ha ocurrido un error!")