"""Implementation of run length encoding"""


def compress(text):

    buffer = []

    prev_char = None
    prev_ctr = 0

    for char in text:
        if char != prev_char:
            if prev_char is not None:
                buffer += f"{chr(prev_ctr)}{prev_char}"
            prev_char = char
            prev_ctr = 0
        prev_ctr += 1

    if prev_char is not None:
        buffer += f"{chr(prev_ctr)}{prev_char}"

    return ''.join(buffer)


def decompress(text):

    buffer = []
    prev_chr = None
    for idx, chr in enumerate(text):
        if idx % 2:
            buffer += chr * ord(prev_chr)
        prev_chr = chr

    return ''.join(buffer)


assert decompress(compress("Boon & Chi")) == "Boon & Chi"
assert 100 * 'k' == decompress('dk')

cat_ascii = r'''
                                                            .-'
                                                         .-'
                                                      .-'
                                                   .-'
                                                .-'
                  /)                         .-'
                 ||                       .-'
                 ||                    .-'
                 ||                 .-'
                 ||              .-'     .------.
                 ||           .-'  __   | *meow* |
                 ||        .-'   .'-/__ |  _.---'
                 |`-------------'    \/ /.'
                 |*                 '| /'
                 |     |          `--'
               .-| |  /_______    |
            .-'  | | <        `.|||               _.'|
         .-'____  \\`.`.       ||||           _.-'_.-|
      .-'  ||   `--`- `.).____ ||||       _.-'_.-'   |
   .-'     ||                 ``-``--._.-'_.-'       |
.-'        ||                         |`-'           |
           ||                         | |            |
           ||                         | |            |
           ||                         | |            |
           ||                         | |            |
           ||                         | |            |
           ||                        |`--;}};.       |
           ||                       .'  o\ }}}}      |
           ||                     .'\      }}}}      |
           ||                     |      )}}}}}      |
           ||                      \    '}}}}}       |
           ||                       L    }}}}}}      |
           ||                       |  _.}}}}}}      |
           ||                    .-'|.'.-`-}}}}}     |
           ||                  .'  |/|/      `.}}    |
           ||                .' /              \}    |
           ||               /  |           \    \    |
           ||              /   |           |\    \   |
           ||            .'   .'\          | \    \  |
           ||          .'   .'  |   `      |  \    \ |
`.         ||        .'   .'    |          |   |    )|
  `.       ||     .-'\  .'      |          (  /   .' |
    `.     ||   _/__.'`'        J          J /   /   |
      `.   || (')               |           /   /    |
        `. ||                   F          <   /     |
          `||                   L        ,/ `./      |
           ||                   `-.__.---/'_/_/      |
           ||                   |       //-'|        |
           ||                   |      //   |        |
           ||                   |      '    |        |
           ||                   |           |        |
           ||                   `-.______.-'         |
           ||                    |    F    |         |
           ||                    (   J|    F         |
           ||                    |   ||   J          |
           ||                    |   |J(   L         |
           ||                    J   F|F   |         |
           ||                    |  J ||   |         |
           ||                    |  |_||   F         |
           ||                   _F  J `|  J          |
           ||               _.-'/_.' ) |  |`.        |
           ||           _.-' .-'  /\/  |  |. `.      |
           ||       _.-'     `---'     F  ) `. `.    |
           ||   _.-'                  /-'/|   `. `.  |
           ||.-'                    .__.'       `. `.|
                                                  `. |
                                                    `|
                                                      `.
  VK                                                    `.
                                                          `.
'''

print("Original length: ", len(cat_ascii))
print("Compressed length: ", len(compress(cat_ascii)))
print("Compressed: ", compress(cat_ascii))
print("Decompressed: ", decompress(compress(cat_ascii)))
print(f"Compression percentage: {100 * (len(cat_ascii) - len(compress(cat_ascii))) / len(cat_ascii)} %")

assert decompress(compress(cat_ascii)) == cat_ascii
