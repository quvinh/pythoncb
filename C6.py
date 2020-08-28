km = float(input("Nhap so km:"))
t = 0
if km<=1:
    t = 15
if km>1 and km<=5:
    t = 15 + (km-1)*13.5
if km>5 and km<=120:
    t = 15 + 4*13.5 + (km-5)*11
if km>120:
    t = 15 + 4*13.5 + (km-5)*11 - (15 + 4*13.5 + (km-5)*11)*0.1

print("So tien taxi: %.3f vnd"%t)
