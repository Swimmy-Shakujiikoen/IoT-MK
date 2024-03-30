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
    await btn.send_trigger()
    # 信号の送信に失敗した場合はボタンを失敗マークにする
    if not btn.is_send_ok(): ### 信号の送信に成功した確認する ###
        js.btn_failure()### ボタンを失敗マークにする ###
        return

    # IoT側が動作完了するまで10秒ごとに確認する
    while not await btn.is_done(): ### IoT側が動作完了したか確認する ###:
        await btn.sleep(10)### 10秒待つ ###

    js.btn_success()### ボタンを成功マークにする ###
