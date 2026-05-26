import streamlit as st
import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI智能伴侣")
# logo
st.logo("resources/logo.jpg")
# 系统提示词
system_prompt = "你是一个AI助理，名字叫小余"

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

#消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt: # 字符串会自动转换为布尔值,如果字符串为空,则为True; ""则为False
    st.chat_message("user").write(prompt)
    print("--------->调用大模型,提示词:",prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role":"user","content":prompt})

    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            # {"role": "user", "content": prompt}
            # 采用解包
            *st.session_state.messages
        ],
        stream=True
    )

    # 输出大模型返回的结果(非流式输出的解析方式)
    # print("--------->调用大模型,提示词:",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出大模型返回的结果(流式输出的解析方式)
    response_message = st.empty() # 创建一个空的组件，用于展示大模型返回的结果

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_response += content
                response_message.chat_message("assistant").write(full_response)


    #保存大模型返回的结果
    st.session_state.messages.append({"role":"assistant","content":full_response})

