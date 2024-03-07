## COMMON LIST ALGORITHMS

## Collecting values that matches a criteria
## =========================================
scores = [90, 85, 60, 48, 75, 45, 80, 35, 40]

# finding values greater than 50
threshold = 50
result = []
for x in scores:
    if x > threshold:
        result.append(x)
  
print('scores:', scores)
print('scores > 50:', result)

# Finding values greater than 50 along with their indicies.
# Here, for each match, we collect a Tuple where the 1st value is 
#       the index and the second value is the score.
result2 = []
for index in range(len(scores)):
    if scores[index] > threshold:
        result2.append((index, scores[index])) 

print('scores:', scores)        
print('(indexes, score) of scores > 50:', result2)



## Removing all Matches
## ====================

# Removing all words that has less than 4 characters
words = ['Welcome', 'to', 'the', 'island']
print('Initial list:', words)
i=0
while i < len(words):
    if len(words[i]) < 4:
        words.pop(i) # Remove the i-th element. Note: when the 
                     # element is removed, the next element comes
                     # to the i-th place. Therefore, we should not
                     # increment i so that we will test the next 
                     # word in the next iteration.
    else:
        i = i + 1 # increment i.
           
print('Final list:', words)

 
