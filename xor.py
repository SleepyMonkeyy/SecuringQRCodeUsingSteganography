def code(a,b):



 input_str = a
 key = b
 no_of_itr = len(input_str)
 output_str = ""


 for i in range(no_of_itr):
  current = input_str[i]
  current_key = key[i%len(key)]
  output_str += chr(ord(current)^ord(current_key))

 return output_str
 print("Here's the output :",output_str)