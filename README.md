# CodeAlpha_Internship
Intership project showcasing Python programming concepts, problem-solving, and real-world application development.

# 1. Hangman Game Assignment
This is a simple text-based Hangman game build in Python. The player has to guess a randomly chosen word by entering one letter at a time. The game ends when the player either guesses the word correctly or uses all 6 incorrect guesses.

> Features : 

●​ Randomly selects a word from a predefined list of 5 words.   <br>
●​ Displays guessed letters and underscores for remaining ones. <br>
●​ Console-based input/output.          <br>
●​ Ends the game when:                  <br>
    - The player guesses the word, or  <br>
    - The player makes 6 wrong guesses.

> Concepts Used :

●​ 'randome' module             <br>
●​ 'while' loop                 <br>
●​ 'if-else' conditions         <br>
●​ Strings & Lists              <br>
●​ Console-based input/output.  <br>

> Example Gameplay

Welcome to Hangman!             <br>
Word: _ _ _ _ _                 <br>
Enter a letter: a               <br>
Good guess! Word: a _ _ a _     <br>
Enter a letter: z               <br>
Wrong guess! You have 5 tries left.

# 2. Stock Portfolio Tracker Assignment
A beginner-friendly Python project that tracks stock investments using hardcoded prices. Users can enter stock names and quantities, calculate the total investment, and optionally save the results to .txt or .csv files. Demonstrates use of dictionaries, loops, arithmetic operations, and file handling in Python.

> Features : 

●​ Predefined stock prices stored in a dictionary.  <br>
●​ User inputs stock symbols and quantities.        <br>
●​ Calculates total investment value.               <br>
●​ Option to save results in:                       <br>
    - TXT file <br>
    - CSV file

> Concepts Used :

●​  Python 3                            <br>
●​  Dictionary                          <br>
●​  File handling ('txt' and 'csv')     <br>

> Example Gameplay

Welcome to Stock Portfolio Tracker          <br>
Available stock prices:                     <br>
AAPL: $180                                  <br>
TSLA: $250                                  <br>
GOOGL: $135                                 <br>
MSFT: $320                                  <br>
AMZN: $140                                  <br>

Enter stock symbol (or 'dome' to finish): aapl      <br>
Enter quantity for AAPL: 10                         <br>

Enter stock symbol (or 'dome' to finish): tsla      <br>
Enter quantity for TSLA: 5                          <br>

Enter stock symbol (or 'dome' to finish): amzn      <br>
Enter quantity for AMZN: 10                         <br>

Enter stock symbol (or 'dome' to finish): done      <br>

Stock       Quantity        Price       Investment  <br>
--------------------------------------------------- <br>
AAPL            10           $180         $1800     <br>
TSLA            5            $250         $1250     <br>
AMZN            10           $140         $1400     <br>
--------------------------------------------------- <br>
TOTAL                                     $4450

