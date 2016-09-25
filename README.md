# Многабукаф (https://youtu.be/d_H-BjA7utA) будет просмотренно автоматически и составлен лист из ещё неизвестных букаф

Input(input.txt): текст... сложнаааа
Input(filter.txt): понятные букавы
Output(output1.txt): букавы и их частота
Output(output2.txt): букавы и их длина
Program(my.py): читает букавы из input.txt (за вас!), пропускает мимо букавы из filter.txt (ну вы же их знаете) и выводит статистику в двух формах output1.txt (частота появления в тексте), output2.txt (тоже что и output1.txt, но отсортированы по длине букавы).

Limitations:
1) https://www.python.org/downloads/ нужен
2) фильтр туп
3) функционал почти на нуле

TODO:
* separate project
* multiple filter files and filter file formats
* input dependancy resolution
* more complex букаф's dependancy on each other in context with graph representation and ability to filter complex structures of букаф instead of separate букаф.

NOT TODO:
* language syntax support should be delegated to separate filter because user might be interested in highlighting of unknown syntax and  de-emphasize known syntax.
