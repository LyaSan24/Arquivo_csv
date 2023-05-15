import csv

import pandas as pd

with open('advertising.csv', mode= 'r') as arquivo_csv:

    leitor_csv = csv.reader(arquivo_csv)

    for linha in leitor_csv:

        print(linha)



