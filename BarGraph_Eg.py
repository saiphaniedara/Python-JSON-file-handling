import matplotlib.pyplot as mpl
products=['Ketchup','Peanut Butter','Chocolate Bar','Ice Cream','Chocolate Cake','Soda','Crackers']
per_of_sug=[8.8,9.2,33.2,21.4,30.3,28.9,11.8]
mpl.bar(products,per_of_sug,label='Foods')
mpl.legend() 
mpl.xlabel('Products',color='m')
mpl.ylabel('Percentage of Sugar',color='m')
mpl.title('Amount of Sugar in Certain foods')
mpl.show()
