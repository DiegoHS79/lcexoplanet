import os

from lcexoplanet.utilities import SpaceMissionFitsDownload

os.system("clear")
print("*" * 20)
down = SpaceMissionFitsDownload("k2", "220522664")
print("*" * 20)
