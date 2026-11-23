# Chaker_Souissi.py

Three quantitative finance projects in Python. Below is the output obtained by running each script (Python 3, pandas / numpy / matplotlib / seaborn).

## 1. [`Chaker_Souissi.py`](Chaker_Souissi.py) — Euro Stoxx 50 analysis

This script prints nothing to the console: its output is three charts.

- **Graph 1 — Analyst upside vs. BEst P/E ratio:** a regression with a negative slope. The higher the P/E, the lower the upside expected by analysts.
  <img width="1389" height="787" alt="image" src="https://github.com/user-attachments/assets/5959e9c3-7c7d-40e2-9f40-e0a4833793d4" />

- **Graph 2 — ESG score vs. 1-year total return:** a regression with a 99% confidence interval.
- **Graph 3 — Risk (360-day volatility) vs. 1-year return by sector:** the SX5E Index is the benchmark (red star), with average-volatility and average-return lines.

## 2. [`Dynamic Portfolio Allocation.py`](Dynamic%20Portfolio%20Allocation.py)

```
Nombre de réallocations : 10
Performance totale : 189.12%

               2026-01-01 2026-01-21 2026-03-30 2026-04-17 2026-04-28 2026-06-02 2026-06-10 2026-06-22 2026-06-26 2026-07-29 2026-10-05
SXKP Index                        20                                                                                                   
SX6E index                        20                    20                                                                             
SX3P Index                                                                    20                    20                               20
SXEP Index                        20                    20                                                     20         20           
SXPP index             20                                          20                                                     20           
SXIP index                                                                                                     20                      
SX7E Index                                   20                                          20                                            
SX8P index             20                    20                    20                                                     20           
SXQE Index                                                                    20                    20                                 
SX86P index                                                                                         20                                 
SXNP Index             20                                                                                                              
sxrp index                                                                    20                                                     20
sxfp index                                                                                                     20                      
sxop index                                                                               20                                            
sxmp index                                   20                                                                20                      
sx6p index                                              20                                                                             
sx7p index                                                                               20                    20                      
SX8E Index             20                                          20                    20                               20           
SXDP Index                                                                    20                    20                               20
SXKE Index                        20                               20                                                                  
RTY Index              20                    20                                                                                        
sxqp index                                                                    20                    20                               20
IXN US Equity                                20         20         20                    20                               20           
WELD GY Equity                    20                    20                                                                           20
```

## 3. [`Equity Research & Quantitative Stock Screening.py`](Equity%20Research%20%26%20Quantitative%20Stock%20Screening.py)

```
Corrélation entre Rule of 40 et Score GARP : 0.88
Entreprises validant la Rule of 40 (>= 40%) : 30 / 99

Top 10 selon le Score GARP et leur Rule of 40:
Ticker       Short Name  Sales_Growth  Prof_Margin  Rule_of_40  FCF_Yld  Upside  Score_GARP
  NVDA      NVIDIA CORP         65.47        55.60      121.07     3.15   0.711   78.291211
   IDR   INDRA SISTEMAS         64.59        39.42      104.01    20.86   0.211   77.006450
  CRDO CREDO TECHNOLOGY        205.68        35.37      241.05     1.71   1.054   76.131750
   WDC  WESTERN DIGITAL         35.70        72.95      108.65     3.92   0.993   71.631000
  ALAB  ASTERA LABS INC        115.13        25.70      140.83     0.88   0.558   67.781097
  RDDT     REDDIT INC-A         69.40        24.05       93.45     6.28   0.471   66.312616
  MRVL MARVELL TECHNOLO         42.09        32.58       74.67     1.18   0.972   61.393000
  PLTR PALANTIR TECHN-A         56.18        36.31       92.49     1.49   0.328   60.051787
   ASM      ASM INTL NV         39.36        28.89       68.25     2.45   0.643   57.435522
  CHTR CHARTER COMMUN-A        -56.84       123.23       66.39    24.29   0.251   55.788591

 COMPARAISON DES PORTEFEUILLES 
                               Portefeuille GARP (25 titres, 4% par titre)  Univers Équipondéré (99 titres)
Nb Titres                                                            25.00                            99.00
Poids Max (%)                                                         4.00                             1.01
Score GARP Moyen                                                     55.75                            40.53
Rule of 40 Médiane (%)                                               63.92                            26.44
Croissance Ventes Médiane (%)                                        28.60                            11.84
Marge Bénéficiaire Moy. (%)                                          31.88                            14.93
FCF Yield Moyen (%)                                                   4.52                             4.60
P/E Nxt Yr Médian                                                    18.90                            17.84
PEG Médian                                                            0.69                             1.25
Upside Moyen (%)                                                     47.88                            32.04
```
