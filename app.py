import streamlit as st

st.title("サンプルアプリ②: 少し複雑なWebアプリ")

st.write("##### 動作モード1: 文字数カウント")
# #を6つまで並べることができます。これは文字を太くする際に使用します。#が少ないほど、大きく太く表示できます。
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("##### 動作モード2: BMI値の計算")
st.write("身長と体重を入力することで、肥満度を表す体型指数のBMI値を算出できます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["文字数カウント", "BMI値の計算"]
)
# radio()メソッドを使用することで、ラジオボタンを表示できます。
# 第一引数はラジオボタンのラベルとして上部に表示され、第二引数にリストで指定した各要素のテキスト
# が、選択肢として表示されます。
st.divider()
# divider()メソッドを使用することで、水平線を表示できます。 

if selected_item == "文字数カウント":
    input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")
    text_count = len(input_message)

else:
    height = st.text_input(label="身長（cm）を入力してください。")
    weight = st.text_input(label="体重（kg）を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "文字数カウント":
        if input_message:
            st.write(f"文字数: **{text_count}**")

        else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")
# error()メソッドを使用することで、エラーメッセージを赤色で表示できます。
    else:
        if height and weight:
            try:
                bmi = round(int(weight) / ((int(height)/100) ** 2), 1)
                # round()関数は、小数点を起点に四捨五入する関数で、「1」の場合は、少数第一位までを表示するという意味です。
                # **はべき乗を示し、この場合は2乗したいので、「2」と指定します。
                # 例えば、「**3」であれば3乗という意味です。
                st.write(f"BMI値: {bmi}")

            except ValueError as e:
                st.error("身長と体重は数値で入力してください。")

        else:
            st.error("身長と体重をどちらも入力してください。")