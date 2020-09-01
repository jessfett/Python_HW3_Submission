#import dependences
import os
import csv



# csv file path
budget_path = os.path.join('Resources', 'budget_data.csv')
 
    
    
#establish variables needed
monthcount = 0
total = 0
current_month = 0
last_month = 0
revenue_change = 0

#create lists for changes
revenue_list = []
months = []    
    
    
    
#open file
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
   
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    


    # gather monthly changes in revenue
    for row in csvreader:
        monthcount = monthcount + 1
        months.append(row[0])
        current_month = int(row[1])
        total = total + current_month
        if monthcount > 1:
            revenue_change = current_month - last_month
            revenue_list.append(revenue_change)
        last_month = current_month

        
        
#ccommands to find changes over months
revenue_sum = sum(revenue_list)
profit_average = revenue_sum / (monthcount-1)
max_revenue_change = max(revenue_list)
min_revenue_change = min(revenue_list)
index_max = revenue_list.index(max_revenue_change)
index_min = revenue_list.index(min_revenue_change)
month_max = months[index_max+1]
month_min = months[index_min+1]


#create variables with clean outputs with commas and rounding
rounded_profit_average=round(profit_average,2)
comma_total='{:,}'.format(total)
comma_max_month='{:,}'.format(max_revenue_change)
comma_min_month='{:,}'.format(min_revenue_change)
comma_average_change='{:,}'.format(rounded_profit_average)


# print summary to console
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {monthcount}")
print(f"Total: ${comma_total}")
print(f"Average Change: ${comma_average_change}")
print(f"Greatest Increase in Profit: {month_max} (${comma_max_month})")
print(f"Greatest Decrease in Profit: {month_min} (${comma_min_month})")



#output summary
output_summary=("Financial Analysis"
"----------------------------------------"
f"Total Months: {monthcount}\n"
f"Total: ${comma_total}\n"
f"Average Change: ${comma_average_change}\n"
f"Greatest Increase in Profit: {month_max} (${comma_max_month})\n"
f"Greatest Decrease in Profit: {month_min} (${comma_min_month})\n")



#Write to Text File
output_file="budget_data_output.txt"

with open(output_file, "w") as txt_file:
    txt_file.write(output_summary)