import java.lang.Integer;

/*
define a function called "consecutive_zeroes" that takes a single parameter which is a string of zeros and ones

"1100110101" e.g

the function should find the largest amount of consecutive zeros
in the example aboffve that is "2"

"0" should output 1
1100011 should output 3

my solution:
simply convert the string into an int
>WARNING! if done so and string starts with one 0 or more, those zeroes get deleted, and those zeroes might be exactly the longest conseq. row, so:
>just add a "1" beforehand.
and then simply run thru the number.

or even easier; turn into array
*/


public class MyClass {
    public static void main(String args[]) {
      String succ = "00001010101010110101000100010100100010010010100000";
      int lengthy = succ.length();
      int[] intArray = new int[lengthy];


      for(int i = 0; i < lengthy; i++){
          intArray[i] = Character.getNumericValue(succ.charAt(i));
      }

      int currently = 0;
      int biggestSoFar = 0;

      for(int i = 0; i < lengthy; i++){
          if(intArray[i] == 0){
              currently++;
              if(currently > biggestSoFar){
                  biggestSoFar = currently;
              }
          } else {
              currently = 0;
          }
      }

      System.out.println("the biggest 0-consecutive row is: " + biggestSoFar);
    }
}
