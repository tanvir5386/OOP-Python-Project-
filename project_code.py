class Star_cinema:
    def __init__(self) -> None:
        self._hall_list=[]   
    
    def entry_hall(self,hall):
        self._hall_list.append(hall)

class Hall(Star_cinema):
    def __init__(self,rows,cols,hall_no):
        self._seats={}
        self._show_list=[]
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no
        self._show_num=[]
        
    def entry_show(self,id,movie_name,time):
        self._show_num.append(id)
        info=(id,movie_name,time)
        self._show_list.append(info)
        blocks=[]
        for i in range(self._rows):
            col=[]
            for j in range (self._cols):
                col.append('0')
            blocks.append(col)
        self._seats[self._hall_no]=blocks

    def book_seats(self,show_id,seat_list):
        if(show_id not in self._show_num):
            print('NO SHOW FOUND WITH THIS ID!')
            print('Please check again!')
            return
        valid_seat=self._seats.get(self._hall_no)
        if valid_seat==None:
            print('Error while finding seats! We are unable to fetch this information')
            return
             
        for i in seat_list:
            row,col=i
            if not(0 <= i[0] < self._rows and 0 <= i[1] < self._cols):
                print('This is not a valid seat number. Please read the guidelines.')
                continue
            if valid_seat[row][col]=='1':
                print(f"Seat ({i[0]}, {i[1]}) is already booked.")
                print('To see the available seats. Please go to "View Available Seats"')
            else:
                valid_seat[row][col]='1'
                print(f"Seat ({i[0]}, {i[1]}) booked successfully")

    def view_show_list(self):
        print("Show Schedule: ")
        for item in self._show_list:
            print(f"Show ID: {item[0]} , Show Name: {item[1]}, Time: {item[2]}" )
       
    def available_seats(self,show_id):
        valid_seat=self._seats.get(self._hall_no)
        if valid_seat==None:
            print('Error while fetching this information')
            return
        print("The list of the available seats: ")
        for i in range(self._rows):
            for j in range(self._cols):
                if(valid_seat[i][j]=='0'):
                    print(f"Row no: {i}, Column no: {j}")

cinema=Star_cinema()
cinema.entry_hall('Jamuna')
cinema.entry_hall('Meghna')

jamuna=Hall(10,7,1)
jamuna.entry_show('101','Dunki','10:00 am')
jamuna.entry_show('102','Pathan','2:00 pm')

meghna=Hall(15,10,2)
meghna.entry_show('201','Anabelle',"7:00 pm")
meghna.entry_show('202','The Nun',"10:00 pm")

while True:
    print("Here are the available features: ")
    print("1. Show all the available halls ")
    print("2. Choose a Hall ")
    print("Enter 0 to exit")
    print("Please make your choice")
    
    n=int(input()) 

    if(n==1):
        print("The available halls are : ", cinema._hall_list)
        print("For Further inquiry, run the program again and choose option 2")

    elif(n==2):
        print("For Jamuna, PRESS 1")
        print("For Meghna, PRESS 2")
        
        t=int(input())
        
        if(t==1):
            print("You have chosen Jamuna.")
            print("Press 3 for the schedule of shows")
            print("Press 4 for the available seats")
            print("Press 5 for booking seats")
            
            p=int(input())
            
            if(p==3):
                jamuna.view_show_list()
                print("Enter 6 to see the available seats")
                print("Enter 7 to book seat")
                print("To exit enter 0")
                
            if(p==4):
                jamuna.view_show_list()
                print("Enter the Show ID for checking available seats: ")
                sh_num=input()
                jamuna.available_seats(sh_num)
                print("Enter 8 to book seat")
                print("To exit enter 0")

            if(p==5):
                jamuna.view_show_list()
                print("Enter the Show ID")
                sh_num=input()
                print("Enter the number of seats you want to book")
                li = []
                n = int(input())
                print("CAUTION: Row ranges from 0 to 9 and Column ranges from 0 to 6")
                for i in range(n):
                    x, y = map(int, input().split())
                    li.append((x, y))
                jamuna.book_seats(sh_num,li)   

        if(t==2):
            print("You have chosen Meghna.")
            print("Press 3 for the schedule of shows")
            print("Press 4 for the available seats")
            print("Press 5 for booking seats")
            p=int(input())
            
            if(p==3):
                meghna.view_show_list()
                print("Enter 6 to see the available seats")
                print("Enter 7 to book seat")
                print("To exit enter 0")

            if(p==4):
                meghna.view_show_list()
                print("Enter the Show ID for checking available seats: ")
                sh_num=input()
                meghna.available_seats(sh_num)
                print("Enter 8 to book seat")
                print("To exit enter 0")
                
            if(p==5):
                meghna.view_show_list()
                print("Enter the Show ID")
                sh_num=input()
                print("Enter the number of seats you want to book")
                li = []
                n = int(input())
                print("CAUTION: Row ranges from 0 to 14 and Column ranges from 0 to 9")
                for i in range(n):
                    x, y = map(int, input().split())
                    li.append((x, y))
                meghna.book_seats(sh_num,li)

    elif n == 0:
        break
