s = '''import java.util.*;

public class BrainyThings {
  public static void main(String[] args) {
    Integer[] a = {1, 4, 2, 3, 5};
    
    List<Integer> l = Arrays.asList(a);
    System.out.println(l);
    System.out.println(Arrays.toString(a));

    l.set(2, 8);
    System.out.println(l);
    System.out.println(Arrays.toString(a));
  }
}'''

# f('#a366ff', purple)
# f('#ff002b', red)
# f('#0099cc', blue)
# f('#77b300', green)
# f('#ff9900', orange)
f = open('abc.txt', 'w')
red = ['*', '=', 'import', 'public', 'static']
green = ['BrainyThings', 'main']
blue = ['Arrays', 'asList', 'class', 'Integer', 'java', 'String', 'util', 'void']
