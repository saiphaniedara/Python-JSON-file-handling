import matplotlib.pyplot as mpl
pieces_con_week=[0,5,10,15,20,25,30,35,40,45]
no_of_cust=[40,30,50,50,60,30,30,10,30,10]
mpl.bar(pieces_con_week,no_of_cust,label='Customers',width=4.8)
mpl.legend()
mpl.xlabel('Pieces of candy consumed in a week')
mpl.ylabel('Number of customers')
mpl.title('Distribution of Weekly Candy Consumption')
mpl.show()
