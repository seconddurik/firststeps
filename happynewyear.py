# из модуля datetime класс datetime
from datetime import datetime

# модуль time полностью
import time

# бесконечный цикл пока True(верно) и до break
while True:
    
    # текущее время на компе (локально)
    now = datetime.now()
    
    # now.year + 1 ======> 2026 + 1 = 2027 и тд / строго (год, месяц, день)
    new_year = datetime(now.year + 1, 1, 1)
   
    # разница между будущим и текущим
    delta = new_year - now
    
    # если 0 секунд и меньше ===> новый год
    if delta.total_seconds() <= 0:
        print("С Новым годом!")
        
        # выходим из цикла (чтобы бесконечно не спамило)
        break

# Расклад разницы (строчка 16-17) на дни/часы/минуты/секунды
    # дни уже отдельной строчкой
    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    print(
#\033[2K\ стирает старую строку с экрана
        f"\033[2K\rДо Нового года осталось: {days} дн. {hours:02d}:{minutes:02d}:{seconds:02d}",
        end="",
        flush=True,
    )


    time.sleep(1)