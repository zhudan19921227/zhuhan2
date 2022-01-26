import os
import sys


path = os.path.dirname((os.path.abspath(__file__)))
pub_path = os.path.join(path,'page\\login_page')
sys.path.append(pub_path)

print(sys.path)