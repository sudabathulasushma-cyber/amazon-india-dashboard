"""Builds index.html (a self-contained interactive dashboard) from the Excel sales data.

Usage:  python build_dashboard.py
"""
import json
import pandas as pd

SRC = "data/Amazon_Sales_Data_India.xlsx"
TEMPLATE = "dashboard_template.html"
OUT = "index.html"

df = pd.read_excel(SRC)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.strftime("%Y-%m")

def codes(col):
    """Return (sorted list of unique values, value -> index lookup)."""
    vals = sorted(df[col].unique())
    return vals, {v: i for i, v in enumerate(vals)}

months, mi = codes("Month")
cats, ci = codes("Category")
prods, pi = codes("Product")
pays, payi = codes("Payment_Method")
fuls, fi = codes("Fulfillment")
sts, si = codes("Order_Status")
states, sti = codes("Ship_State")

# One compact row per order:
# [month, category, product, quantity, sales, profit, payment, fulfilment, status, state]
rows = [
    [mi[r.Month], ci[r.Category], pi[r.Product], int(r.Quantity),
     round(float(r.Total_Sales_INR), 2), round(float(r.Profit_INR), 2),
     payi[r.Payment_Method], fi[r.Fulfillment], si[r.Order_Status], sti[r.Ship_State]]
    for r in df.itertuples()
]

data = dict(months=months, cats=cats, prods=prods, pays=pays,
            fuls=fuls, sts=sts, states=states, rows=rows)

html = open(TEMPLATE, encoding="utf-8").read().replace("__DATA__", json.dumps(data, separators=(",", ":")))
open(OUT, "w", encoding="utf-8").write(html)

print(f"Built {OUT}: {len(rows)} orders | sales Rs {df.Total_Sales_INR.sum():,.0f} | profit Rs {df.Profit_INR.sum():,.0f}")
