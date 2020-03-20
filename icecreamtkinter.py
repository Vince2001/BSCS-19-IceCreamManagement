from tkinter import*
import tkinter as tk

root=Tk()
root.geometry("1250x600")
root.title("Ice Cream Store")
root.resizable(False,False)

Tops = Frame (root, width = 1350, height=350, bd= 12, relief="raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('Brush Script MT', 50),bg="yellow", text="\t\tIce Cream Store\t\t\t")
lblTitle.grid(row =0, column=0)

Bottom = Frame (root, width = 1350 , height=600, bg="navy blue", bd= 12, relief="raise")
Bottom.pack(side=BOTTOM)

frame1 = Frame (Bottom, width = 1350 , height=500, bd= 12, relief="raise")
frame1.pack(side=LEFT)
frame2 = Frame (Bottom, width = 1350 , height=500, bd= 12, relief="raise")
frame2.pack(side=LEFT)
frame3 = Frame (Bottom, width = 1350 , height=500, bd= 12, relief="raise")
frame3.pack(side=RIGHT)

#VARIATION

iTotal1 = IntVar()
iTotal2 = IntVar()
iTotal3 = IntVar()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()


var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)


#Originals Flavors
varPandan =StringVar()
varChocolate =StringVar()
varVanilla =StringVar()
varCheese =StringVar()
varUbe =StringVar()
varStrawberies =StringVar()
varMocha =StringVar()
varOreo =StringVar()

#International Flavors
varBananasplit =StringVar()
varUbedalas =StringVar()
varConSenordelpablo =StringVar()

#Others
varWater =StringVar()
varExtra =StringVar()

varTotal =StringVar()


#Originals Flavors
varPandan.set("0")
varChocolate.set("0")
varVanilla.set("0")
varCheese.set("0")
varUbe.set("0")
varStrawberies.set("0")
varMocha.set("0")
varOreo.set("0")

#International Flavors
varBananasplit.set("0")
varUbedalas.set("0")
varConSenordelpablo.set("0")

#Others
varWater.set("0")
varExtra.set("0")

varTotal.set("0")


def Reset():
    varPandan.set("0")
    varChocolate.set("0")
    varVanilla.set("0")
    varCheese.set("0")
    varUbe.set("0")
    varStrawberies.set("0")
    varMocha.set("0")
    varOreo.set("0")

#International Flavors
    varBananasplit.set("0")
    varUbedalas.set("0")
    varConSenordelpablo.set("0")

#Others
    varWater.set("0")
    varExtra.set("0")

    varTotal.set("0")
   

    txtPandan.configure(state =DISABLED)
    txtChocolate.configure(state = DISABLED)
    txtVanilla.configure(state = DISABLED)
    txtCheese.configure(state = DISABLED)
    txtUbe.configure(state = DISABLED)
    txtStrawberies.configure(state = DISABLED)
    txtMocha.configure(state = DISABLED)
    txtOreo.configure(state = DISABLED)
    txtBananaSplit.configure(state = DISABLED)
    txtUbeDalas.configure(state = DISABLED)
    txtConSenordelpablo.configure(state = DISABLED)
    txtWater.configure(state = DISABLED)
    txtExtra.configure(state = DISABLED)
    txtTotal.configure(state = DISABLED)
#=============== This is for to check the box if you order also you can type the quantity
def checkPandan():
    if (var1.get() == 1):
        txtPandan.configure(state = NORMAL)
        varPandan.set("")
    elif (var1.get() == 0):
        txtPandan.configure(state = DISABLED)
        varPandan.set("0")

def checkChocolate():
    if (var2.get() == 1):
        txtChocolate.configure(state = NORMAL)
        varChocolate.set("")
    elif (var2.get() == 0):
        txtChocolate.configure(state = DISABLED)
        varChocolate.set("0")

def checkVanilla():
    if (var3.get() == 1):
        txtVanilla.configure(state = NORMAL)
        varVanilla.set("")
    elif (var13.get() == 0):
        txtVanilla.configure(state = DISABLED)
        varVanilla.set("0")

def checkCheese():
    if (var4.get() == 1):
        txtCheese.configure(state = NORMAL)
        varCheese.set("")
    elif (var4.get() == 0):
        txtCheese.configure(state = DISABLED)
        varCheese.set("0")

def checkUbe():
    if (var5.get() == 1):
        txtUbe.configure(state = NORMAL)
        varUbe.set("")
    elif (var5.get() == 0):
        txtUbe.configure(state = DISABLED)
        varUbe.set("0")

def checkStrawberies():
    if (var6.get() == 1):
        txtStrawberies.configure(state = NORMAL)
        varStrawberies.set("")
    elif (var6.get() == 0):
        txtStrawberies.configure(state = DISABLED)
        varStrawberies.set("0")

def checkMocha():
    if (var7.get() == 1):
        txtMocha.configure(state = NORMAL)
        varMocha.set("")
    elif (var7.get() == 0):
        txtMocha.configure(state = DISABLED)
        varMocha.set("0")

def checkOreo():
    if (var8.get() == 1):
        txtOreo.configure(state = NORMAL)
        varOreo.set("")
    elif (var8.get() == 0):
        txtOreo.configure(state = DISABLED)
        varOreo.set("0")

def checkBananaSplit():
    if (var9.get() == 1):
        txtBananaSplit.configure(state = NORMAL)
        varBananasplit.set("")
    elif (var9.get() == 0):
        txtBananaSplit.configure(state = DISABLED)
        varBananasplit.set("0")
        
def checkUbeDalas():
    if (var10.get() == 1):
        txtUbeDalas.configure(state = NORMAL)
        varUbedalas.set("")
    elif (var10.get() == 0):
        txtUbeDalas.configure(state = DISABLED)
        varUbedalas.set("0")

def checkConSenordelpablo():
    if (var11.get() == 1):
        txtConSenordelpablo.configure(state = NORMAL)
        varConSenordelpablo.set("")
    elif (var11.get() == 0):
        txtConSenordelpablo.configure(state = DISABLED)
        varConSenordelpablo.set("0")

def checkWater():
    if (var12.get() == 1):
        txtWater.configure(state = NORMAL)
        varWater.set("")
    elif (var12.get() == 0):
        txtWater.configure(state = DISABLED)
        varWater.set("0")

def checkExtra():
    if (var13.get() == 1):
        txtExtra.configure(state = NORMAL)
        varExtra.set("")
    elif (var13.get() == 0):
        txtExtra.configure(state = DISABLED)
        varExtra.set("0")
#=================== This is for cost and also total=====================
def totalofmeal():
    order1 = float(varPandan.get())
    order2 = float(varChocolate.get())
    order3 = float(varVanilla.get())
    order4 = float(varCheese.get())
    order5 = float(varUbe.get())
    order6 = float(varStrawberies.get())
    order7 = float(varMocha.get())
    order8 = float(varOreo.get())
    order9 = float(varBananasplit.get())
    order10 = float(varUbedalas.get())
    order11 = float(varConSenordelpablo.get())
    order12 = float(varWater.get())
    order13 = float(varExtra.get())

    iTotal1.set((order1 * 50) + (order2 * 35) + (order3 * 35) + (order4 * 40))
    iTotal2.set((order5 * 40) + (order6 * 50) + (order7 * 45) + (order8 * 55))
    iTotal3.set((order9 * 75) + (order10 * 65) + (order11 * 80) + (order12 * 10) + (order13 * 7))
    iCost = (iTotal1.get() + iTotal2.get() + iTotal3.get())
    varTotal.set(iCost)
#===========================================FRAME 1==============================================#
lblTatakPinoy =Label(frame1, font=('Brush Script MT', 26, 'bold'), text="Original Flavors")
lblTatakPinoy.grid(row =0, column=0)

Pandan =Checkbutton(frame1, text="Panda---Php.50.00", variable=var1, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkPandan).grid(row=1, column=0, sticky=W)
txtPandan = Entry(frame1,font=('arial', 18, 'bold'), textvariable =varPandan, width=6, justify=RIGHT, state =DISABLED)
txtPandan.grid(row =1, column =1)

Chocolate =Checkbutton(frame1, text="Chocolate---Php.35.00", variable=var2, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkChocolate).grid(row=2, column=0, sticky=W)
txtChocolate = Entry(frame1,font=('arial', 18, 'bold'), textvariable =varChocolate, width=6, justify=RIGHT, state =DISABLED)
txtChocolate.grid(row=2, column=1)

Vanilla =Checkbutton(frame1, text="Vanilla----Php.35.00", variable=var3, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkVanilla).grid(row=3, column=0, sticky=W)
txtVanilla = Entry(frame1,font=('arial', 18, 'bold'), textvariable =varVanilla, width=6, justify=RIGHT, state =DISABLED)
txtVanilla.grid(row =3, column =1)

Cheese =Checkbutton(frame1, text="Cheese-----Php.40.00", variable=var4, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkCheese).grid(row=4, column=0, sticky=W)
txtCheese = Entry(frame1,font=('arial', 18, 'bold'), textvariable =varCheese, width=6, justify=RIGHT, state =DISABLED)
txtCheese.grid(row=4, column=1)

Ube =Checkbutton(frame1, text="Ube--------Php.40.00", variable=var5, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkUbe).grid(row=5, column=0, sticky=W)
txtUbe = Entry(frame1,font=('arial', 18, 'bold'), textvariable =varUbe, width=6, justify=RIGHT, state =DISABLED)
txtUbe.grid(row =5, column =1)

Strawberies =Checkbutton(frame1, text="Strawberies---Php.50.00", variable=var6, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkStrawberies).grid(row=6, column=0, sticky=W)
txtStrawberies = Entry(frame1,font=('arial', 18, 'bold'), textvariable =varStrawberies, width=6, justify=RIGHT, state =DISABLED)
txtStrawberies.grid(row=6, column=1)

Mocha =Checkbutton(frame1, text="Mocha-----Php.45.00", variable=var7, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkMocha).grid(row=7, column=0, sticky=W)
txtMocha = Entry(frame1,font=('arial', 18, 'bold'), textvariable =varMocha, width=6, justify=RIGHT, state =DISABLED)
txtMocha.grid(row=7, column=1)

Oreo =Checkbutton(frame1, text="Oreo-----Php.55.00", variable=var8, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkOreo).grid(row=8, column=0, sticky=W)
txtOreo = Entry(frame1,font=('arial', 18, 'bold'), textvariable =varOreo, width=6, justify=RIGHT, state =DISABLED)
txtOreo.grid(row=8, column=1)


#===========================================FRAME 2==============================================#

lblTatakPinoy =Label(frame2, font=('Brush Script MT', 26, 'bold'), text="International Flavors")
lblTatakPinoy.grid(row =0, column=0)

BananaSplit =Checkbutton(frame2, text="BananaSplit--Php.75.00", variable=var9, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkBananaSplit).grid(row=1, column=0, sticky=W)
txtBananaSplit = Entry(frame2,font=('arial', 18, 'bold'), textvariable =varBananasplit, width=6, justify=RIGHT, state =DISABLED)
txtBananaSplit.grid(row =1, column =1)

UbeDalas =Checkbutton(frame2, text="Ube Dalas-----Php.65.00", variable=var10, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkUbeDalas).grid(row=2, column=0, sticky=W)
txtUbeDalas = Entry(frame2,font=('arial', 18, 'bold'), textvariable =varUbedalas, width=6, justify=RIGHT, state =DISABLED)
txtUbeDalas.grid(row=2, column=1)

ConSenordelpablo =Checkbutton(frame2, text="ConBBCream--Php.80.00", variable=var11, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkConSenordelpablo).grid(row=3, column=0, sticky=W)
txtConSenordelpablo = Entry(frame2,font=('arial', 18, 'bold'), textvariable =varConSenordelpablo, width=6, justify=RIGHT, state =DISABLED)
txtConSenordelpablo.grid(row =3, column =1)

#=========================================frame 2 but it has extras=================================================#

lblTatakPinoy1 =Label(frame2, font=('Brush Script MT', 26, 'bold'), text="Others")
lblTatakPinoy1.grid(row =4, column=0)


Water =Checkbutton(frame2, text="Bottled Water--Php.10.00", variable=var12, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkWater).grid(row=5, column=0, sticky=W)
txtWater = Entry(frame2,font=('arial', 18, 'bold'), textvariable =varWater, width=6, justify=RIGHT, state =DISABLED)
txtWater.grid(row =5, column =1)

Extra =Checkbutton(frame2, text="Extra Chocolate Syrup--Php.7.00", variable=var13, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=checkExtra).grid(row=6, column=0, sticky=W)
txtExtra = Entry(frame2,font=('arial', 18, 'bold'), textvariable =varExtra, width=6, justify=RIGHT, state =DISABLED)
txtExtra.grid(row=6, column=1)


#=============================================FRAME 3====================================================#
lblPayment = Label(frame3, font=('Brush Script MT', 26, 'bold'), text="Payments", bd=7, width= 6)
lblPayment.grid(row=0, column=0)


lblTotal = Label(frame3, font=('arial', 15, 'bold'), text="Total", bd=7, width= 6, anchor='w')
lblTotal.grid(row= 3, column= 1)
txtTotal = Entry(frame3, font=('arial', 15, 'bold'), textvariable =varTotal, width= 4, justify='right', state =DISABLED)
txtTotal.grid(row= 3, column= 2)

#=============================================== BUTTONS =================================================#

btnTotal=Button(frame3,padx=16,pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width= 5,
                text="Total", command =totalofmeal).grid(row= 4, column= 0)

btnReset=Button(frame3,padx=16,pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width= 5,
            text="Reset", command =Reset).grid(row= 4,column= 1)



root.mainloop()
                    
