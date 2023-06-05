
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Printar o Sistema Operacional que voce esta usando:
# YOUR CODE HERE

print("Sistema Operacional:", sys.platform)

# Printar a versão de Python que voce esta usando:
# YOUR CODE HERE

print("Versão do Python:", sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Printar a process Id atual
# YOUR CODE HERE
print("ID do Processo:", os.getpid())

# Printar o atual diretório:
# YOUR CODE HERE
print("Diretório Atual:", os.getcwd())

# Printar o nome da maquina
# YOUR CODE HERE
print("Nome da Máquina:", os.uname().nodename)
