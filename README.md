# На входе - текст, на выходе - список слов с частотой их появления отсортированный по частоте, либо по длине слова.

**Завести / Run**:
> python my.py

**Input(_[input.txt][2]_):** текст  
**Input(_[filter.txt][3]_):** слова, которые будут исключены из результатов  
**Output(_[output1.txt][4]_):** слова и их частота  
**Output(_[output2.txt][5]_):** слова и их частота, в порядке убывания длины слова  
**Program(_[my.py][6]_):** утилита на вход получает input.txt и filter.txt, выводит output1.txt и output2.txt  

**Limitations:**  
нужен [Python][1]

**TODO:**  
* separate project  
* multiple filter files and filter file formats  
* input dependancy resolution  
* more complex word's dependancy on each other in context with graph representation and ability to filter complex structures of words instead of separate words.  
* language syntax support should be delegated to separate filter because user might be interested in highlighting of unknown syntax and  de-emphasizing of known syntax.  

[1]: https://www.python.org/downloads/ "Python"
[2]: /input.txt "ВХОД#1"
[3]: /filter.txt "ВХОД#2"
[4]: /output1.txt "ВЫХОД#1"
[5]: /output2.txt "ВЫХОД#2"
[6]: /my.py "Жми сюда!"
