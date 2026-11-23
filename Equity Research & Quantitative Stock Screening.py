import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# j'ai préféré transormer le fichier excel en dictionnaire python pour éviter les erreurs lors de la références du fichier .xlsx
# pour cela j'ai exécuté le code suivant sur python :
# import pandas as pd
# data= pd.read_excel("universe of stock 261113.xlsx")
# data = data.to_dict(orient="list")
# notez que j'ai mis le symbole boursier en première colonne pour que ce soit plus lisible et maniable
data = {
    'Ticker': ['BESI', 'STMPA', 'VU', 'DTE', 'KPN', 'PUB', 'ASM', 'ASML', 'CAP', 'DSY', 'IDR', 'IFX', 'NEM', 'NOKIA', 'SAP', 'AUTO', 'HTO', 'INF', 'VEND', 'VOD', 'IFCN', 'LOGN', 'SGE', 'SOI', 'SOP', 'STMMI', 'TPRO', 'TEMN', 'FOX', 'RDDT', 'TLS', 'VZ', 'DIS', 'ADBE', 'AMAT', 'ANET', 'ADSK', 'AVGO', 'CSCO', 'FLEX', 'HUBS', 'IBM', 'INTC', 'MRVL', 'MSFT', 'MDB', 'NVDA', 'OKTA', 'PANW', 'CRM', 'IOT', 'WDC', 'GOOGL', 'T', 'CHTR', 'FOXA', 'NFLX', 'OMC', 'TTWO', 'ADI', 'AAPL', 'ALAB', 'CDNS', 'CHKP', 'NET', 'COHR', 'GLW', 'CRDO', 'CRWD', 'DDOG', 'DELL', 'P', 'FFIV', 'HPE', 'HPQ', 'INTU', 'JBL', 'KEYS', 'KLAC', 'MCHP', 'MSI', 'NTAP', 'NXPI', 'ON', 'ORCL', 'PLTR', 'PTC', 'QCOM', 'SHOP', 'SWKS', 'SNOW', 'SNPS', 'TDY', 'TER', 'TXN', 'TSEM', 'TWLO', 'ZM', 'ZS'],
    'Short Name': ['BE SEMICONDUCTOR', 'STMICROELECTRONI', 'VUSION', 'DEUTSCHE TELEKOM', 'KPN (KONIN) NV', 'PUBLICIS GROUPE', 'ASM INTL NV', 'ASML HOLDING NV', 'CAPGEMINI SE', 'DASSAULT SYSTEME', 'INDRA SISTEMAS', 'INFINEON TECH', 'NEMETSCHEK SE', 'NOKIA OYJ', 'SAP SE', 'AUTOTRADER GROUP', 'HELLENIC TELECOM', 'INFORMA PLC', 'VEND MARKE CL', 'VODAFONE GROUP', 'INFICON-REG', 'LOGITECH INTER-R', 'SAGE GROUP PLC/T', 'SOITEC', 'SOPRA STERIA GRO', 'STMICROELECTRONI', 'TECHNOPROBE SPA', 'TEMENOS AG-REG', 'FOX CORP - B', 'REDDIT INC-A', 'TELSTRA GROUP LT', 'VERIZON COMMUNIC', 'WALT DISNEY CO/T', 'ADOBE INC', 'APPLIED MATERIAL', 'ARISTA NETWORKS', 'AUTODESK INC', 'BROADCOM INC', 'CISCO SYSTEMS', 'FLEX LTD', 'HUBSPOT INC', 'IBM', 'INTEL CORP', 'MARVELL TECHNOLO', 'MICROSOFT CORP', 'MONGODB INC', 'NVIDIA CORP', 'OKTA INC', 'PALO ALTO NETWOR', 'SALESFORCE INC', 'SAMSARA INC-CL A', 'WESTERN DIGITAL', 'ALPHABET INC-A', 'AT&T INC', 'CHARTER COMMUN-A', 'FOX CORP - A', 'NETFLIX INC', 'OMNICOM GROUP', 'TAKE-TWO INTERAC', 'ANALOG DEVICES', 'APPLE INC', 'ASTERA LABS INC', 'CADENCE DESIGN', 'CHECK POINT SOFT', 'CLOUDFLARE INC-A', 'COHERENT CORP', 'CORNING INC', 'CREDO TECHNOLOGY', 'CROWDSTRIKE HO-A', 'DATADOG INC-A', 'DELL TECHN-C', 'EVERPURE INC-A', 'F5 INC', 'HEWLETT PACKA', 'HP INC', 'INTUIT INC', 'JABIL INC', 'KEYSIGHT TEC', 'KLA CORP', 'MICROCHIP TECH', 'MOTOROLA SOLUTIO', 'NETAPP INC', 'NXP SEMICONDUCTO', 'ON SEMICONDUCTOR', 'ORACLE CORP', 'PALANTIR TECHN-A', 'PTC INC', 'QUALCOMM INC', 'SHOPIFY INC - A', 'SKYWORKS SOLUTIO', 'SNOWFLAKE INC', 'SYNOPSYS INC', 'TELEDYNE TECH', 'TERADYNE INC', 'TEXAS INSTRUMENT', 'TOWER SEMICONDCT', 'TWILIO INC - A', 'ZOOM COMMUNICATI', 'ZSCALER INC'],
    'Sector': ['Information Technology', 'Information Technology', 'Information Technology', 'Communication Services', 'Communication Services', 'Communication Services', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Communication Services', 'Communication Services', 'Communication Services', 'Communication Services', 'Communication Services', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Communication Services', 'Communication Services', 'Communication Services', 'Communication Services', 'Communication Services', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Communication Services', 'Communication Services', 'Communication Services', 'Communication Services', 'Communication Services', 'Communication Services', 'Communication Services', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology', 'Information Technology'],
    'Country': ['NETHERLANDS', 'SWITZERLAND', 'FRANCE', 'GERMANY', 'NETHERLANDS', 'FRANCE', 'NETHERLANDS', 'NETHERLANDS', 'FRANCE', 'FRANCE', 'SPAIN', 'GERMANY', 'GERMANY', 'FINLAND', 'GERMANY', 'BRITAIN', 'GREECE', 'BRITAIN', 'NORWAY', 'BRITAIN', 'SWITZERLAND', 'SWITZERLAND', 'BRITAIN', 'FRANCE', 'FRANCE', 'SWITZERLAND', 'ITALY', 'SWITZERLAND', 'UNITED STATES', 'UNITED STATES', 'AUSTRALIA', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'ISRAEL', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'NETHERLANDS', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'CANADA', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES', 'ISRAEL', 'UNITED STATES', 'UNITED STATES', 'UNITED STATES'],
    'Upside': [0.457, 0.508, 0.397, 0.350, 0.061, 0.095, 0.643, 0.565, 0.197, -0.019, 0.211, 0.609, 0.361, 0.423, 0.125, 0.027, 0.111, 0.223, 0.228, 0.057, 0.249, 0.070, 0.021, 0.681, 0.112, 0.448, 0.778, 0.070, 0.348, 0.471, -0.013, 0.084, 0.064, 0.108, 0.601, 0.200, 0.182, 0.498, 0.342, 1.005, 0.047, 0.096, 0.505, 0.972, 0.225, 0.355, 0.711, 0.182, 0.253, 0.318, 0.259, 0.993, 0.292, 0.231, 0.251, 0.216, 0.345, 0.129, 0.247, 0.184, -0.034, 0.558, 0.268, 0.037, 0.091, 0.642, 0.500, 1.054, 0.121, 0.462, 0.642, 0.416, 0.414, 0.478, -0.059, 0.165, 0.679, 0.408, 0.410, 0.423, 0.048, 0.170, 0.146, 0.334, 0.944, 0.328, 0.032, 0.087, 0.181, -0.094, 0.480, 0.298, 0.186, 0.607, 0.102, 0.711, 0.274, 0.213, 0.240],
    'RSI_14D': [47.84, 50.44, 68.69, 54.63, 67.32, 65.02, 46.79, 44.83, 59.24, 64.24, 42.49, 49.57, 39.90, 44.93, 60.63, 66.81, 44.55, 56.74, 58.73, 47.27, 42.63, 53.60, 59.27, 41.91, 74.71, 50.49, 39.47, 64.11, 50.52, 34.34, 67.45, 57.19, 65.57, 42.54, 44.67, 60.43, 59.06, 59.50, 45.21, 41.54, 45.52, 50.50, 33.40, 37.17, 48.44, 46.03, 25.99, 43.31, 38.73, 39.16, 48.51, 41.29, 42.28, 47.86, 63.08, 50.10, 39.72, 61.19, 63.60, 53.31, 59.69, 41.12, 52.59, 54.69, 54.45, 49.20, 43.49, 43.12, 43.76, 31.58, 39.46, 44.27, 25.78, 41.82, 42.28, 54.41, 43.40, 45.31, 47.59, 35.29, 76.97, 42.66, 61.43, 51.53, 48.43, 41.86, 74.63, 52.34, 44.06, 63.97, 44.58, 51.60, 54.14, 40.27, 60.17, 39.93, 38.98, 55.93, 35.99],
    'Perf_1M': [-10.55, -4.27, 20.95, 5.81, 14.01, 4.71, -14.52, -11.16, 6.45, 14.82, -5.08, -10.41, -10.93, -15.12, 8.37, 12.00, -1.15, 0.89, 9.34, -1.53, -17.82, -0.80, 9.00, -28.97, 13.87, -3.04, -29.22, 13.19, 6.78, -35.74, 10.34, 6.78, 9.98, 1.63, -19.18, 0.44, 14.77, -2.56, -14.55, -30.86, -2.80, 6.75, -41.58, -40.57, -3.97, -9.28, -28.36, -19.84, -18.69, -8.45, -0.22, -19.66, -14.49, -2.89, 26.27, 6.99, -9.51, 11.94, 16.31, -2.39, 5.34, -31.30, -1.80, 9.15, -8.53, -22.29, -21.67, -31.49, -12.93, -34.27, -36.94, -30.94, -33.55, -28.76, -5.81, 14.62, -19.31, -18.42, -15.97, -17.27, 18.53, -23.56, 15.89, -5.71, -12.42, -18.53, 1.20, -0.82, -15.37, 15.91, -17.26, -7.32, 6.18, -32.00, 6.63, -23.27, -24.79, -0.77, -15.16],
    'Perf_YTD': [15.36, 87.01, -26.79, -3.94, 11.75, 19.27, 35.63, 45.56, -10.72, 8.56, 20.85, 32.97, -31.52, 32.99, 2.62, -1.98, 11.98, 0.59, -17.21, 17.21, 60.53, 3.61, 9.65, 345.02, 28.01, 89.05, 83.44, 0.25, -8.02, -56.59, 5.13, 14.12, 4.97, -31.39, 46.01, 56.78, -10.66, 0.59, 27.65, 26.88, -46.40, -16.83, 62.76, 87.93, 7.91, -19.35, -12.22, 109.99, 75.26, -17.75, 16.16, 77.56, -3.35, -10.67, -35.31, -8.49, -32.00, 8.81, -9.00, 49.26, 32.24, 34.38, 4.99, -20.60, 61.32, 22.08, 32.88, -5.58, 94.08, 36.95, 186.78, 61.77, 23.98, 104.08, 29.49, -47.84, 12.48, 48.64, 27.25, -3.72, 38.84, 70.59, 20.84, 33.54, -35.65, -4.36, 12.67, 2.55, -3.86, 39.95, 34.94, -2.43, 27.07, 33.61, 76.92, 34.75, 48.90, 12.88, -13.75],
    'FCF_Yld': [2.32, 1.38, -14.46, 23.04, 7.84, 9.10, 2.45, 4.05, 9.43, 5.06, 20.86, 3.16, 5.31, -0.01, 3.66, 6.64, 7.56, 7.36, 1.17, 23.85, 2.14, 6.57, 4.56, 2.21, 12.22, 1.36, 0.46, 5.69, 8.91, 6.28, 7.26, 11.49, 3.99, 10.91, 2.05, 1.93, 5.17, 2.28, 3.41, 2.71, 6.33, 6.37, 1.21, 1.18, 1.54, 2.40, 3.15, 3.05, 1.72, 7.73, 1.06, 3.92, 0.55, 11.67, 24.29, 7.96, 4.32, 16.18, 0.24, 2.47, 2.61, 0.88, 1.95, 7.54, 0.29, -4.09, 2.39, 1.71, 0.66, 1.70, 3.52, 0.35, 4.81, 5.85, 14.50, 9.18, 5.01, 2.82, 1.96, 4.32, 2.88, 4.50, 5.19, 5.57, -7.82, 1.49, 3.80, 4.58, 1.40, 1.71, 1.17, 3.13, 3.76, 2.48, 2.57, -0.15, 3.61, 6.66, 2.53],
    'PE_Nxt_Yr': [23.97, 16.83, 14.63, 10.21, 16.77, 12.18, 20.22, 23.72, 9.43, 17.84, 17.06, 13.52, 22.40, 17.87, 25.23, 13.04, 10.94, 13.46, 22.52, 11.12, 26.06, 16.60, 20.35, 26.65, 10.18, 17.13, 26.20, 19.15, 10.38, 12.30, 22.07, 8.78, 15.75, 8.67, 15.78, 34.42, 18.27, 18.90, 17.38, 10.13, 12.87, 18.51, 34.46, 22.50, 21.80, 43.03, 10.44, 41.89, 66.32, 13.58, 43.77, 7.59, 18.59, 8.54, 2.94, 11.62, 16.54, 7.80, 22.76, 24.28, 34.25, 31.66, 33.81, 13.36, 168.34, 14.60, 26.20, 14.51, 143.04, 57.13, 12.16, 25.97, 15.82, 10.65, 9.09, 12.73, 11.79, 21.83, 21.88, 14.02, 26.99, 16.78, 14.44, 15.50, 11.45, 67.31, 19.72, 15.09, 57.58, 11.88, 99.30, 24.75, 23.35, 21.53, 26.54, 21.81, 30.90, 15.41, 34.45],
    'LTG_EPS': [64.13, 96.55, 12.91, 14.89, 16.65, 8.01, 46.31, 51.79, 7.54, 5.23, 19.99, 44.40, 19.08, 22.39, 11.22, 10.78, 3.51, 8.26, 124.38, 20.55, 21.04, 3.59, 14.56, 54.98, 8.37, 96.55, 102.54, 9.67, 6.99, 55.60, 9.52, 7.61, 12.17, 13.90, 31.24, 36.30, 16.50, 65.86, 14.32, 47.82, 27.65, 5.55, 86.51, 69.67, 17.43, 24.80, 72.04, 11.18, 14.04, 13.94, 31.73, 76.13, 19.44, 11.01, 3.13, 6.99, 22.58, 12.84, 41.49, 37.99, 7.00, 75.76, 18.36, 2.38, 56.26, 52.76, 37.13, 50.00, 31.61, 20.23, 48.49, 43.18, 7.95, 36.00, 2.91, 7.95, 29.25, 30.74, 27.21, 43.73, 12.15, 11.52, 21.43, 38.25, 28.13, 62.53, 8.93, 14.16, 30.80, 19.28, 32.32, 22.70, 10.62, 58.54, 33.37, 72.07, 19.32, 3.85, 20.14],
    'PEG': [0.56, 0.36, 1.36, 0.77, 1.10, 1.66, 0.63, 0.63, 1.38, 3.62, 0.97, 0.41, 1.43, 0.93, 2.66, 1.38, 3.24, 1.98, 0.26, 0.66, 1.63, 4.76, 1.61, 2.08, 1.36, 0.37, 0.42, 2.17, 1.39, 0.27, 2.48, 1.21, 1.40, 0.70, 0.65, 1.31, 1.25, 0.47, 1.33, 0.32, 0.57, 3.56, 0.47, 0.56, 1.50, 2.09, 0.25, 4.15, 5.49, 0.93, 1.69, 0.16, 0.84, 0.84, 1.79, 1.56, 0.77, 0.69, 0.79, 0.84, 5.37, 0.69, 2.16, 6.01, 4.13, 0.43, 0.95, 0.45, 5.79, 3.30, 0.30, 0.91, 2.20, 0.36, 3.06, 1.86, 0.50, 0.86, 1.00, 0.39, 2.43, 1.62, 0.82, 0.59, 0.55, 1.61, 2.45, 1.32, 2.49, 0.81, 4.13, 1.34, 2.39, 0.48, 1.02, 0.53, 1.78, 4.15, 1.96],
    'Rsk_Prem': [24.19, 4.81, 5.89, 6.09, 5.23, 7.21, 23.52, 21.74, 8.41, 6.87, 6.69, 13.66, 10.25, 11.58, 9.48, 5.49, 5.76, 7.72, 6.19, 6.08, 7.09, 7.82, 5.56, 11.62, 7.25, 4.81, 14.93, 4.60, 6.67, 17.57, 1.52, 3.38, 9.31, 9.07, 13.08, 15.75, 7.56, 16.81, 9.05, 15.52, 10.55, 8.27, 15.88, 16.76, 9.70, 15.77, 14.29, 10.24, 12.28, 9.57, 12.04, 17.67, 10.43, 3.31, 7.14, 6.67, 8.59, 7.18, 7.83, 13.07, 9.29, 19.62, 11.10, 1.75, 12.36, 17.98, 11.66, 25.35, 13.48, 12.79, 16.50, 16.95, 8.82, 13.52, 10.34, 5.04, 12.83, 12.73, 14.06, 16.58, 4.99, 12.25, 15.93, 14.62, 14.20, 17.14, 9.03, 13.30, 12.84, 10.99, 12.87, 11.77, 7.94, 13.11, 10.27, 4.32, 12.78, 9.16, 10.61],
    'Sales_Growth': [-2.66, -11.07, 54.18, 26.95, 3.46, 8.54, 39.36, 15.58, 1.67, 0.36, 64.59, 11.53, 21.34, 3.48, 7.68, 17.71, 6.97, -0.27, 5288.38, 8.05, 0.41, 7.43, 6.90, -33.51, -2.23, -11.07, 31.27, 30.67, 5.07, 69.40, 52.21, 2.52, 3.10, 10.53, 21.43, 28.60, 17.53, 23.87, 11.77, 8.14, 19.17, 7.62, 0.00, 42.09, 17.79, 22.79, 65.47, 11.84, 24.49, 9.58, 29.57, 35.70, 15.09, 2.71, -56.84, 5.07, 15.85, 10.09, 18.16, 3.42, 15.06, 115.13, 14.12, 6.25, 29.85, 22.51, 19.14, 205.68, 21.71, 27.68, 18.80, 15.61, 10.64, 13.84, 3.24, 13.90, 20.64, 7.95, 11.71, 7.08, 8.00, 5.37, -2.74, -15.35, 17.35, 56.18, -0.21, -2.63, 30.14, -3.11, 29.16, 15.12, 7.86, 4.92, 13.05, 9.05, 13.66, 4.36, 25.42],
    'Prof_Margin': [22.26, 1.41, 9.74, 9.24, 14.75, 9.50, 28.89, 29.42, 7.13, 19.18, 39.42, 9.25, 31.25, 3.27, 19.46, 1.69, 12.81, 5.49, -103.05, -0.98, 12.74, 19.19, -4.48, -37.15, 5.25, 1.41, -0.52, 20.95, 9.84, 24.05, -22.18, 12.43, 7.42, 30.00, 29.29, 38.99, 15.60, 36.20, 20.95, 3.15, 1.47, 15.69, 12.53, 32.58, 40.31, -2.89, 55.60, 8.05, 2.67, 17.96, -0.56, 72.95, 32.81, 17.47, 123.23, 9.84, 24.30, -0.32, -4.48, 6.47, 27.60, 25.70, 20.94, 38.78, -4.72, 11.31, 10.21, 35.37, -3.38, 3.14, 5.23, 5.14, 21.14, 0.17, 4.57, 21.29, 2.90, 15.81, 35.57, 4.88, 18.44, 18.43, 16.47, 2.02, 25.37, 36.31, 37.80, 31.60, 10.65, 4.35, -28.43, 18.89, 14.63, 50.58, 28.28, 14.08, 0.67, 39.03, -1.88]
}

df = pd.DataFrame(data)

# Calcul de la Rule of 40 et création de notre Score de comparaison basé à la fois sur la croissance des ventes, les marges, le free cash flow yield et le potentiel du prix de l'action avec une certaine pondération
df['Rule_of_40'] = df['Sales_Growth'] + df['Prof_Margin']
df['Pass_Rule40'] = df['Rule_of_40'] >= 40

# On écrête les valeurs extremes en limitant à un certain seuil pour ne pas fausser le score
g_clean = df['Sales_Growth'].clip(-20, 80)
m_clean = df['Prof_Margin'].clip(-20, 60)
fcf_clean = df['FCF_Yld'].clip(-5, 20)
up_clean = df['Upside'].clip(-0.1, 0.8)

# Normalisation min-max sur [0, 100]
def norm(s):
    return (s - s.min()) / (s.max() - s.min()) * 100

#Calcul de notre score croissance à un prix raisonnable (Growth At a Reasonable Price)
df['Score_GARP'] = (
    0.35 * norm(g_clean) +
    0.30 * norm(m_clean) +
    0.20 * norm(fcf_clean) +
    0.15 * norm(up_clean)
)

## Visualisation de l'univers
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Graphique 1 : Répartition par pays
df['Country'].value_counts().plot(kind='barh', ax=axes[0], color='blue')
axes[0].set_title("Répartition par pays")
axes[0].invert_yaxis()

# Graphique 2 : Croissance vs Marge et frontière Rule of 40
sub = df[df['Sales_Growth'].between(-50, 150) & df['Prof_Margin'].between(-50, 100)]
axes[1].scatter(sub['Sales_Growth'], sub['Prof_Margin'])
x_vals = np.linspace(-40, 120, 100)
axes[1].plot(x_vals, 40 - x_vals, 'r--', label='Seuil Rule of 40')
axes[1].set_title("Croissance vs Marge ")
axes[1].set_xlabel("Croissance des ventes (%)")
axes[1].set_ylabel("Marge bénéficiaire (%)")
axes[1].legend()

# Graphique 3 : Comparaison Rule of 40 vs Score GARP
axes[2].scatter(df['Rule_of_40'].clip(-50, 150), df['Score_GARP'], alpha=0.7, color='blue')
axes[2].axvline(40, color='red', linestyle='--', label='Rule of 40 = 40%')
axes[2].set_title("Comparaison : Rule of 40 vs Score GARP")
axes[2].set_xlabel("Rule of 40 (%) [bornée]")
axes[2].set_ylabel("Score GARP (/100)")
axes[2].legend()

plt.tight_layout()
plt.show()

## Analyse comparative des deux métriques
corr = df['Rule_of_40'].clip(-50, 150).corr(df['Score_GARP'])
print(f"Corrélation entre Rule of 40 et Score GARP : {corr:.2f}")
print(f"Entreprises validant la Rule of 40 (>= 40%) : {df['Pass_Rule40'].sum()} / {len(df)}")
print("\nTop 10 selon le Score GARP et leur Rule of 40:")
print(df[['Ticker', 'Short Name', 'Sales_Growth', 'Prof_Margin', 'Rule_of_40', 'FCF_Yld', 'Upside', 'Score_GARP']]
      .sort_values('Score_GARP', ascending=False).head(10).to_string(index=False))

## Construction et comparaison des portefeuilles
# Portefeuille diversifié : Top 25 titres équipondérés avec une allocation de 4% par titre (<= 5%)
nb_titres = 25
ptf_garp = df.sort_values('Score_GARP', ascending=False).head(nb_titres).copy()
ptf_garp['Poids'] = 1.0 / nb_titres  # soit 0.04 (4.0%)

# Portefeuille Benchmark : Univers complet équipondéré
ptf_univ = df.copy()
ptf_univ['Poids'] = 1.0 / len(df)

def stats_portefeuille(p, nom):
    w = p['Poids']
    # On utilise la médiane pour le P/E et la croissance afin d'éviter la distorsion des extrêmes
    return pd.Series({
        'Nb Titres': len(p),
        'Poids Max (%)': w.max() * 100,
        'Score GARP Moyen': (p['Score_GARP'] * w).sum(),
        'Rule of 40 Médiane (%)': p['Rule_of_40'].median(),
        'Croissance Ventes Médiane (%)': p['Sales_Growth'].median(),
        'Marge Bénéficiaire Moy. (%)': (p['Prof_Margin'] * w).sum(),
        'FCF Yield Moyen (%)': (p['FCF_Yld'] * w).sum(),
        'P/E Nxt Yr Médian': p['PE_Nxt_Yr'].median(),
        'PEG Médian': p['PEG'].median(),
        'Upside Moyen (%)': (p['Upside'] * w).sum() * 100,
    }, name=nom)

comparaison = pd.concat([
    stats_portefeuille(ptf_garp, "Portefeuille GARP (25 titres, 4% par titre)"),
    stats_portefeuille(ptf_univ, "Univers Équipondéré (99 titres)")
], axis=1)

print("\n COMPARAISON DES PORTEFEUILLES ")
print(comparaison.round(2))

# Graphique comparatif final
criteres_plot = ['Croissance Ventes Médiane (%)', 'Marge Bénéficiaire Moy. (%)', 'FCF Yield Moyen (%)', 'Upside Moyen (%)']
comparaison.loc[criteres_plot].plot(kind='bar', figsize=(10, 5), color=['green', 'blue'])
plt.title("Portefeuille Sélectionné vs Univers")
plt.ylabel("Pourcentage (%)")
plt.xticks(rotation=15)
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
