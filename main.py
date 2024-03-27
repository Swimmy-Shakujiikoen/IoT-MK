"""スマホのボタン側のプログラム

© 2024 Swimmy石神井公園校
"""

import js

import btncon

# ボタンのコントローラーを発動
btn = btncon.ButtonController()

# 準備OKでないなら、ボタンを失敗マークにする
if not btn.is_ready():
    js.btn_failure()


# ボタン発動時
async def btn_click(event) -> None:
    ### IoTに信号を送る ###

    # 信号の送信に失敗した場合はボタンを失敗マークにする
    if not ### 信号の送信に成功した確認する ###:
        ### ボタンを失敗マークにする ###
        return

    # IoT側が動作完了するまで10秒ごとに確認する
    while not await ### IoT側が動作完了したか確認する ###:
        ### 10秒待つ ###

    ### ボタンを成功マークにする ###
