public class _824 {
    public String toGoatLatin(String sentence) {
        String vowels = "aeiouAEIOU";
        StringBuilder result = new StringBuilder();
        int cnt = 0;
        String last = "a";
        for (int i = 0; i < sentence.length(); i++) {
            char start = sentence.charAt(i++);
            if (vowels.indexOf(start) >= 0) {
                result.append(start);
                while (i < sentence.length() && sentence.charAt(i) != ' ') {
                    result.append(sentence.charAt(i++));
                }
            } else {
                while (i < sentence.length() && sentence.charAt(i) != ' ') {
                    result.append(sentence.charAt(i++));
                }
                result.append(start);
            }
            result.append("ma");
            cnt++;
            for (int j = 0; j < cnt; j++) {
                result.append(last);
            }
            if (i < sentence.length()) {
                result.append(" ");
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        _824 solution = new _824();
        System.out.println(solution.toGoatLatin("I speak Goat Latin"));
        System.out.println(solution.toGoatLatin("Each word consists of lowercase and uppercase letters only"));
    }
}
