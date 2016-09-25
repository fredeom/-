# [Многабукаф][1] будет просмотренно автоматически и составлен лист из ещё неизвестных букаф

**Завести / Run**:
> python my.py

**Input(_[input.txt][2]_):** текст... сложнаааа  
**Input(_[filter.txt][3]_):** понятные букавы  
**Output(_[output1.txt][4]_):** букавы и их частота  
**Output(_[output2.txt][5]_):** букавы и их длина  
**Program(_[my.py][6]_):** читает букавы из input.txt (за вас!), пропускает мимо букавы из filter.txt (ну вы же их знаете) и выводит статистику в двух формах output1.txt (частота появления в тексте), output2.txt (тоже что и output1.txt, но отсортированы по длине букавы).  

**Limitations:**  
1. https://www.python.org/downloads/ нужен  
2. фильтр туп  
3. функционал почти на нуле  

**TODO:**  
* separate project  
* multiple filter files and filter file formats  
* input dependancy resolution  
* more complex букаф's dependancy on each other in context with graph representation and ability to filter complex structures of букаф instead of separate букаф.  

**NOT TODO:**  
* language syntax support should be delegated to separate filter because user might be interested in highlighting of unknown syntax and  de-emphasizing of known syntax.  

[1]: https://youtu.be/d_H-BjA7utA "Привет Михалкову"
[2]: /input.txt "ВХОД#1"
[3]: /filter.txt "ВХОД#2"
[4]: /output1.txt "ВЫХОД#1"
[5]: /output2.txt "ВЫХОД#2"
[6]: /my.py "Жми сюда!"
