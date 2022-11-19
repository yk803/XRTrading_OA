import argparse

def read_team(teammap):
    with open(teammap) as f:
        # Read and discard the header line
        _ = f.readline()
        output = {}
        # Read and store the data line by line
        for line in f.readlines():
            team_id, name = line.split(',')
            output[int(team_id)] = name.strip()
        f.close()
    return output

def read_product(product):
    with open(product) as f:
        output = {}
        # Read and store the data line by line
        for line in f.readlines():
            p_id, name, price, lotsize = line.split(',')
            output[int(p_id)] = {'name':name,'price':float(price),'lotsize':int(lotsize)}
        f.close()
    return output

def read_sales(sales):
    with open(sales) as f:
        output = {}
        # Read and store the data line by line
        for line in f.readlines():
            s_id, p_id, t_id, quantity, discount = line.split(',')
            output[int(s_id)] = {'p_id':int(p_id),'t_id':int(t_id),'quantity':int(quantity),'discount':float(discount)}
        f.close()
    return output

def t_report(teams,products,sales,report_fname):
    # Record sales data row by row
    revenues = [0]*len(teams) # no need to store in map anymore since we will not to use but just to export it
    for record in sales.values():
        prod, team, quan = record['p_id'], record['t_id'], record['quantity']
        # (team-1) as index since Python index starts with 0
        revenues[team-1] += products[prod]['price'] * products[prod]['lotsize'] * quan

    # Sort the data by gross revenue in descending order
    tnames = [name for name in teams.values()] # list comprehension faster than zip
    sorted_revenues = sorted(zip(tnames,revenues), key=lambda r: r[1], reverse=True) 

    # Write the file
    with open(report_fname,'w') as f:
        f.write('Team,GrossRevenue\n')
        for name,revenue in sorted_revenues:
            f.write('{},{:.2f}'.format(name,revenue))
            f.write('\n')
        f.close()
    return sorted_revenues

def p_report(teams,products,sales,report_fname):
    # Record sales and other data row by row
    revenues = [0]*len(products) # no need to store in map anymore since we will not to use but just to export it
    units = [0]*len(products)
    discounts = [0]*len(products)
    for record in sales.values():
        prod, team, quan = record['p_id'], record['t_id'], record['quantity']
        num_unit = products[prod]['lotsize'] * quan
        # (prod-1) as index since Python index starts with 0
        units[prod-1] += num_unit
        rev = products[prod]['price'] * num_unit
        revenues[prod-1] += rev
        discounts[prod-1] += rev * record['discount']/100
    
    # Sort the data by gross revenue in descending order
    pnames = [prod['name'] for prod in products.values()] # list comprehension faster than zip
    sorted_revenues = sorted(zip(pnames,revenues,units,discounts), key=lambda r: r[1], reverse=True) 

    # Write the file
    with open(report_fname,'w') as f:
        f.write('Name,GrossRevenue,TotalUnits,DiscountCost\n')
        for name,revenue,unit,discount in sorted_revenues:
            # What's slightly different here from the challenge handbook:
            # round all floats to 2 decimal places to match the previous results' format
            f.write('{},{:.2f},{},{:.2f}'.format(name,revenue,unit,discount))
            f.write('\n')
        f.close()
    return sorted_revenues

def print_fname_error(fname):
    print('Fail to produce the report. {} is not a valid file name!'.format(fname))



def main():
    try:
        teammap = read_team(args.t)
    except IOError:
        print_fname_error(args.t); return
    try:
        product = read_product(args.p)
    except IOError:
        print_fname_error(args.p); return
    try:
        sales = read_sales(args.s)
        treport = t_report(teammap,product,sales,args.team_report)
        preport = p_report(teammap,product,sales,args.product_report)
        print('Data produced successfully!')
    except IOError:
        print_fname_error(args.s); return
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t",
                        type=str,
                        default = "TeamMap.csv",
                        help = "csv file where Team Map is stored",
                        )
    parser.add_argument("-p",
                        type=str,
                        default = "ProductMaster.csv",
                        help = "csv file where product information is stored",
                        )
    parser.add_argument("-s",
                        type=str,
                        default = "Sales.csv",
                        help = "csv file where sales information is stored",
                        )
    parser.add_argument("--team-report",
                        type=str,
                        default = "TeamReport.csv",
                        help = "csv file where team report data will be stored",
                        )
    parser.add_argument("--product-report",
                        type=str,
                        default = "ProductReport.csv",
                        help = "csv file where product report information will be stored",
                        )


    args = parser.parse_args()
    main()