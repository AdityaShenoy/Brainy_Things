import java.util.*;

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
}