import pandas as pd
import sqlite3
import os

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 1000)

conn = sqlite3.connect('yahooquery_aws/financial_data_yahooquery.db')
duplicates = pd.read_sql("select * from tickers where ticker in ('AC', 'ACA', 'ACC', 'ACR', 'ADOC', 'ADP', 'AFG', 'AGS', 'AI', 'AIR', 'ALT', 'ALTR', 'ALX', 'AM', 'AMG', 'AMSC', 'APAM', 'APM', 'ARCH', 'ARGX', 'ARR', 'ASA', 'ASC', 'ASM', 'ASML', 'ATI', 'ATO', 'AUB', 'AUTO', 'AVT', 'AXS', 'BB', 'BCS', 'BEN', 'BIG', 'BMA', 'BON', 'BORR', 'BRG', 'BUI', 'BUR', 'CAF', 'CAN', 'CARA', 'CAS', 'CCEP', 'CEN', 'CIB', 'CLB', 'CNF', 'CO', 'COOL', 'COUR', 'CPA', 'CRI', 'CRTO', 'CS', 'CTT', 'CYAD', 'DG', 'DNB', 'DSM', 'EC', 'EDF', 'EDI', 'EL', 'EMD', 'ENX', 'EOS', 'EPR', 'EQNR', 'EQS', 'ERF', 'ERYP', 'ES', 'ESI', 'ESP', 'EURN', 'EXN', 'EXR', 'FAST', 'FINM', 'FLNG', 'FLO', 'FLUX', 'FR', 'FREY', 'FRO', 'GAM', 'GBT', 'GDS', 'GEG', 'GEOS', 'GLO', 'GLPG', 'GNE', 'GNFT', 'GOGL', 'GTBP', 'HAL', 'ICAD', 'ICE', 'IDEX', 'IEP', 'IEX', 'ITP', 'IVA', 'KOF', 'LEA', 'LI', 'LIFE', 'LIN', 'LINK', 'MAN', 'MAR', 'MAS', 'MF', 'MMT', 'MRK', 'MRM', 'MT', 'NAPA', 'NEWT', 'NEX', 'NEXT', 'NOC', 'NOM', 'NRC', 'NRG', 'NRO', 'NRP', 'NTG', 'NVG', 'NYXH', 'OR', 'ORA', 'ORN', 'PAR', 'PAY', 'PBH', 'PEN', 'PEP', 'PHR', 'PPG', 'PVL', 'RAM', 'RAND', 'RE', 'REAL', 'REI', 'RF', 'ROCK', 'SALM', 'SAN', 'SATS', 'SAVE', 'SBT', 'SEM', 'SII', 'SLB', 'SMAR', 'SNOW', 'SO', 'SOI', 'SON', 'SOR', 'STLA', 'STM', 'STRO', 'SU', 'TECH', 'TEL', 'TGS', 'TNET', 'TRI', 'TTE', 'VAC', 'VEON', 'VGM', 'VIV', 'VTR', 'WAVE', 'ZEN', 'ACAN', 'AKOM', 'ARTE', 'AURA', 'AVTX', 'GET', 'GIGA', 'KEYW', 'MDXH', 'ML', 'MNTR', 'NN', 'NSI', 'ALPAU', 'ALVU') order by ticker", conn)
eurostocks = pd.read_csv(os.getcwd() + '/tickers/eurostocks.csv')

duplicate_names = set(duplicates['name'])
eurostock_names = set(eurostocks['name'])
duplicates.inter