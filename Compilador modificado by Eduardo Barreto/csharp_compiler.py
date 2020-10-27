import os
import datetime

directory = os.listdir('./src')

if 'out' not in os.listdir('./'):
    os.mkdir('./out')

out = open('./out/main.cs', 'w')

data = datetime.datetime.now()

out.write('Last change: ' + str(data.strftime("%d")) + '/' + str(data.strftime("%m")) + '/' + str(data.strftime("%Y")) + ' | ' + str(data.strftime("%X")) + '\n')
out.write('-'*100+'*/\n\n')


os.system('cls')

for source_file in directory:
    if 'cs' in source_file.lower():
        current_file = open('./src/' + source_file, 'r')
        for line in current_file:
            if '//' in line:
                pass
            else:
                out.write(line)
        current_file.close()
        out.write('\n\n')

    else:
        print('-'*20, 'Arquivo inválido:', source_file,'-'*20, end='')
    print('\n', '-'*20, 'Arquivo', source_file[:source_file.lower().find('.')], 'compilado com sucesso', '-'*20)

out.close()
print('\nCompilado com sucesso.\n')
