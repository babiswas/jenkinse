import csv
with open('test.csv','w',newline='') as file:
     fieldnames=["name","email"]
     writer=csv.DictWriter(file,fieldnames=fieldnames)
     writer.writeheader()
     for obj in [("hello","bello"),("bello","tello")]:
         writer.writerow({"name":obj[0],"email":obj[1]})

    
