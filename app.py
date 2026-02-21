import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 設定 App 基本資訊
st.set_page_config(page_title="東京熱血之旅", page_icon="🗼", layout="centered")
st.title(🗼 6天5夜 東京熱血之旅)
st.write(出發：38 捷星 GK012  回程：313 星宇 JX805)

# 建立三個分頁
tab1, tab2, tab3 = st.tabs([📅 專屬行程, 🗺️ 互動地圖, 💰 旅費記帳])

# === 分頁一：專屬行程與導航 ===
with tab1
    st.header(行程明細與導航)
    
    with st.expander(Day 1 (38) 熱血開局，直衝大巨蛋, expanded=True)
        st.image(httpsimages.unsplash.comphoto-1509805903332-6804561081e4auto=format&fit=crop&w=800&q=80, use_container_width=True)
        st.write(0800  抵達淺草，先至「住一淺草一號店」寄放行李)
        st.markdown([📍 一鍵導航至飯店](httpswww.google.commapsdirapi=1&destination=住一淺草一號店))
        st.write(1100  抵達東京巨蛋觀看 WBC 台灣 VS 韓國 (午餐吃球場便當))
        st.markdown([📍 一鍵導航至東京巨蛋](httpswww.google.commapsdirapi=1&destination=東京巨蛋))
        st.write(下午  秋葉原尋寶，找稀有 Topps 棒球卡)
        st.write(1900  晚餐：淺草 牛舌檸檬)
        st.markdown([📍 一鍵導航至牛舌檸檬](httpswww.google.commapsdirapi=1&destination=淺草牛舌檸檬))

    with st.expander(Day 2 (39) 寶可夢樂園與迷幻新宿)
        st.image(httpsimages.unsplash.comphoto-1605901309584-818e25960b8fauto=format&fit=crop&w=800&q=80, use_container_width=True)
        st.write(1100  讀賣樂園 (新開幕寶可夢主題樂園))
        st.markdown([📍 一鍵導航至讀賣樂園](httpswww.google.commapsdirapi=1&destination=讀賣樂園))
        st.write(傍晚  新宿繁華街頭，帶著相機用底片模擬來場高質感街拍)
        st.write(2000  晚餐：新宿 神戶屋燒肉)
        st.markdown([📍 一鍵導航至神戶屋](httpswww.google.commapsdirapi=1&destination=新宿神戶屋))
        
    with st.expander(Day 3 (310) 次文化尋寶與頂級夜生活)
        st.image(httpsimages.unsplash.comphoto-1555580045-8495bc20c921auto=format&fit=crop&w=800&q=80, use_container_width=True)
        st.write(上午  淺草寺周邊清晨散策)
        st.write(下午  中野百老匯挖寶 (尋找絕版漫畫與老玩具))
        st.write(2000  六本木 63ANGEL 看華麗舞台秀)
        st.markdown([📍 一鍵導航至 63ANGEL](httpswww.google.commapsdirapi=1&destination=六本木63ANGEL))

    with st.expander(Day 4 (311) 伊豆海岸線放鬆一日遊)
        st.image(httpsimages.unsplash.comphoto-1493976040374-85c8e12f0c0eauto=format&fit=crop&w=800&q=80, use_container_width=True)
        st.write(上午  搭乘特急踊子號前往伊豆)
        st.write(下午  城崎海岸、門脇吊橋壯闊風景攝影與泡日歸溫泉)
        st.markdown([📍 一鍵導航至城崎海岸](httpswww.google.commapsdirapi=1&destination=城崎海岸))

    with st.expander(Day 5 & 6 (312 - 313) 美食與歸途)
        st.image(httpsimages.unsplash.comphoto-1533052306132-75d164627d2cauto=format&fit=crop&w=800&q=80, use_container_width=True)
        st.write(312 上午  築地市場大啖海鮮)
        st.write(312 下午  上野阿美橫町 (採買藥妝，賞櫻！))
        st.write(313 1530  回淺草拿行李，準備前往成田機場)
        st.write(313 2010  搭乘星宇 JX805 準備回程)
        st.markdown([📍 一鍵導航至成田機場](httpswww.google.commapsdirapi=1&destination=成田機場))

# === 分頁二：互動地圖 ===
with tab2
    st.header(重點座標地圖)
    st.write(這次旅程的核心地標一覽：)
    m = folium.Map(location=[35.6895, 139.6917], zoom_start=10)
    folium.Marker([35.7135, 139.7966], popup=住一淺草一號店, tooltip=住宿).add_to(m)
    folium.Marker([35.7056, 139.7519], popup=東京巨蛋, tooltip=WBC比賽).add_to(m)
    folium.Marker([35.6277, 139.5173], popup=讀賣樂園, tooltip=寶可夢樂園).add_to(m)
    folium.Marker([34.8829, 139.1357], popup=城崎海岸, tooltip=伊豆絕景).add_to(m)
    st_folium(m, width=700, height=400)

# === 分頁三：旅費記帳 ===
with tab3
    st.header(旅費記帳 (日幣 ¥))
    
    if expenses not in st.session_state
        st.session_state.expenses = []

    col1, col2 = st.columns([2, 1])
    with col1
        item = st.text_input(項目名稱 (如：球場便當))
    with col2
        price = st.number_input(金額, min_value=0, step=100)
        
    if st.button(新增花費)
        if item and price  0
            st.session_state.expenses.append({項目 item, 金額 price})
            st.success(f已新增：{item} ¥{price})

    if st.session_state.expenses
        df = pd.DataFrame(st.session_state.expenses)
        st.dataframe(df, use_container_width=True)
        total = df[金額].sum()
        st.subheader(f目前總計 ¥ {total,})