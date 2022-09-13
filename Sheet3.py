# import matplotlib.pyplot as plt
# # x axis values 
# x = [1,2,3]
# # corresponding y axis values 
# y = [2,4,1] 
# plt.plot(x, y) 
# # naming the x axis 
# plt.xlabel('x - axis') 
# # naming the y axis 
# plt.ylabel('y - axis') 
# # giving a title to my graph 
# plt.title('My first graph!') 
# # function to show the plot 
# plt.show()

# import matplotlib.pyplot as plt 
# # line 1 points 
# x1 = [1,2,3] 
# y1 = [2,4,1] 
# # plotting the line 1 points 
# plt.plot(x1, y1, label = "line 1") 
# # line 2 points 
# x2 = [1,2,3]
# y2 = [4,1,3] 
# # plotting the line 2 points 
# plt.plot(x2, y2, label = "line 2") 
# # naming the x axis 
# plt.xlabel('x - axis') 
# # naming the y axis 
# plt.ylabel('y - axis') 
# # giving a title to my graph 
# plt.title('Two lines on same graph!') 
# # show a legend on the plot 
# plt.legend() 
# # function to show the plot 
# plt.show()


# import matplotlib.pyplot as plt 
# # frequencies 
# ages = [2,5,70,40,30,45,50,45,43,40,44, 60,7,13,57,18,90,77,32,21,20,40] 
# # setting the ranges and no. of intervals 
# range = (0, 100) 
# bins = 10 
# # plotting a histogram 
# plt.hist(ages, bins, range, color = 'green', histtype = 'bar', rwidth = 0.8) 
# # x-axis label 
# plt.xlabel('age') 
# # frequency label 
# plt.ylabel('No. of people') 
# # plot title 
# plt.title('My histogram') 
# # function to show the plot
# plt.show()



# import matplotlib.pyplot as plt
# # defining labels
# activities= ['eat', 'sleep', 'work', 'play']
# # # portion covered by each label
# slices= [3, 7, 8, 6]# color for each label
# colors= ['r', 'y', 'g', 'b']# plotting the pie chart
# plt.pie(slices, labels= activities, colors=colors,startangle=90, shadow= True, explode= (0, 0, 0.1, 0),radius= 1.2, autopct= '%1.1f%%')
# # plotting legend
# plt.legend()# showing the plot
# plt.show()


import pandas as pd
nba = pd.read_csv("dataset.csv")
print(type(nba))
print(len(nba))
print(nba.shape)
print(nba.head(5))
print(nba.tail(3))
print(nba.info())
print(nba.describe())
print(nba["team_id"].value_counts())
print(nba["fran_id"].value_counts())
print(nba.isna().sum())

print("There are {} duplicated rows".format(nba.duplicated().sum()))