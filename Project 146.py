from tkinter import *

root=Tk()
root.title("Fibonacci")
root.geometry("400x400")

enter=Entry(root)
label_series=Label(root)
label_sum=Label(root)

def fibonacci():
    input=enter.get()
    sum=1
    first_num=0
    second_num=1
    sum2=0
    while(input != ""):
        label_series["text"] +=str(sum) + " "
        label_sum["text"] = "Fibonacci Sum : " + str(sum2)
        first_num=second_num
        second_num=sum
        sum=first_num + second_num
        sum2=sum2+sum
button = Button(root, text="Show Fibonacci", command=fibonacci)
        
    

button.pack()
label_series.pack()
label_sum.pack()
enter.pack()
root.mainloop()
