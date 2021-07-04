import argparse

def sum(a,b):
  return a+b

if __name__=="__main__":
   parser=argparse.ArgumentParser()
   parser.add_argument('--param1',help="Enter first argument")
   parser.add_argument('--param2',help="Enter second argument")
   arg=parser.parse_args()
   print("Displaying the sum")
   print(sum(int(arg.param1),int(arg.param2)))

   
   