DOT = "."
DASH = 3 * "-"
SPACE_PART = " "
SPACE_LETTER = 3 * " "
SPACE_WORD = 7 * " "

class MorseCode:
    """Single class that encodes a text message into morse code"""
    
    
    def __init__(self) -> None:
        """Initialize the morse code table"""
        self.letter_table = {
            "A": f"{DOT}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "B": f"{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "C": f"{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "D": f"{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "E": f"{DOT}{SPACE_LETTER}",
            "F": f"{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "G": f"{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "H": f"{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "I": f"{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "J": f"{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "K": f"{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "L": f"{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "M": f"{DASH}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "N": f"{DASH}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "O": f"{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "P": f"{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "Q": f"{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "R": f"{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "S": f"{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "T": f"{DASH}{SPACE_LETTER}",
            "U": f"{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "V": f"{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "W": f"{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "X": f"{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "Y": f"{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "Z": f"{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "1": f"{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "2": f"{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "3": f"{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "4": f"{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DASH}{SPACE_LETTER}",
            "5": f"{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "6": f"{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "7": f"{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "8": f"{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "9": f"{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DOT}{SPACE_LETTER}",
            "0": f"{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_PART}{DASH}{SPACE_LETTER}"
        }
    

    def encode(self, message: str) -> str:
        """Encodes an alphanumeric message into morse code"""
        encoded_message = []
        text_message = message.upper()
        for word in text_message.split(" "):
            if word.isalnum():
                for letter in word:
                    encoded_message.append(self.letter_table[letter])
                # Remove final letter end space
                encoded_message[-1] = encoded_message[-1].rstrip()
                encoded_message.append(SPACE_WORD)
            else:
                raise RuntimeError(f"'{word}' is not alphanumeric.")
        # Remove end word space
        encoded_message[-1] = encoded_message[-1].rstrip()

        return "".join(encoded_message)
