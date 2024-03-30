# 使用するモジュールのインポート
import btncon
import js

# ボタンのコントローラーを発動
btn = btncon.ButtonController()


# ボタン発動時
async def btn_click(event) -> None:
    await btn.sleep(5)### 5秒待つ ###

    ### ボタンを成功マークにする ###
    js.btn_success()  # 成功マークにする