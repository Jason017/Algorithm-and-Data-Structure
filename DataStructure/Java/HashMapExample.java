import java.util.HashMap;
import java.util.Map;

public class HashMapExample {
    public static void main(String[] args) {
        String[] strings = { "a", "b", "a", "f", "b", "a", "z" };
        System.out.println(wordCount(strings));
    }

    private static Map<String, Integer> wordCount(String[] strings) {
        Map<String, Integer> map = new HashMap<>();
        for (String s : strings) {
            if (!map.containsKey(s))
                map.put(s, 1);
            else
                map.put(s, map.get(s) + 1);
        }
        return map;
    }
}
