#instalar biblioteca tqdm: Essas bibliotecas fornecem funcionalidades prontas para criar barras de progresso de forma simples e eficiente
#pip install tqdm

from tqdm import tqdm
import time

#exibe a barra
for i in tqdm(range(100)):
    time.sleep(0.05)