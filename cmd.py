import subprocess
from typing import List
from kitty.boss import Boss

def main(args: List[str]) -> str:
    p = subprocess.run(["navi", "--print"], capture_output=True, text=True)
    cmd = p.stdout
    return cmd

def handle_result(args: List[str], answer: str, target_window_id: int, boss: Boss) -> None:
    # get the kitty window into which to paste answer
    w = boss.window_id_map.get(target_window_id)
    if w is not None:
        w.paste_text(answer)
