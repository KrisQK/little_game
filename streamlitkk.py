import streamlit as st
import random

st.title('小游戏集合')

# 游戏选择
game = st.sidebar.selectbox('选择一个游戏', ['猜数字', '石头剪刀布'])

if game == '猜数字':
    st.header('猜数字游戏')
    number = st.number_input('输入一个数字（1-10）', 1, 10)
    if st.button('猜'):
        secret_number = random.randint(1, 10)
        if number == secret_number:
            st.success(f'恭喜你猜对了！数字是 {secret_number}')
        else:
            st.error(f'猜错了，数字是 {secret_number}')

elif game == '石头剪刀布':
    st.header('石头剪刀布')
    choice = st.radio('选择一种', ['石头', '剪刀', '布'])
    if st.button('出拳'):
        computer_choice = random.choice(['石头', '剪刀', '布'])
        if choice == computer_choice:
            st.write(f'平局！电脑也选择了 {computer_choice}')
        elif (choice == '石头' and computer_choice == '剪刀') or \
             (choice == '剪刀' and computer_choice == '布') or \
             (choice == '布' and computer_choice == '石头'):
            st.success(f'你赢了！电脑选择了 {computer_choice}')
        else:
            st.error(f'你输了，电脑选择了 {computer_choice}')
