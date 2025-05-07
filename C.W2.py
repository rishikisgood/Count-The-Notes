Amount=int(input("Please Enter Amount for Withdraw:"))

note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10

print("Notes of 100 Rs=", note_1)
print("Notes of 50 Rs=", note_2)
print("Notesof 10 Rs=", note_3)



