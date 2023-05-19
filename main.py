"""
Platformer Game
"""
import arcade
import random


words = open('word.txt', 'r').read().split('\n')

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hangman"

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window=True)

        arcade.set_background_color(arcade.csscolor.DARK_OLIVE_GREEN)

        self.word = None
        self.guess = None
        self.lives = None


    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.word = random.choice(words)
        print(self.word)
        self.lives = 7
        self.guess = []
        self.corrected_guess = []
        pass

    def on_draw(self):
        """Render the screen."""
        # Code to draw the screen goes here
        self.clear()


        arcade.draw_text(f'lives : {self.lives}', 10,SCREEN_HEIGHT - 50, arcade.csscolor.WHITE, 18)
        arcade.draw_text(f'Guess : {self.guess}', 10,10, arcade.csscolor.WHITE, 18)
        self.draw_word()

        if self.lives == 0:
            arcade.draw_text('Perdu', SCREEN_WIDTH/2,SCREEN_HEIGHT/2, arcade.csscolor.WHITE, 50)
            self.setup()

        tmp = 0
        for ch in self.word:
            if ch in self.guess:
                tmp += 1
        if tmp == len(self.word):
            arcade.draw_text('gagne', SCREEN_WIDTH/2,SCREEN_HEIGHT/2, arcade.csscolor.WHITE, 50)
            self.setup()
          

    def on_key_press(self, key, modifier):
        print(self.guess)
        if 97 <= key <= 122:
            if chr(key) in self.guess:
                return('Value already selected')
            else:
                self.guess.append(chr(key))
                if chr(key) in self.word:
                    self.corrected_guess.append(chr(key))
                else:
                    self.lives -= 1  

        print(f"Guess {self.guess}")
        print(f"Guess correct {self.corrected_guess}")

    def draw_word(self):
        letter_witdh = 100
        letter_espacement = 30

        start = SCREEN_WIDTH - ((len(self.word) -1)  * letter_witdh) - letter_espacement * (len(self.word) -2) 
        for x in range(len(self.word)):
            arcade.draw_rectangle_filled(letter_witdh * x + letter_espacement *x + start/ 2,150,100,100,arcade.csscolor.DARK_RED)

        for value in self.word and self.guess:
            indexes = find(self.word, value)
            for i in indexes:
                arcade.draw_text(value, letter_witdh * i + letter_espacement *i + start/ 2, 150, arcade.csscolor.WHITE, 18 )

def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()