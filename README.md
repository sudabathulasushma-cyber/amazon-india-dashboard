# Amazon India Dashboard

An interactive management dashboard built for the SapphireIQ Data Analyst internship. It gives a non-technical manager (Ravi) a one-page view of sales, profit, products, orders, order status, payment, fulfilment and state-wise performance.

 **Live demo:** https://sudabathulasushma-cyber.github.io/amazon-india-dashboard/

## What the dashboard shows

| Section | Contents |
|---|---|
| 1. Overall sales and profit | Total Sales, Total Profit, Total Orders, Units Sold, Average Order Value, Profit Margin %, monthly sales and profit trend |
| 2. Categories and products | Category-wise sales, profit and units sold; Top 10 products by sales |
| 3. Order status and revenue loss | Delivered, Shipped, Returned and Cancelled orders; Return Rate %; Cancellation Rate %; category-wise returns and cancellations; sales lost |
| 4. Payment, fulfilment and states | Sales and profit by payment method and by fulfilment method; state-wise sales, profit and orders |

Filters for **Year**, **Category** and **State** update every KPI and chart. Each section ends with an auto-generated insight in plain language.

## Project structure

```
amazon-india-dashboard/
├── index.html                  # the finished dashboard (open in any browser)
├── dashboard_template.html     # HTML, CSS and JavaScript for the dashboard
├── build_dashboard.py          # reads the Excel data and builds index.html
├── data/Amazon_Sales_Data_India.xlsx
├── requirements.txt
└── README.md
```

## How to run

Just open `index.html` in a browser. No server or internet connection is needed.

To rebuild it from the data:

```bash
pip install -r requirements.txt
python build_dashboard.py
```

## Dataset

10,000 orders from Jan 2024 to Aug 2026 with 13 columns: order ID and date, category, product, quantity, unit price, discount, total sales (INR), profit (INR), payment method, fulfilment, order status and ship state. The data has no nulls or duplicates, and `Total_Sales_INR` equals Quantity x Unit Price x (1 - Discount) on every row.

## Key numbers

- Total sales: Rs 15.58 crore | Total profit: Rs 3.32 crore | Profit margin: 21.3%
- Orders: 10,000 | Units sold: 24,926 | Average order value: Rs 15,579
- Return rate: 4.85% | Cancellation rate: 5.0%

## Assumptions

- **Sales are gross.** Cancelled and returned orders keep their sales value but have zero profit in the data. The dashboard reports them separately as "Sales lost" (about 10% of sales).
- **Shipped orders** are still in transit, so they are not counted as lost.
- **2026 is a partial year** (January to August), so compare month by month, not by yearly totals.
- Money is shown in Indian units: L = lakh (1,00,000), Cr = crore (1,00,00,000).

## Tech

HTML, CSS and vanilla JavaScript (charts drawn with SVG and CSS, no external libraries). Python with pandas prepares the data.
