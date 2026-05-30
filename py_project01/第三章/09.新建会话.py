import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

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

# 生成会话标识函数
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 保存会话信息函数
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }

        # 如果session目录不存在,则创建
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        # 保存会话数据
        with open(f"sessions/{st.session_state.current_session}.json","w",encoding="utf-8") as f:
            json.dump(session_data,f,ensure_ascii=False,indent=2)

# 大标题
st.title("AI智能伴侣")
# logo
st.logo("resources/logo.jpg")
# 系统提示词
system_prompt = """
你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。

规则:
1. 每次只回1条消息
2. 禁止任何场景或状态描述性文字
3. 匹配用户的语言
4. 回复简短，像微信聊天一样
5. 有需要的话可以用❤️🌸等emoji表情
6. 用符合伴侣性格的方式对话
7. 回复的内容，要充分体现伴侣的性格特征

伴侣性格:
- %s

你必须严格遵守上述规则来回复用户。
"""

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的东北姑娘"
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

# 左侧的侧边栏 - with:streamlit中上下文管理器
with st.sidebar:
    # 会话信息
    st.subheader("AI控制面板")
    # 新建会话
    if st.button("新建会话",width="stretch",icon="✏️"):
        # 1.保存当前会话信息
        save_session()
        # 2.创建新的会话
        if st.session_state.messages: # 如果聊天信息非空,则为True ,否则为False
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun() # 重新运行当前页面

    # 昵称输入框
    nick_name = st.text_input("昵称" , placeholder="请输入昵称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    # 性格输入框
    nature = st.text_area("性格",placeholder="请输入性格" ,value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

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
            {"role": "system", "content": system_prompt % (st.session_state.nick_name,st.session_state.nature)},
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

