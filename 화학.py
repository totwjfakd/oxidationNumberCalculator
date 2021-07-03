from tkinter import *
from tkinter import ttk
from tkinter import messagebox




def cal() :
        global An, Bn,  Ay, By, Aq, Bq,  Aw, Bw, end

        g1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
        g2 = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra']
        metal = ['Ti', 'V', 'Cr', 'Zn', 'Mn', 'Fe', 'Cu', 'Ag', 'Cd']
        g13 = ['B', 'Al', 'Ga']
        g14 = ['C', 'Si', 'Ge', 'Pb']
        g15 = ['N', 'P', 'As', 'Sd', 'Bi']
        g16 = ['O', 'S', 'Se', 'Te']
        g17 =  ['F', 'Cl', 'Br', 'I',]

        Aq = 0.0
        Bq = 0.0
        Aw = 0.0
        Bw = 0.0

        '''
        An = input ("첫번째 원소기호는?")

        Ay = float(input ("첫번째 원소의 원자 개수는?"))

        Bn = input ("두번째 원소기호는?")

        By = float(input ("두번째 원소의 원자 개수는?"))
        '''

        An = mf1.get()
        Ay = float(mf2.get())
        Bn = mf3.get()
        By = float(mf4.get())

        if An == 'F':
                    Aq = -1
        else:
                    if Bn == 'F':
                              Bq = -1

        if An in g1:
                    Aq = 1
        if An in g2:
                    Aq = 2
        if Bn in g1:
                    Bq = 1
        if Bn in g2:
                    Bq = 2


        if An == 'Al':
                    Aq = 3
        else:
                    if Bn == 'Al':
                            Bq = 3




        if Bn == 'H':
                    if An in g1:
                            Bq = -1
                    else:
                            if An in g2:
                                        Bq = -1

                            else:
                                        Bq = 1
        if An == 'H':
                    Aq = 1



        if An == 'O':
                    if Bq == 0:
                            Aq = -2
        if Bn == 'O':
                    if Aq == 0:
                            Bq = -2



        if An in g17:
                    if Bq == 0:
                            Aq = -1
        if Bn in g17:
                    if Aq == 0:
                            Bq = -1


        if Aq != 0:
                    if Bq != 0:
                            messagebox.showinfo("계산 결과", "%s 의 산화수는 %d, %s의 산화수는 %d 입니다."% (An, Aq, Bn, Bq))

                    if Bq == 0:
                            Bw = 0 - Aq * Ay
                            Bq = Bw/By
                            messagebox.showinfo("계산 결과",  "%s 의 산화수는 %d, %s의 산화수는 %d 입니다."% (An, Aq, Bn, Bq))
                            

        else:
                    if Bq != 0:
                            Aw = 0 -  Bq * By
                            Aq = Aw/Ay
                            messagebox.showinfo("계산 결과", "%s 의 산화수는 %d, %s의 산화수는 %d 입니다."% (An, Aq, Bn, Bq))
                    else:
                            messagebox.showinfo("계산 결과", "계산할수없어요..ㅎ")
                            



root = Tk()
root.geometry("300x250")
root.title("산화수 계산기")


first = Frame(root)
first.grid(row = 0, column = 0, sticky = N)
main_lbl = Label(first, text = "산화수 계산기")
main_lbl.grid(row = 0, column = 0)

none_lbl = Label(first, text = " ")
none_lbl.grid(row = 1, column = 0)

mf1_lbl = Label(first, text = "첫번째 원소의 기호")
mf1_lbl.grid(row = 2, column = 0)
mf1 = Entry(first, width = 10)
mf1.grid (row = 2, column = 1)

mf2_lbl = Label(first, text = "첫번째 원소의 원자개수")
mf2_lbl.grid(row = 3, column = 0)
mf2 = Entry(first, width = 10)
mf2.grid (row = 3, column = 1)

mf3_lbl = Label(first, text = "두번째 원소의 기호")
mf3_lbl.grid(row = 4, column = 0)
mf3 = Entry(first, width = 10)
mf3.grid (row = 4, column = 1)

mf4_lbl = Label(first, text = "두번째 원소의 원자개수")
mf4_lbl.grid(row = 5, column = 0)
mf4 = Entry(first, width = 10)
mf4.grid (row = 5, column = 1)


lunch_cal = Button(first, text = "확인", width = 15, command = cal)
lunch_cal.grid (row = 6, column = 1)

made_hanbaek = Frame(root)
made_hanbaek.grid(row = 1, column = 0, sticky = S)
none_lbl = Label(made_hanbaek, text = "한백 만듦 (화학 세특 산화수 계산기)")
none_lbl.grid(row = 1, column = 0)
none_lbl2 = Label(made_hanbaek, text = "예시 H 2 O 2 차례로 입력시 산화수가 출력됩니다.")
none_lbl2.grid(row = 2, column = 0)
root.mainloop()