int countOccurrences(string s, int K) 
{ 
    int n = s.length(); 
    int C, c1 = 0, c2 = 0; 
    for (int i = 0; i < n; i++) { 
        if (s[i] == 'a') 
            c1++; // Count of 'a's 
        if (s[i] == 'b') { 
            c2++; // Count of 'b's 
            C += c1; // occurrence of "ab"s in string S 
        } 
    } 
