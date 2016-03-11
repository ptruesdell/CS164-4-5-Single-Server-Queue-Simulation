# Case 6 (Line switch):

  
elif (getNextEvent() == ts):

   
t = ts

   ts = generateSwitchTime()

  
 maxLineLength = max(len(line1), len(line2), len(line3), len(line4))

   
# Set longest line

   
if (maxLineLength == len(line1)):

       
longestLine = list(line1)

   
elif (maxLineLength == len(line2)):

 
      longestLine = list(line2)

   
elif (maxLineLength == len(line3)):

   
    longestLine = list(line3)

  
 else:

   
    longestLine = list(line4)

  
 lastInLineIndex = longestLine[maxLineSize - 1]

   
longestLine.pop()



  
 if(cmp(longestLine, getShortestLineSwitch(longestLine)) == False):

   
    if (len(getShortestLineSwitch(longestLine)) == 0):

    
       if (cmp(line1, getShortestLineSwitch(longestLine)) == True):

     
           td1 = generateDepartureTime()

     
      elif (cmp(line2, getShortestLineSwitch(longestLine)) == True):

        
        td2 = generateDepartureTime()

       
    elif (cmp(line3, getShortestLineSwitch(longestLine)) == True):

       
         td3 = generateDepartureTime()

       
    elif (cmp(line4, getShortestLineSwitch(longestLine)) == True):

        
        td4 = generateDepartureTime()

    
   getShortestLineSwitch(longestLine).push(lastInLineIndex)



