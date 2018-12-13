try: 
  length = 10;
  width = 0;
  # del(width);
  length/width;

except ZeroDivisionError:
  print("Division by zero is not allowed");
except NameError: 
  print("variable has been used before defining it");