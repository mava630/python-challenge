import csv, os

file = os.path.join('Resources','budget_data.csv')

with open(file) as readfile:
    csvfile = csv.DictReader(readfile)

    months = 0
    total = 0
    change = 0
    prev_rev = 0
    total_change = 0
    inc = ['',0]
    dec = ['',0]

    for row in csvfile:
        months += 1
        revenue =float(row['Profit/Losses'])
        total += revenue
        change = revenue - prev_rev
        if prev_rev == 0:
            change = 0
        total_change += change
        prev_rev = revenue

        #Greatst increase
        if change > float(inc[1]):
            inc[0] = row['Date']
            inc[1] = change

        #Greatst decrease
        if change < float(dec[1]):
            dec[0] = row['Date']
            dec[1] = change


    total_change = total_change/(months - 1)

    print('\n\nFinancial Analysis')
    print('----------------------------')
    print("Months: " + str(months))
    print('Total: $' + str(total))
    print('Average  Change: $' + str(round(total_change,2)))
    print('Greatest Increase in Profits: ' + str(inc[0]) + ' ($' + str(inc[1]) + ')')
    print('Greatest Decrease in Profits: ' + str(dec[0]) + ' ($' + str(dec[1]) + ')')


#    output = f'\n\nFinancial Analysis\n----------------------------\nMonths:  str(months\nTotal: $ str(total\nAverage  Change: $ str(round(total_change,2)\nGreatest Increase in Profits:  str(inc[0]  ($ str(inc[1])\nGreatest Decrease in Profits:  str(dec[0] ($ str(dec[1]'

#     print(output)