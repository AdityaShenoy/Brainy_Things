package programming.java.util.Arrays.asList;

import java.util.*;

public class BrainyThings {
    public static void main(String[] args) {
        // Converting primitve boolans into List of its non-primitive wrapper class Boolean by using boxing.
        List<Boolean> lBoolean = Arrays.asList(true, false, false, true, true);
        System.out.println(lBoolean);
        
        // Converting primitve bytes into List of its non-primitive wrapper class Byte by using boxing.
        List<Byte> lByte = Arrays.asList((byte)1, (byte)2, (byte)3, (byte)4, (byte)5);
        System.out.println(lByte);

        // Converting primitve chars into List of its non-primitive wrapper class Character by using boxing.
        List<Character> lCharacter = Arrays.asList('a', 'b', 'c', 'd', 'e');
        System.out.println(lCharacter);

        // Converting primitve doubles into List of its non-primitive wrapper class Double by using boxing.
        List<Double> lDouble = Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0);
        System.out.println(lDouble);

        // Converting primitve floats into List of its non-primitive wrapper class Float by using boxing.
        List<Float> lFloat = Arrays.asList(1.0f, 2.0f, 3.0f, 4.0f, 5.0f);
        System.out.println(lFloat);

        // Converting primitve ints into List of its non-primitive wrapper class Integer by using boxing.
        List<Integer> lInteger = Arrays.asList(1, 2, 3, 4, 5);
        System.out.println(lInteger);

        // Converting primitve longs into List of its non-primitive wrapper class Long by using boxing.
        List<Long> lLong = Arrays.asList(1L, 2L, 3L, 4L, 5L);
        System.out.println(lLong);

        // Converting primitve shorts into List of its non-primitive wrapper class Short by using boxing.
        List<Short> lShort = Arrays.asList((short)1, (short)2, (short)3, (short)4, (short)5);
        System.out.println(lShort);

        // Converting Strings into List of Strings.
        List<String> lString = Arrays.asList("a","b","c","d","e");
        System.out.println(lString);
    }
}