import dl
import json
import os
import time

import config
import parse

try:
    parse.main()
    dl.main()
except Exception:
    pics = os.listdir(config.IMAGES_SAVE_DIR)
    data = {
        'pics': pics,
        'last_update': int(time.time()),
        'count': len(pics)
    }
    with open(os.path.join(config.BASE_DIR, 'data.json'), 'w') as f:
        json.dump(data, f)
    print('更新data.json成功')
finally:
    pics = os.listdir(config.IMAGES_SAVE_DIR)
    data = {
        'pics': pics,
        'last_update': int(time.time()),
        'count': len(pics)
    }
    with open(os.path.join(config.BASE_DIR, 'data.json'), 'w') as f:
        json.dump(data, f)
    print('更新data.json成功')
