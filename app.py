import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# --- 1. 读取我们的数据弹药库 ---
try:
    df = pd.read_csv("iphone_data.csv")
except FileNotFoundError:
    st.error("找不到数据文件！请确保 iphone_data.csv 和本代码在同一个文件夹里。")
    st.stop()

# --- 2. 核心：数据翻译与模型训练 ---
model_mapping = {
    'iPhone 13': 1, 
    'iPhone 13 Pro': 2, 
    'iPhone 14': 3, 
    'iPhone 14 Pro': 4, 
    'iPhone 15': 5
}
df['型号_数字代号'] = df['型号'].map(model_mapping)

X = df[['型号_数字代号', '容量_GB', '电池健康度_%', '成色得分']]
y = df['成交价_元']

# 唤醒 AI 大脑并让它学习
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# --- 3. 搭建炫酷的网页界面 ---
st.set_page_config(page_title="AI 二手手机估价师", page_icon="📱")
st.title("📱 AI 二手手机估价师 (Pro 版)")
st.markdown("背后搭载机器学习算法，基于 **500 条最新市场数据** 实时演算！")
st.divider()

col1, col2 = st.columns(2)
with col1:
    model_choice = st.selectbox("请选择手机型号", list(model_mapping.keys()))
    storage_choice = st.selectbox("请选择容量 (GB)", [128, 256, 512])
with col2:
    battery_choice = st.slider("电池健康度 (%)", 70, 100, 85)
    condition_choice = st.slider("外观成色打分 (10分为全新未拆封)", 1, 10, 8)

# --- 4. 见证 AI 的预测实力 ---
if st.button("🚀 启动 AI 精准估价", type="primary", use_container_width=True):
    user_input = pd.DataFrame({
        '型号_数字代号': [model_mapping[model_choice]],
        '容量_GB': [storage_choice],
        '电池健康度_%': [battery_choice],
        '成色得分': [condition_choice]
    })
    
    prediction = model.predict(user_input)[0]
    
    st.balloons()
    st.success(f"根据当前市场行情深度计算，这台 **{model_choice} ({storage_choice}GB)** 的合理估价约为：")
    st.metric(label="AI 建议挂牌价", value=f"¥ {prediction:.0f}")
    st.info("💡 提示：此价格由 Random Forest 算法分析市场成交规律计算得出，包含因电池与外观折损的动态扣减。")
