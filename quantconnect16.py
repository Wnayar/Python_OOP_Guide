rates = {
    "USDAUD": 1.5,    # Australia
    "USDCAD": 0.5,    # Canada
    "USDCNY": 4.35,   # China
    "USDEUR": 0.0,    # Euro Area
    "USDINR": 6.5,    # India
    "USDJPY": -0.1,   # Japan
    "USDMXN": 4.25,   # Mexico
    "USDTRY": 7.5,    # Turkey
    "USDZAR": 7.0     # South Africa
}

print(rates)

sorted_rates = sorted(rates.items(), key = lambda x:x[1])
print(sorted_rates)

print(sorted_rates[0][-1])
print(sorted_rates[-1][0])