import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt

# 20年前から今日までの日付範囲を計算
end_date = dt.datetime.today()
start_date = end_date - dt.timedelta(days=20 * 365)

# S&P500（^GSPC）の日次データを取得
df = yf.download("^GSPC", start=start_date.strftime("%Y-%m-%d"),
                 end=end_date.strftime("%Y-%m-%d"))

# 各年の最初の終値を基準に正規化
df['Year'] = df.index.year
first_close = df.groupby('Year')['Close'].transform('first')
df['Normalized'] = df['Close'] / first_close * 100

# グラフ作成
fig, ax = plt.subplots(figsize=(12, 6))
for year, group in df.groupby('Year'):
    ax.plot(group.index, group['Normalized'], label=str(year))

ax.set_title("S&P 500 各年初を100として正規化した推移")
ax.set_xlabel("日付")
ax.set_ylabel("指数 (年初 = 100)")
ax.legend(loc="upper left", ncol=2, fontsize="small")
plt.show()
