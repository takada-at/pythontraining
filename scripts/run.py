import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import bbs
app = bbs.get_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0')
