import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 設定 App 基本資訊
st.set_page_config(page_title="東京熱血之旅", page_icon="🗼", layout="centered")
st.title("🗼 6天5夜 東京熱血之旅")
st.write("出發：3/8 捷星 GK012 | 回程：3/13 星宇 JX805")

# 建立三個分頁
tab1, tab2, tab3 = st.tabs(["📅 專屬行程", "🗺️ 互動地圖", "💰 旅費記帳"])

# === 分頁一：專屬行程與導航 ===
with tab1:
    st.header("行程明細與導航")
    
    with st.expander("Day 1 (3/8): 熱血開局，直衝大巨蛋", expanded=True):
        st.write("**08:00** | 抵達淺草，先至「住一淺草一號店」寄放行李")
        st.markdown("[📍 一鍵導航至飯店](https://www.google.com/maps/dir/?api=1&destination=住一淺草一號店)")
        st.write("**11:00** | 抵達東京巨蛋觀看 WBC 台灣 VS 韓國 (午餐吃球場便當)")
        st.markdown("[📍 一鍵導航至東京巨蛋](https://www.google.com/maps/dir/?api=1&destination=東京巨蛋)")
        st.write("**下午** | 秋葉原尋寶，找 Topps 棒球卡")
        st.write("**19:00** | 晚餐：淺草 牛舌檸檬")
        st.markdown("[📍 一鍵導航至牛舌檸檬](https://www.google.com/maps/dir/?api=1&destination=淺草牛舌檸檬)")

    with st.expander("Day 2 (3/9): 寶可夢樂園與迷幻新宿"):
        st.write("**11:00** | 讀賣樂園 (寶可夢主題樂園)")
        st.markdown("[📍 一鍵導航至讀賣樂園](https://www.google.com/maps/dir/?api=1&destination=讀賣樂園)")
        st.write("**傍晚** | 新宿繁華街頭，富士相機底片模擬街拍")
        st.write("**20:00** | 晚餐：新宿 神戶屋燒肉")
        st.markdown("[📍 一鍵導航至神戶屋](https://www.google.com/maps/dir/?api=1&destination=新宿神戶屋)")
        
    with st.expander("Day 3 (3/10): 次文化尋寶與頂級夜生活"):
        st.write("**上午** | 淺草寺周邊清晨散策")
        st.write("**下午** | 中野百老匯挖寶 (絕版漫畫、老玩具)")
        st.write("**20:00** | 六本木 63ANGEL 看秀")
        st.markdown("[📍 一鍵導航至 63ANGEL](https://www.google.com/maps/dir/?api=1&destination=六本木63ANGEL)")

    with st.expander("Day 4 (3/11): 伊豆海岸線放鬆一日遊"):
        st.write("**上午** | 搭乘特急踊子號前往伊豆")
        st.write("**下午** | 城崎海岸、門脇吊橋壯闊風景攝影與溫泉")
        st.markdown("[📍 一鍵導航至城崎海岸](https://www.google.com/maps/dir/?api=1&destination=城崎海岸)")

    with st.expander("Day 5 & 6 (3/12 - 3/13): 美食與歸途"):
        st.write("**3/12 上午** | 築地市場大啖海鮮")
        st.write("**3/12 下午** | 上野阿美橫町 (幫布偶貓買肉泥)")
        st.write("**3/13 15:30** | 回淺草拿行李，準備前往成田機場")
        st.markdown("[📍 一鍵導航至成田機場](https://www.google.com/maps/dir/?api=1&destination=成田機場)")

# === 分頁二：互動地圖 ===
with tab2:
    st.header("重點座標地圖")
    st.write("這次旅程的核心地標一覽：")
    # 建立以東京為中心的簡單地圖
    m = folium.Map(location=[35.6895, 139.6917], zoom_start=11)
    folium.Marker([35.7135, 139.7966], popup="住一淺草一號店", tooltip="住宿").add_to(m)
    folium.Marker([35.7056, 139.7519], popup="東京巨蛋", tooltip="WBC比賽").add_to(m)
    folium.Marker([35.6277, 139.5173], popup="讀賣樂園", tooltip="寶可夢樂園").add_to(m)
    st_folium(m, width=700, height=400)

# === 分頁三：旅費記帳 ===
with tab3:
    st.header("旅費記帳 (日幣 ¥)")
    
    # 初始化 session_state
    if "expenses" not in st.session_state:
        st.session_state.expenses = []

    # 記帳輸入框
    col1, col2 = st.columns([2, 1])
    with col1:
        item = st.text_input("項目名稱 (如：午餐)")
    with col2:
        price = st.number_input("金額", min_value=0, step=100)
        
    if st.button("新增花費"):
        if item and price > 0:
            st.session_state.expenses.append({"項目": item, "金額": price})
            st.success(f"已新增：{item} ¥{price}")

    # 顯示記帳清單與總計
    if st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)
        st.dataframe(df, use_container_width=True)
        total = df["金額"].sum()
        st.subheader(f"目前總計: ¥ {total:,}")