class Solution {
    public int reinitializePermutation(int n) {
        int[] original = new int[n];
        int[] perm = new int[n];
        int[] tmp = new int[n];

        int ans = 0;

        for(int i=0; i<n; i++) {
            original[i] = i;
            perm[i] = i;
            tmp[i] = i;
        }

        while(true) {
            boolean check = true;
            for(int i=0; i<n; i++) {
                if(i%2==0) tmp[i] = perm[i/2];
                else tmp[i] = perm[n / 2 + (i - 1) / 2];
            }

            ans++;

            for(int i=0; i<n; i++) {
                perm[i] = tmp[i];
                if(original[i] != perm[i]) {
                    check = false;
                } 
            }   
            if(check) break;
        }

        return ans;
    }
}