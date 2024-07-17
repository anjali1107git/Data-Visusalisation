headers = ['StdId','StdName','Age','Hindi','English','Maths','Science','Computer','Total']
print(headers)
# # Define the rows
# rows = [
#     [101,'Anjali' ,15,67,89,80,89,90,415],
#     [102,'Ashi' ,15,67,89,87,19,90,352],
#     [103,'rani' ,15,67,89,82,89,90,418],
#     [104,'bhoomi' ,15,67,79,87,89,90,412],
#     [105,'ram' ,15,67,89,87,80,90,421],
#     [106,'vishwa' ,15,67,89,77,89,90,412],
#     [107,'Ayush' ,15,67,89,87,70,90,401],
#     [108,'meera' ,15,67,89,87,89,91,423],
#     [109,'kirti' ,100,97,99,97,99,90,482]
# ]

# # Create a DataFrame from the lists
# df = pd.DataFrame(rows, columns=headers)

# # Display the DataFrame as a table
# print(df)

rows = [
    [101,'Anjali' ,15,67,89,80,89,90,415],
    [102,'Ashi' ,15,67,89,87,19,90,352],
    [103,'rani' ,15,67,89,82,89,90,418],
    [104,'bhoomi' ,15,67,79,87,89,90,412],
    [105,'ram' ,15,67,89,87,80,90,421],
    [106,'vishwa' ,15,67,89,77,89,90,412],
    [107,'Ayush' ,15,67,49,87,70,90,361],
    [108,'meera' ,15,67,89,87,89,91,423],
    [109,'kirti' ,100,97,99,97,99,90,482]
]
print('Name of student whose marks are greater than 50 in english')
for i in rows:
    if  i[4] > 50:
        print(i[1])
        
print('name and age of top four scorers in maths')
sorted_rows_1 = sorted(rows, key=lambda x: x[5], reverse=True)
for i in sorted_rows_1[:4]:
    print(i[1], i[2])

print('name, id of students who are bottom three scorers')
sorted_rows_2 = sorted(rows, key=lambda x: x[-1])
for i in sorted_rows_2[:3]:
    print(i[1], i[0])