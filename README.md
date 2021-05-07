<div align="center">
  
<h1>AI-bot</h1>

</div>

</div>

![AI-bot](https://socialify.git.ci/hitblunders/AI-bot/image?description=1&descriptionEditable=An%20NLP%20based%20intelligent%20chatbot&font=Raleway&forks=1&issues=1&language=1&owner=1&pattern=Overlapping%20Hexagons&pulls=1&stargazers=1&theme=Dark)

<div align="center">
  <img src="http://ForTheBadge.com/images/badges/uses-js.svg">
</div>

<div>

**Intelligent bot**

This is an NLP(Natural Language Processing) based chatbot that communicates with the user via textual methods. This chatbot uses Bag of Words Model.

The whole process of creating the chatbot is broken down in few major steps - 

  1) **Tokenize:** Tokenization is the technique for chopping text up into pieces, called tokens, and at the same time throwing away certain characters, such as punctuation. These tokens are linguistically representative of the text.

  2) **Word Stemming:** Stemming a word is attempting to find the root of the word. For example, the word "thats" stem might be "that" and the word "happening" would have the stem of "happen". This process of stemming words reduces the vocabulary of the model and attempt to find the more general meaning behind sentences.
 
  3) **Bag of Words:** Each sentence is represented with a list with the length of the amount of words in model's vocabulary. Each position in the list will represent a word from vocabulary. If the position in the list is a 1 then that means that the word exists in the sentence, if it is a 0 then the word is not present. This is called a bag of words because the order in which the words appear in the sentence is lost, we only know the presence of words in model's vocabulary.

  4) **Neural Network:** A simple Neural Network is used to train the model.

  5) **GUI:** **tkinter** package is used to create GUI elements using widgets found in Tk toolkit.
