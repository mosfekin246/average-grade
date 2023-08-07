bangla = int(input(("Enter your bangla marks: ")))
english = int(input(("Enter your english marks: ")))
maths = int(input(("Enter your maths marks: ")))
science= int(input(("Enter your science marks: ")))

avg = round((bangla+english+maths+science)/4)

print("Final grade sheet")
if(avg>=91):
    print("Bangla ->", bangla,"\nEnglish ->", english, "\nmaths ->", maths, "\nScience->", science, "\naverage marks ->", avg, "\naverage grade -> A+")
if(avg>=81):
    print("Bangla ->", bangla,"\nEnglish ->", english, "\nmaths ->", maths, "\nScience->", science, "\naverage marks ->", avg, "\naverage grade -> A" )
if(avg>=71):
    print("Bangla ->", bangla,"\nEnglish ->", english, "\nmaths ->", maths, "\nScience->", science, "\naverage marks ->", avg, "\naverage grade -> B")
if(avg>=61):
    print("Bangla ->", bangla,"\nEnglish ->", english, "\nmaths ->", maths, "\nScience->", science, "\naverage marks ->", avg, "\naverage grade -> C")
if(avg>=41):
    print("Bangla ->", bangla,"\nEnglish ->", english, "\nmaths ->", maths, "\nScience->", science, "\naverage marks ->", avg, "\naverage grade -> D")
else:
    print("Bangla ->", bangla,"\nEnglish ->", english, "\nmaths ->", maths, "\nScience->", science, "\naverage marks ->", avg, "\naverage grade -> F")

