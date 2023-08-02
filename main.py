def profit(buy, shipping, packaging, selling):
    percent = (buy + shipping + packaging) * 0.20
    sum1 = (buy + shipping + packaging) + percent
    ebay_amazon_fee = selling * 0.18
    add = selling - ebay_amazon_fee
    final_profit = add - sum1

    return round(final_profit, 2)