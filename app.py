import re

text = """
5. It is known (a) ----- all that one day all will pass away (b) ----- this earth. So, we have no escape (c) ----- death. One day, we all will roll down (d) ----- the lap of death. Because death is common (e) ----- all. So we should not mourn (f) ----- the dead. But those who die (g) ----- the country are immortal. Their memories do not sink (h) ----- oblivion. There is no medicine that can save a man (i) ----- death. So, we should always be ready (j) ----- death.

6. If you want to derive the best (a) --- your education you must be fully aware (b) --- some basic things. You should never be indifferent (c) --- your study. In Fact, fostering a kind of passion (d) --- learning appears to be very important for achieving your goal. Again, you should never try to learn anything (e) --- context. You should also not run (f) --- substandard traditional guide books. As a matter of fact, confining yourself (g) --- poor quality note books discourages you to learn something deeply. But (h) --- learning a thing very deeply, you cannot achieve the required mastery (i) --- the learnt thing. Thus, you may fail to get the desired benefits (j) --- your learning.

7. Life of common people besets (a) ----- a number of troubles. Price spiral has added new sufferings (b) ----- our life. Indeed, price of daily commodities has gone (c) ----- the ability of the common people. Lack (d) ----- supervision is responsible (e) ----- it. Some dishonest businessmen devoid (i) ----- morality hoard goods (g) ----- quick profit. The govt. should take punitive action (h) ----- those people. People from all walks (i) ----- life should also co-operate (j) ----- government. 
"""

# Add *** before question numbers at the beginning of lines (like 6. or 7.)
text = re.sub(r'^(\d+\.)', r'***\1', text, flags=re.MULTILINE)

# Add *** at the end of paragraphs that end with a full stop
text = re.sub(r'(\.)(\s*\n)', r'\1***\2', text)

print(text)
