import pandas as pd
import random

print("⚙️ 正在生成真实的二手 iPhone 市场数据...")

data_list = []
models = ['iPhone 13', 'iPhone 13 Pro', 'iPhone 14', 'iPhone 14 Pro', 'iPhone 15']
storages = [128, 256, 512]

# 模拟 500 条数据
for _ in range(500):
    model = random.choice(models)
    storage = random.choice(storages)
    battery = random.randint(75, 100) # 电池健康度 75% 到 100%
    condition = random.randint(5, 10) # 成色打分 5 到 10 分
    
    # 设定基础价格
    base_price = 0
    if '13' in model: base_price = 2800
    if '14' in model: base_price = 3800
    if '15' in model: base_price = 4800
    if 'Pro' in model: base_price += 1000
    
    # 根据容量、电池和成色调整价格
    if storage == 256: base_price += 400
    if storage == 512: base_price += 900
    
    # 电池和成色越差，扣钱越多，并加入一点随机市场波动（±150元）
    price = base_price - ((100 - battery) * 15) - ((10 - condition) * 100) + random.randint(-150, 150)
    
    data_list.append({
        '型号': model,
        '容量_GB': storage,
        '电池健康度_%': battery,
        '成色得分': condition,
        '成交价_元': price
    })

# 保存为 CSV
df = pd.DataFrame(data_list)
df.to_csv("iphone_data.csv", index=False, encoding='utf-8-sig')

print(f"✅ 成功生成 {len(df)} 条数据！")
print("📁 数据已保存为 iphone_data.csv，现在我们有充足的弹药来训练 AI 模型了！")