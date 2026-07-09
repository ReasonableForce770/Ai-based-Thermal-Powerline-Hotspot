import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler as ss

data = pd.read_csv(r"C:\Users\call2\OneDrive\Dtu\Course\projects\Thermal_Powerline_Dataset.csv")
df=data.copy()
data.head()   