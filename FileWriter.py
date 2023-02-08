# Raihan Khalil Abdillah, 30065695
# AT2.4 Question 2
# File Writer

lines = ["Python\n",
         "\n",
         "Python is a high-level, interpreted, general-purpose programming language.\n" "Its design philosophy "
         "emphasizes "
         "code readability with the use of significant indentation.\n",
         "\n",
         "Python is dynamically-typed and garbage-collected.\nIt supports multiple programming paradigms, including "
         "structured (particularly procedural), object-oriented and functional programming.\nIt is often described as "
         "a 'batteries included' language due to its comprehensive standard library.\n",
         "\n",
         "Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language "
         "and first released it in 1991 as Python 0.9.0.\nPython 2.0 was released in 2000 and introduced new features "
         "such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.\n"
         "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier "
         "versions.\nPython 2 was discontinued with version 2.7.18 in 2020.\n",
         "\n",
         "Python consistently ranks as one of the most popular programming languages.\n"
         "\n"
         "taken from https://en.wikipedia.org/wiki/Python_(programming_language)"]
# https://en.wikipedia.org/wiki/Python_(programming_language)

file = open("news.txt", 'w')
file.writelines(lines)
file.close()
