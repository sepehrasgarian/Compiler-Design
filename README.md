# Compiler-Design
This project is my implementation of the compiler course's projects under the supervision of Dr. Saeedeh Momtazi.(Spring 2020) 
In the first phase, the purpose is denoted to provide a Lexical analyzer that can recognize the words in the code and identify each symbol. Furthermore, in this section analyzer can determine if the word is correct or not, and if it is wrong, it has to declare the wrong part. 

In addition to the first phase, in the next point, a Bottom-Up parser(LALR) is designed.  The given grammar in the test cases folder is ambiguous. Thus in this section, the goal is to Resolve ambiguity by using Priorities. I implemented this part by using the ply library.[https://www.dabeaz.com/ply/]
