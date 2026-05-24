import streamlit as st

# 大标题
st.title("Streamlit 入门表演")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落文字
st.write("你好!!!!!!!!!!!!!!!!!")
# 图片
st.image("resources/cat.jpg")
# 音频
st.audio("resources/news.mp3")
# # 视频
st.video("resources/news.mp4")
# # Logo
st.logo("resources/logo.png")
# 表格
student_data = {
    "姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98, 90, 59, 29, 80],
    "数学": [88, 78, 65, 70, 39],
    "英语": [99, 89, 87, 59, 62],
    "总分": [285, 257, 211, 158, 181]
}

st.table(student_data)

# 输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名为:{name}")
# 单选按钮
password = st.text_input("请输入密码", type="password")
st.write(f"您输入的密码为:{password}")
# 单选按钮
gender = st.radio("请输入您的性别",["男","女","未知"],index=1)
st.write(f"您的性别为:{gender}")