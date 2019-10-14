from docopt import docopt
from api import *
from tabulate import tabulate
usage = """
usage:
    spent_app.py --init
    spent_app.py --show [<category>]
    spent_app.py --add <amount> <category> [<message>]
    spent_app.py --delete
"""
args = docopt(usage)
if args['--init']:
    init()
    print('your table successfully created')
if args['--show']:
    category = args["<category>"]
    amount , result = show(category)
    print('total expense :' , amount)
    print(tabulate(result))

if args['--add']:
    try:
        amount = float(args['<amount>'])
        add(amount , args['<category>'] , args["<message>"])
        print("item added")
    except:
        print(usage)
if args['--delete']:
    delete()
    print('deleted table')



