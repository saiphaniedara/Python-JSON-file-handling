import matplotlib.pyplot as mpl
x=[q for q in range(1,21)]
yi=[5,7,6,7,4,2,7,9,0,5,4,1,6,7,12,4,8,3,7,15]
ya=[4,6,2,3,1,6,8,2,9,7,13,5,8,11,4,0,5,7,9,12]
mpl.plot(x,yi,color='c',label='India')
mpl.plot(x,ya,color='r',label='Afghanistan')
mpl.xlabel('Over',color='b')
mpl.ylabel('Runs per over',color='b')
mpl.legend()
mpl.show()
