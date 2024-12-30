
def garble_text(text, garble_dict):
    """
    Garbles the input text based on the provided dictionary.

    Parameters:
    text (str): The text to be garbled.
    garble_dict (dict): A dictionary where keys are characters to be replaced and values are their replacements.

    Returns:
    str: The garbled text.
    """
    garbled_text = ''.join(garble_dict.get(char, char) for char in text)
    return garbled_text

""" def test():

  print('hello world')

  inputText = input("Enter your text: ")
  print(f"Current Text, {inputText}")


  garbled = inputText.replace("one", "three")

  print(garbled)

 """

# Example usage
garble_dict = {
    'a': '@',
    'e': '3',
    'i': '1',
    'o': '0',
    's': '$'
}



if __name__ == "__main__":
    inputText = input("Enter your text: ")
    garbled = garble_text(inputText, garble_dict)
    garbled = garble_text(garbled, garble_dict)
    print(garbled)



