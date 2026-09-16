// O(n)

class Solution {
    public int calPoints(String[] operations) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i<operations.length; i++) {
            int now = list.size()-1;
            switch (operations[i]) {
                case "C":
                    list.remove(now);
                    break;
                case "D":
                    list.add(list.get(now) * 2);
                    break;
                case "+":
                    list.add(list.get(now) + list.get(now-1));
                    break;
                default:
                    list.add(Integer.parseInt(operations[i]));
            }
        }
        int sum = 0;
        for (int l : list) sum += l;
        return sum;
    }
}
