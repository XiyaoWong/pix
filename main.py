import dl
import json
import os
import sys
import time

import config
import parse

try:
    parse.main()
    dl.main()
except KeyboardInterrupt:
    print("正在退出...")
    sys.exit()
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
