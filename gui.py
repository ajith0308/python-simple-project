#App for nutrition values


from tkinter import *
from tkinter import messagebox
import functions
#new add
from functools import partial
import mysql.connector
from threading import*

class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("App calculating nutrition values")
        self.switch(Menu)
        self.geometry('350x350')
        self.config(bg = "black")

    def switch(self, frame_class):
        """Destroys current frame and replaces it with a chosen by the user"""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Menu(Frame):
    """Main menu"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        """Frame widgets"""
        label = Label(self, text = "Project Notes Presents Nutrition Calculator!\n Choose an option."\
                      , bg = "black", fg = "white")
        label.pack()
        button = Button(self, text = "Calculator", width = 20, command = lambda: master.switch(Calculator))
        button.pack(padx = 10, pady = 10)
        button2 = Button(self, text = "Add a product", width = 20, command = lambda: master.switch(File_Write))
        button2.pack()
        button3 = Button(self, text = "Exit", width = 20, command = self.close)
        button3.pack(padx = 10, pady = 10)

    def close(self):
        """Close the app"""
        self.destroy()
        exit()


class Calculator(Frame):
    """Writing nutritional values of the user defined food"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")
        def db(s):
            try:
                mydb = mysql.connector.connect(host="localhost",user="admin",password="",db="food")
                print(mydb)
                mys = mydb.cursor()
                print(mys)
                search = "SELECT * FROM food_team WHERE food_it="
                new = str(s)
                new1: str = "'"
                new2: str = "'"
                request: str = new1 + new + new2
                qry = search +request
                print(qry)
                mys.execute(qry)
                result = mys.fetchall()
                
              
                return result
            except:
                print("error")
                return 0
            


        def click(food,qat):
            output.delete(0.0, END)
            s = food.get()
            x = qat.get()
            print(type(qat))
            #am=int(x)
            kcalValue,total=0,0
            proteinValue,pro=0,0
            carbValue,crobo=0,0
            fatValue,fat=0,0
            
            print("food=",s)
            print("quantity",x)
            z=db(s)
            print(z)
            #destory the inner frame
            #self.frame1.destroy()


            #root.destroy()
            if(len(z)==0):
                outcome="Sorry, but we don't have this product in our database: %s, but you can add it! :)"% (s)
                output.insert(END,outcome)
            else:
                for row in z:
                    #print("Name",row[1]
                    total=row[1]
                    pro=row[2]
                    crobo=row[3]
                    fat=row[4]
                kcalValue += x / 100 * total
                proteinValue += x / 100 *pro
                carbValue += x/ 100 *crobo
                fatValue += x/ 100 *fat
                outcome = "Your product provided you with %d kcal, "\
                "%d protein, %d carbs oraz %d fat."\
                % (kcalValue, proteinValue, carbValue, fatValue)
                output.insert(END,outcome)

                
                #self.frame1.destroy()
                #newfram()



        """Frame widgets"""
        food = StringVar()
        qat = IntVar()
        
        label = Label(self, text ="Enter a product that you ate.", bg = "black", fg = "white")
        label.pack()
        # user input, product
        label2 = Label(self, text = "Name: ", bg = "black", fg = "white")
        label2.pack()
        #ip
        entryProduct = Entry(self, width = 20,textvariable=food ,bg = "white")
        entryProduct.pack()
        # user input, amount
        label3 = Label(self, text = "Amount: " ,bg = "black", fg = "white")
        label3.pack()
        #ip
        entryGram = Entry(self, width = 20,textvariable=qat, bg = "white")
        entryGram.pack()
        # submit
        clk = partial(click,food,qat)
       
        go=Button(self, text = "Submit", width = 8, command =clk).pack(padx = 10, pady = 10)
      
        # output
        label4 = Label(self, text = "These are the nutrinion values:", bg = "black", fg = "white")
        label4.pack()
        output = Text(self, width = 20, height = 6, wrap = WORD, bg = "white")
        output.pack()
        #going back to menu
        self.button = Button(self, text = "Back", width = 8, command = lambda: master.switch(Menu))
        self.button.pack(padx = 10, pady = 10)


class File_Write(Frame):
    """User can add new new products and their values"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        
        def db(name, kcal, protein, carb, fat):
            nameEntry.delete(0, END)
            kcalEntry.delete(0, END)
            proteinEntry.delete(0, END)
            carbEntry.delete(0, END)
            fatEntry.delete(0, END)
            try:
               mydb = mysql.connector.connect(
                   host="localhost",
                   user="admin",
                   password="",
                   db="food")
              
               try:
                   mycursor = mydb.cursor()
                   sql ="INSERT INTO food_team(food_it,klr,pro,co,fat) VALUES(%s,%s,%s,%s,%s)"
                   VAL =(name,kcal,protein,carb,fat)
                   mycursor.execute(sql,VAL)
                   mydb.commit()
                   
                   return 1
               except:
                    return 0
            except:
                 print("db error")
                 return -1
                
              
                
        def update():
            error = False
            # checking if kcal, protein, carb and fat are integers and productName is a string
            try:
                name = int(nameEntry.get())
                error = True
            except:
                 name = nameEntry.get()
            try:
                kcal = int(kcalEntry.get())
                protein = int(proteinEntry.get())
                carb = int(carbEntry.get())
                fat = int(fatEntry.get())
            except:
                error = True
            if error == True:
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                #writing to a file
                x=db(name, kcal, protein, carb, fat)
                if(x==0):
                    messagebox.showerror("duplicate records", "value already present!")
                elif(x==1):
                     messagebox.showinfo("ok"," insert successfully completed")
                else:
                     messagebox.showerror("Error", "database is not connected ")

        def validate():
            """Checks is the user inputs correct data"""
            def write(name, kcal, protein, carb, fat):
                """Writes to file"""
                file = open("Products.txt", "a")
                productValue = "%s,%s:%s:%s:%s" % (name, kcal, protein, carb, fat)
                file.write("\n" + productValue)
                file.close()
                #Emptying inputs
                nameEntry.delete(0, END)
                kcalEntry.delete(0, END)
                proteinEntry.delete(0, END)
                carbEntry.delete(0, END)
                fatEntry.delete(0, END)

            error = False
            # checking if kcal, protein, carb and fat are integers and productName is a string
            try:
                name = int(nameEntry.get())
                error = True
            except:
                 name = nameEntry.get()
            try:
                kcal = int(kcalEntry.get())
                protein = int(proteinEntry.get())
                carb = int(carbEntry.get())
                fat = int(fatEntry.get())
            except:
                error = True
            if error == True:
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                #writing to a file
                write(name, kcal, protein, carb, fat)

        """Frame widgets"""
        label = Label(self, text ="Enter the product name and its nutritional "\
                "values per 100 gram", bg = "black", fg = "white")
        label.pack()
        label1 = Label(self, text = "Name:", bg = "black", fg = "white")
        label1.pack()
        nameEntry = Entry(self, width = 20, bg = "white")
        nameEntry.pack()

        label2 = Label(self, text = "Calories:", bg = "black", fg = "white")
        label2.pack()
        kcalEntry = Entry(self, width = 20, bg = "white")
        kcalEntry.pack()

        label3 = Label(self, text = "Protein:", bg = "black", fg = "white")
        label3.pack()
        proteinEntry = Entry(self, width = 20, bg = "white")
        proteinEntry.pack()

        label4 = Label(self, text = "Carbs:", bg = "black", fg = "white")
        label4.pack()
        carbEntry = Entry(self, width = 20, bg = "white")
        carbEntry.pack()

        label5 = Label(self, text = "Fat:", bg = "black", fg = "white")
        label5.pack()
        fatEntry = Entry(self, width = 20, bg = "white")
        fatEntry.pack()

        submit = Button(self, text = "Submit", width = 8, command =update)
        submit.pack(padx = 10, pady = 10)

        button3 = Button(self, text = "Back", width = 20, command = lambda: master.switch(Menu))
        button3.pack(padx = 10, pady = 10)


if __name__ == "__main__":
    app = App()
    app.mainloop()

