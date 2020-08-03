[comment]: # (Hi trustee. It is best to view this file in a markdown preview.)

# Generate the contributions-to-date report
You can use the qb-to-xl-arranged.py script to generate a nicely formatted spreadsheet for member contributions.

The output will be in a CSV file, which you can open in XL and save as PDF (using the print menu to save as PDF is better BTW)

## Lets get on with it. How do I do it?
1. In QuickBooks go to _Reports_. Then click on _Custom reports_. Find the report called **Member contributions report** (saved under Custom reports). Adjust the report period if you wish. Then click _Run report_

1. Download the report and convert to .CSV (e.g. use Google Spreadsheets to convert to .csv, or Excel). At this point the file should look like:

    ```cs
    St. Gregoriose Orthodox Church of India,,,,
    Sales by  Customer Detail,,,,
    "January 1 - August 2, 2020",,,,
    ,,,,
    ,Date,Account,Amount,Ref #
    Fake Person1,,,,
    ,05/22/2020,Membership & Subscription:Membership/Subscrptn -This Year,600.00  ,9RX92343430450240
    Total for Fake Person1,,,$600.00  ,
    Second Faker,,,,
    ,08/01/2020,Lunch Fund Collections,250.00  ,72S9323432445251M
    ,08/01/2020,Membership & Subscription:Membership/Subscrptn -This Year,"1,200.00  ",72S933632445251M
    Total for Second Faker,,,"$1,450.00  ",
    Third Guy / And Spouse,,,,
    ,02/03/2020,Membership & Subscription:Prev Year Subscription Arrears,270.00  ,5250
    ,02/03/2020,Membership & Subscription:Membership/Subscrptn -This Year,730.00  ,5250
    Total for Third Guy / And Spouse,,,"$1,000.00  ",
    Next Person,,,,
    ,01/13/2020,Special Services Income:Anniversary Offering,25.00  ,CASH
    ,02/29/2020,Special Services Income:Birthday Offering,20.00  ,
    Total for Next Person,,,$45.00  ,

    ...
    ```

1. Rename the csv to contributions.csv

1. Run the qb-to-xl-arranged.py script over the CSV file like this:
    ```bash
    python qb-to-xl-arranged.py < contributions.csv
    ```

    This will create a csv file called "notice_board.csv" with everyone's contributions. 
    The rows will be sorted by the Member Name. The columns will be arranged in alphabetic order. 
    Empty cells will be blank. "Multiple Members" and "Not Specified" will be removed.

1. Open this CSV in Excel. Freeze the first row and column if you like to review. (Place the cursor in cell B2 and View/Freeze Panes)

1. Adjust the columm widths. Bold what you like, and print to PDF. 
I say print because that lets you organize the layout better than "Save as PDF"

