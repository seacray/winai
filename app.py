import streamlit as st
import numpy as np
import time
# Page title and introduction
st.title("💡 Winai Robo-Advisor for K-Wealth Plus")
st.write("Your personalized financial planning assistant.")
st.divider()


with st.chat_message("assistant"):
    st.write("สวัสดีผมคือ Winai Robo-Advisor สำหรับช่วยวางแผนการลงทุนใน K-Wealth Plus มีอะไรให้ผมช่วยไหมครับ?")
    time.sleep(5)


with st.chat_message("user"):
    st.write("User : ผมมีสถานะทางการเงินเป็นอย่างไร? ช่วยผมวิเคราะห์ได้ไหมครับ")
    time.sleep(2)

with st.chat_message("assistant"):
    st.write("Winai Robo-Advisor : ยินดีครับ คุณผู้ใช้ ผมขออนุญาตสอบถามข้อมูลเพิ่มเติมนะครับ ปัจจุบันคุณมี สินทรัพย์ อะไรบ้างมูลค่าเท่าไหร่พอจะบอกได้ไหมครับ")
    time.sleep(2)

with st.chat_message("user"):
    st.write("User : มีบ้านราคา 20 ล้าน รถยนต์หนึ่งคัน 2 ล้าน เงินฝาก 5 ล้าน เงินฝากประจำ 2 ล้าน")
    time.sleep(2)

with st.chat_message("assistant"):
    st.write("Winai Robo-Advisor: ดีเลยครับ ผมขอสอบถามเพิ่มเติมคุณมีหนี้สินอะไรบ้างครับ")
    time.sleep(2)

with st.chat_message("user"):
    st.write("User : หนี้บ้าน 10 ล้านครับ")
    time.sleep(2)

with st.chat_message("assistant"):
    st.write("Winai Robo-Advisor : ผมขอสอบถามเกี่ยวกับรายได้คุณบ้างครับ คุณมีรายได้ต่อเดือนเท่าไหร่ครับ")
    time.sleep(2)

with st.chat_message("user"):
    st.write("User : เงินเดือน 2 แสนครับกับดอกเบี้ยประมาณ 1000 บาทต่อเดือนครับ")
    time.sleep(2)

with st.chat_message("assistant"):
    st.write("Winai Robo-Advisor : ไกล้จบแล้วครับ คุณมีรายจ่ายต่อเดือนอะไรบ้างครับ")
    time.sleep(2)

with st.chat_message("user"):
    st.write("User : รายจ่ายส่วนตัว ประมาณ 100,000 ครับ")
    time.sleep(2)

with st.chat_message("assistant"):
    st.write("Winai Robo-Advisor : สุขภาพทางการเงินของคุณอยู่ในระดับ “ดี” หากอยากรู้ว่าด้านใดที่ดีอยู่แล้ว และด้านใดที่ต้องปรับปรุง เพื่อให้สุขภาพทางการเงินของคุณแข็งแรงยิ่งขึ้น ลองไปดูผลการวิเคราะห์แยกส่วนกันต่อเลยดีกว่า!!")
    time.sleep(0.5)
    st.write("ปัจจุบันฐานะทางการเงินของคุณ “ยังไม่ดี” สักเท่าไหร่ มีภาระหนี้สินค่อนข้างมาก แต่โชคดีที่คุณสามารถบริหารรายได้และค่าใช้จ่ายในแต่ละเดือนได้เป็นอย่างดี ทำให้มีเงินเหลือไปต่อยอดความมั่งคั่งได้")
    time.sleep(0.5)
    st.write("คุณมีเงินสำรองเผื่อฉุกเฉิน “มากเกินความจำเป็น” ซึ่งโดยทั่วไปมีเงินสำรองเผื่อฉุกเฉินประมาณ 3–6 เท่าของค่าใช้จ่ายในปัจจุบัน ก็นับว่าเพียงพอแล้ว ส่วนที่เหลือก็ควรนำไปลงทุนในสินทรัพย์ประเภทต่างๆ เพื่อสร้างความมั่งคั่งให้เพิ่มขึ้น")
    time.sleep(0.5)
    st.write("คุณมีเงินออมต่อเดือนอยู่ในเกณฑ์ “ดี” ซึ่งเงินออมก้อนนี้ ถือเป็นรากฐานสำคัญที่จะนำไปใช้เพื่อต่อยอดความมั่งคั่งในอนาคต")
    time.sleep(0.5)
    st.write("มาดูที่สินทรัพย์ลงทุนกันบ้างดีกว่า… คุณมีสินทรัพย์ลงทุน “ไม่มากนัก” อาจต้องให้ความสำคัญกับการลงทุนในสินทรัพย์ต่างๆ เช่น พันธบัตร หุ้นกู้ กองทุนรวม หรือหุ้นของบริษัทที่เติบโตและมั่นคง ฯลฯ ให้มากกว่านี้ เพราะสินทรัพย์เหล่านี้จะช่วยสร้างรายได้ และช่วยให้คุณมีความมั่งคั่งเพิ่มขึ้น")
    time.sleep(0.5)
    st.write("ที่นี้ คุณอยาก ให้ผมช่วยวางแผนทางการเงินเพื่อเกษียณ หรือ เงินก้อนอื่นใดไหมครับ")
    time.sleep(4)

with st.chat_message("user"):
    st.write("User : ก็ดีนะครับ ผมอยากเกษียณตอนอายุ 55 มีเงินก้อนสัก 20 ล้าน เก็บเงินลงทุนอะไรดี")
    time.sleep(2)

with st.chat_message("assistant"):
    st.write("Winai Robo-Advisor : ผมมีคำแนะนำดีดีแน่นอนครับ แต่ เอ๊ะขออนุญาตนะครับปัจจุบันคุณลูกค้าอายุเท่าไหร่ครับ")
    time.sleep(2)

with st.chat_message("user"):
    st.write("User : 35 ครับ")
    time.sleep(2)

with st.chat_message("assistant"):
    st.write("Winai Robo-Advisor : แล้วมีเงินที่จะลงทุนเพื่อการนี้อยู่ไหมครับ")
    time.sleep(2)

with st.chat_message("user"):
    st.write("User : 1 ล้านก็ได้ครับ")
    time.sleep(2)

with st.chat_message("assistant"):
    st.write("Winai Robo-Advisor : ผมมีแผนการเงินที่น่าสนใจมาเสนอ 3 แผน")

    st.write("‘K-WPULTIMATE’, ‘expected_return’: 10.0%, ‘expected_volatility’: 25.0%, ‘ต้องออมต่อเดือ่น’: 35602.32")

    st.write("K-WPSPEEDUP, ‘expected_return’: 8.0%, ‘expected_volatility’: 15.0%, ‘ต้องออมต่อเดือ่น’: 42528.16")
    st.write("K-WPBALANCED’, ‘expected_return’: 4.0%, ‘expected_volatility’: 10.0%, ‘ต้องออมต่อเดือ่น’: 57787.29")
    st.write("เพื่อให้แนะนำแผนที่เหมาะสมโปรดทำแบบประเมินความเสี่ยงที่นะครับ ผมจะได้บอกได้ว่าแผนใดเหมาะกับคุณ")
    st.write("[แบบประเมินความเสี่ยงคลิ๊ก](https://www.set.or.th/project/caltools/risk.html)")





    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Data from the chart
    categories = ['K-WPBALANCED', 'K-WPSPEEDUP', 'K-WPULTIMATE']
    data = {
        'Cash': [9, 6, 6],
        'Thai Bond': [53, 23, 0],
        'Foreign Bond': [12, 11, 16],
        'Thai Equity': [26, 59, 74],
        'Foreign Equity': [0, 0, 0]
    }
    
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data, index=categories)
    
    # Streamlit Title
    st.title("Investment Allocation Chart")
    
    # Generate the chart using Matplotlib
    fig, ax = plt.subplots()
    
    # Bar width
    bar_width = 0.6
    
    # Positions
    x = range(len(categories))
    bottom_cumulative = [0] * len(categories)
    
    # Plot each category in stacked bar format
    for label in data.keys():
        ax.bar(x, df[label], bar_width, bottom=bottom_cumulative, label=label)
        bottom_cumulative = [i + j for i, j in zip(bottom_cumulative, df[label])]
    
    # Customize chart
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylabel('Percentage')
    ax.set_title('Investment Allocation')
    ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.0))
    
    # Display the chart
    st.pyplot(fig)
    
