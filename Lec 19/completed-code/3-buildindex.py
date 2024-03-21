## 
#  This program builds the index of a book from terms and page numbers.
#

def main() :
   # Create an empty dictionary.
   indexEntries = {}
   
   # Extract the data from the text file.
   infile = open("indexdata.txt", "r")
   fields = extractRecord(infile)
   while len(fields) > 0 :
      addWord(indexEntries, fields[1], fields[0])
      fields = extractRecord(infile)
      
   infile.close()
   
   # Print the index listing.
   printIndex(indexEntries)
 
## Extract a single record from the input file.
#  @param infile the input file object
#  @return a list containing the page number and term or an empty list if
#  the end of file was reached
#
def extractRecord(infile) :
   line = infile.readline()
   if line != "" :   
      fields = line.split(":")      
      page = int(fields[0])
      term = fields[1].rstrip()
      return [page, term]
   else :
      return []   
   
## Add a word and its page number to the index.
#  @param entries the dictionary of index entries
#  @param term the term to be added to the index
#  @param page the page number for this occurrence of the term
#
def addWord(entries, term, page) :   
   # If the term is already in the dictionary, add the page to the set.
   if term in entries :
      pageSet = entries[term]
      pageSet.add(page)
      
   # Otherwise, create a new set that contains the page and add an entry.
   else :
      pageSet = set([page]) # We make this a SET rather than a LIST to
                            # avoid same page appearing more than once
                            # for a given term.
      entries[term] = pageSet

## Print the index listing.
#  @param entries a dictionary containing the entries of the index
#
def printIndex(entries) :
   for key in sorted(entries) :
      print(key, end=" ")
      pageSet = entries[key]
      first = True
      for page in sorted(pageSet) :
         if first :
            print(page, end="")
            first = False
         else :
            print(",", page, end="")
         
      print()
      
# Start the program.
main()

