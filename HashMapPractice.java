//package Example;

import java.util.HashMap;
import java.util.Map;

public class HashMapPractice {
    public static void main(String[] args) {
        String[] strings = {"a", "b", "a", "f", "b", "a", "z"};
        System.out.println(wordCount(strings));
    }

    private static Map<String, Integer> wordCount(String[] strings) {
        Map<String, Integer> map = new HashMap<>();
        for (String s : strings) {
            if (!map.containsKey(s))
                map.put(s, 1);
            else {
                int count = map.get(s);
                map.put(s, count++);
            }
        }
        return map;
    }
}
