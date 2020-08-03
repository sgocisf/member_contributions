import csv
import sys
import pandas

headings = {
    "Anniversary Offering (Anniversary Offering)" : "Anniv.",
    "Special Services Income:Anniversary Offering" : "Anniv.",
    "Auction Receipts (Receipts for Auctions held)": "Auction",
    "Harvest / Auction Receipts": "Auction",
    "Baptism": "Special services",
    "Special Services Income": "Special services",
    "Special Services Income:Special Prayers & Ceremonies": "Special services",
    "Birthday Offering (Birthday Offering)": "Birthday",
    "Special Services Income:Birthday Offering": "Birthday",
    "Building Fund (Building Fund)" : "Building Fund",
    "Building Fund" : "Building Fund",
    "Camping Collections (Camping Income (Collections used to offset camping expenses))": "Camping/Picnic",
    "Catholicate Day - Collections (Catholicate Day Collections)": "Catholicate",
    "Catholicate Day Collections": "Catholicate",
    "Charity Collections": "Charity",
    "Charity Collections:Charity Fund Contributions": "Charity",
    "Christmas Carol Collections": "Christmas",
    "Church Furnishings - Building &": "Misc",
    "Building & Property Maintenance:Church Furnishings": "Misc",
    "Diocese Day - Collections (iocese Day Collections)": "Diocesan/Seminary",
    "Diocesan Day Collections": "Diocesan/Seminary",
    "Lunch Fund Collections (Lunch Fund Collections)": "Lunch Fund",
    "Lunch Fund Collections": "Lunch Fund",
    "MGOCSM Collections (Contribution to MGOCSM)": "Misc",
    "MGOCSM Collections": "Misc",
    "MM Samajam Collections (Contribution to MM Samajam)": "Misc",
    "MM Samajam Collections": "Misc",
    "Marriage": "Special services",
    "Membership & Subscription (Current Year Subscription)": "Membership",
    "Membership & Subscription:Membership/Subscrptn -This Year": "Membership",
    "Future Year Membership": "Membership",
    "Miscellaneous Receipts (Miscellaneous Receipts)": "Misc",
    "Miscellaneous Receipts:Calendar Sales": "Misc",
    "Miscellaneous Receipts:Hall Rental": "Misc",
    "Miscellaneous Receipts:Other Income (Income not related directy to church operations)": "Misc",
    "Miscellaneous Receipts:Qurbana Book Sale (New Qurbana Book Sale)": "Misc",
    "Other Income": "Misc",
    "Miscellaneous Receipts": "Misc",
    "Musical Night Collections": "Misc",
    "A/V Upgrade Project Income": "Misc",
    "Offertory Collections - Other (Other Offertory collections)": "Misc",
    "Offertory Collections:Offertory on Non-Sundays": "Misc",
    "OVBS Collections": "Sunday school/OVBS",
    "Parumala Thirumeni Deposit Box (Parumala Thirumeni Offertory Box)": "Charity",
    "Charity Collections:Parumala Thirumeni Offertory": "Charity",
    "Passion Week (Passion Week donations)": "Passion week",
    "Passion Week Expenses": "Passion week",
    "Passion Week Collections (Passion Week collections)": "Passion week",
    "Offertory Collections:Passion Week Collections": "Passion week",
    "Fellowship Activity Income:Picnic Collections": "Camping/Picnic",
    "Prev Year Subscription (Previous Year's subscription arrears)": "Misc",
    "Membership & Subscription:Prev Year Subscription Arrears": "Misc",
    "Seminary Day Collections (Seminary Day Collections)": "Diocesan/Seminary",
    "Seminary Day Collections": "Diocesan/Seminary",
    "St Mary Deposit Box": "Charity",
    "Charity Collections:St Mary Offertory": "Charity",
    "Sunday Offertory (Sunday Offertory)": "Misc",
    "Offertory Collections:Sunday Offertory": "Misc",
    "Sunday School Collections": "Sunday School/OVBS",
    "Total": "Total",
    "Fellowship Activity Income:Talent Show Income": "Misc",
    "Bank of the West:General Fund": "Misc",
    "Perunnal Expenses": "Misc",
    "Bank Charges": "Misc",
    "Family Conference Income": "Misc",
    "Fellowship Activity Income:Musical Nite Donations": "Misc",
    "Christmas Carol Expenses": "Misc"
 }   

r = csv.reader(sys.stdin, delimiter=',')
name = ''
contribs = dict()
h = set()
n = set()
# Skip the first 5 lines
for _ in range(5):
    next(r)

for row in r:
    if name == '':
        name = row[0]
        contribs[name] = dict()
        n.update(name)
    if row[0].startswith('Total '):
        h.add("Name")
        h.add("Total")
        contribs[name]["Name"] = name
        contribs[name]["Total"] = row[3]
        name = ''
        
    if row[0] == '' and row[2] != "":
        t = headings[row[2]]
        h.add(t)
        if not t in contribs[name]:
            contribs[name][t] = 0
        contribs[name][t] = contribs[name][t] + float(row[3].replace(',',''))

df = pandas.DataFrame.from_dict(contribs, orient='index').reset_index() # read dictionary into a pandas dataframe
df = df.sort_index(axis=1) # sort horizontally by column name (axis = 1)
df.fillna('', inplace=True) # replace NaN with nothing
df = df.set_index('Name').reset_index() # Move Name column to the front
del df['index'] # we dont need this field anymore
df = df.sort_values(by=['Name'])
df = df[df.Name != 'Multiple Members/Individuals'] # remove the row with this name
df = df[df.Name != 'Not Specified'] # remove the row with this name
df.to_csv('notice_board.csv', index=False) # the index column was getting jumbled
