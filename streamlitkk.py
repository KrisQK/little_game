import streamlit as st
import random

st.title('智商训练器-Kris坤坤研发')

# 游戏选择
game = st.sidebar.selectbox('选择一个坤坤魔鬼特训-智商', ['数字之王', '幸运二百五'])

if game == '数字之王':
    st.header('数字之王-挑战主持人')
    number = st.number_input('输入一个数字（1-10）', 1, 10)
    if st.button('猜'):
        secret_number = random.randint(1, 10)
        if number == secret_number:
            st.success(f'恭喜你猜对了！你是一个数字之王! 数字是 {secret_number} 智商+1')
        else:
            st.error(f'猜错了，你这个笨笨狗, 数字是 {secret_number} 坤坤给你核桃疙瘩! 智商-100!')

elif game == '幸运二百五':
    st.header('幸运二百五')
    choice = st.radio('选择一种', ['石头', '剪刀', '布'])
    if st.button('出拳'):
        computer_choice = random.choice(['石头', '剪刀', '布'])
        if choice == computer_choice:
            st.write(f'平局！坤坤也选择了 {computer_choice}')
        elif (choice == '石头' and computer_choice == '剪刀') or \
             (choice == '剪刀' and computer_choice == '布') or \
             (choice == '布' and computer_choice == '石头'):
            st.success(f'你赢了！智商+1! 坤坤选择了 {computer_choice} 继续训练! 你是最棒的二百五! ')
        else:
            st.error(f'你输了，坤坤选择了 {computer_choice} 坤坤暴击小馒头! 智商-100! 你马上变成真正250了, 加油增加智商! ')
