"""
今日编程提示 - 五行推算脚本
基于当前日期 × 用户名，输出五行属性和状态等级。
"""
import subprocess, datetime, os

def get_username():
    for cmd in [["git", "config", "user.name"], ["git", "config", "user.email"]]:
        try:
            out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode().strip()
            if out:
                return out.split("@")[0]
        except Exception:
            pass
    return os.environ.get("USER") or "unknown"

def calc_tiangan(username, date):
    date_val = date.year * 5 + date.month + date.day
    name_val = sum(ord(c) for c in username) % 5
    return (date_val + name_val) % 10

TIANGAN    = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
WUXING_MAP = ["木","木","火","火","土","土","金","金","水","水"]
STATUS_MAP = {"火":"状态爆棚","木":"手感火热","金":"稳定输出","土":"平平无奇","水":"宜摸鱼充电"}
ENERGY_MAP = {"火":100,"木":80,"金":60,"土":40,"水":20}

today    = datetime.date.today()
username = get_username()
idx      = calc_tiangan(username, today)
tiangan  = TIANGAN[idx]
wuxing   = WUXING_MAP[idx]
status   = STATUS_MAP[wuxing]
energy   = ENERGY_MAP[wuxing]
bar      = "█" * (energy // 10) + "░" * (10 - energy // 10)

print(f"DATE={today}")
print(f"USER={username}")
print(f"TIANGAN={tiangan}")
print(f"WUXING={wuxing}")
print(f"STATUS={status}")
print(f"ENERGY={energy}")
print(f"BAR={bar}")
